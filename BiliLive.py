#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2021/07/24
# @Author   : SeeNight
# @Blog     : https://1145141919810.wang
# @License  : MIT


"""BiliLive

A CLI script that record live stream automatically

Params:
* -r/--room :   Live room id
* -o/--output:  Video save path

Example:
```bash
python ./BiliLive -r 12235923 -o ~/videos
```
"""

from colorama import Fore, init
import requests
import time
import os
import datetime
import sys
import getopt
import json


init(autoreset=True, wrap=True)

# Initialization parameters
room = None
path = None

# Get version
with open("./version.json", "r", encoding="utf8") as f:
    data = json.load(f)
    version = data["version"]
    description = data["description"]

opts, args = getopt.getopt(sys.argv[1:], "r:o:h", ["room=", "output=", "help"])
try:
    for opt, val in opts:
        if opt in ("-r", "--room"):
            room = val
        if opt in ("-o", "--output"):
            path = os.path.abspath(val)
        if opt in ("-h", "--help"):
            print("")
            print("BiliLive version {version}".format(version=version))
            print(description)
            print("")
            print("Usage: python BiliLive.py [-r | --room] [-o | --output] [-h | --help]")
            print("Parameters:")
            print("  -r, --room <room id>\t\tLive room id")
            print("  -o, --output <save path>\tVideo save path")
            print("")
            sys.exit()
except getopt.GetoptError as e:
    sys.exit()

if room is None:
    room = input("[Room ID]: ")
if path is None:
    path = input("[Save Path]: ")

print('[Bili Live] Room ID ' + Fore.LIGHTWHITE_EX + room)
print('[Bili Live] Output Path ' + Fore.LIGHTWHITE_EX + path)


class Live:
    api = {
        "get_room_play_info": "https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomPlayInfo?room_id={room_show_id}",
        "get_room_play_url": "https://api.live.bilibili.com/xlive/web-room/v1/playUrl/playUrl?cid={room_id}&platform=web&qn=10000&https_url_req=1&ptype=16",
        "get_room_info": "https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id={room_id}"
    }

    def __init__(self, roomid: str):
        """Initialize the Live class

        Args:
            roomid: live room id that showed in url
        """
        self.roomid = roomid
        self.roomid = self.get_room_play_info()['room_id']

    def get_room_play_info(self) -> dict:
        """Get live room play info

        Returns:
            A dict that contains the following live information:
            - room_id: Live room real id
            - short_id: Live room short id (some UPs have special room shor id, it will show in url)
            - uid: UPs' uid
            - live_status: Live status (0 is closed, 1 is living, 2 is roteting videos)
        """
        res = json.loads(
            requests.get(
                self.api["get_room_play_info"].format(
                    room_show_id=self.roomid
                )
            ).text
        )['data']
        return res

    def get_room_play_url(self) -> dict:
        """Get live room play stream url

        Returns:
            A dict that contains the following stream information:
            - current_qn: Video resolution
            - quality_description: List of resolution
            - durl: List of stream url
        """
        res = json.loads(
            requests.get(
                self.api["get_room_play_url"].format(
                    room_id=self.roomid
                )
            ).text
        )['data']
        return res

    def get_room_info(self) -> dict:
        """Get room information

        Returns:
            A dict contains room information
        """
        res = json.loads(
            requests.get(
                self.api["get_room_info"].format(
                    room_id=self.roomid
                )
            ).text
        )['data']
        return res

r = Live(room)
print('[Bili Live] Monitor Start')


def formatByte(Byte: str) -> str:
    """ Format bytes as easy-to-read values

    If you have a long bytes value, e.g., 516789154431byte, 
    it looks diffcult to read. So it needs to be formated 
    into an easy-to-read form.

    Args:
        Byte: a byte value.

    Returns:
        A string that easy-to-read bytes value.
        It will be formated into G/M/K/B four form.
    """
    if Byte >= 1073741824:
        res = '{}G'.format(round(Byte/1073741824, 2))
    elif Byte >= 1048576:
        res = '{}M'.format(round(Byte/1048576, 2))
    elif Byte >= 1024:
        res = '{}K'.format(round(Byte/1024, 2))
    else:
        res = '{}B'.format(round(Byte, 2))
    return res


def recordLive(path: str) -> None:
    """ Record live stream

    Record bilibili live stream accroding to setted roomid.

    Args:
        room: live room's id
        path: the path where save files
    """
    global r
    streamInfo = r.get_room_play_url()
    url = streamInfo['durl'][0]['url']

    title = r.get_room_info()['room_info']['title']

    filename = '{}_{}'.format(
        title, datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

    response = requests.get(
        url, 
        headers={
            "User-Agent": "Mozilla/5.0", 
            "Referer": "https://www.bilibili.com/"
        }, 
        stream=True
    )
    with open('{path}/[{room_id}]{filename}.flv'.format(
        path=path,
        room_id=r.roomid,
        filename=filename
    ), 'wb') as f:
        byteCount = 0
        now = datetime.datetime.now()
        nb = byteCount
        speed = '0B/s'
        for data in response.iter_content(chunk_size=1024):
            byteCount += len(data)
            stdout = formatByte(byteCount)

            interval = datetime.datetime.now()
            if (interval - now).seconds >= 1:
                now = interval
                flow = byteCount - nb
                speed = '{}/s'.format(formatByte(flow))
                nb = byteCount
            print(
                '[Bili Live] Recorded {:>8s} @ {:15s}'.format(
                    stdout,
                    speed
                ),
                end="\r",
                file=sys.stdout,
                flush=True
            )
            f.write(data)
            f.flush()
    print('[Bili Live] Save to {}/{}.flv'.format(path, filename))
    return


def main():
    global r
    while True:
        try:
            liveStatus = r.get_room_play_info()['live_status']
            if liveStatus == 1:
                print('[Bili Live] ' + Fore.GREEN + '● {}'.format('Live Start'))
                try:
                    recordLive(path)
                    print('[Bili Live] Live Closed')
                except KeyboardInterrupt:
                    print(
                        '\r[Bili Live] ' + Fore.RED + '● Error' + Fore.RESET + ' You Stoped Recording')
            time.sleep(120)
        except KeyboardInterrupt:
            print('\r[Bili Live] Monitor Stop')
            break


if __name__ == "__main__":
    main()
