#!/bin/bash
# $1 control command
# $2 the save path of recorded video

if [ $# -ne 0 ]; then
    if [[ $1 == "start" && $# -eq 2 ]]; then
        cat room_list.txt | while read room_id container_name
        do
            docker run --name $container_name -v `readlink -f $2`:/app/video -d bililive $room_id
        done
    elif [ $1 == "stop" ]; then
        cat room_list.txt | while read room_id container_name
        do
            docker rm `docker stop $container_name`
        done
    fi
fi