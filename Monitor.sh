#!/bin/sh

liveon="正在直播"
liveoff="直播停止"
live=0

path='/home/pi/tools/Monitor'

accpet=`cat $path/config.json | jq -r '.getInfo.headers.Accept'`
origin=`cat $path/config.json | jq -r '.getInfo.headers.Origin'`
referer=`cat $path/config.json | jq -r '.getInfo.headers.Referer'`
useragent=`cat $path/config.json | jq -r '.getInfo.headers."User-Agent"'`
url=`cat $path/config.json | jq -r '.getInfo.url'`
roomid=`cat $path/config.json | jq -r '.comments.room.roomid'`

var=`curl -s -H "$accpet" -H "$origin" -H "$referer" -H "useragent" $url | jq -r '.data.name'`
echo "正在监控$var的直播间"
echo "直播间号：$roomid"

while :
do
	MSG=`sudo python3 $path/check.py`
	if [ $MSG = $liveon ]
		then
		echo -ne "$(date) 直播开始 \r"
		if [ $live == 0 ]
			then
			`bash /home/pi/tools/Monitor/send.sh $var`
			live=1
		fi
	elif [ $MSG = $liveoff ]
		then
		echo -ne "$(date) 直播未开始 \r"
		if [ $live == 1 ]
			then
			live=0
		fi
	fi
	sleep 5m
done
