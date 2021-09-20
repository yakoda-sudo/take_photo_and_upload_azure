#!/bin/sh
cd /home/stevek
filename=image-"`date +"%Y-%m-%d-%H%M"`".jpg
url="https://hackerphotoea.blob.core.windows.net/team/${filename}?sv=2020-08-04&ss=bfqt&srt=sco&sp=rwdlacuptfx&se=2022-09-16T21:11:26Z&st=2021-09-16T13:11:26Z&spr=https&sig=CQY9NQTfQWg4XvId%2FHr3E%2FcJxNbCQpZzU8XHLrN0m8w%3D"
sudo /usr/bin/raspistill -o /home/stevek/$filename -w 1200 -h 1600 -t 1000 -a "Hello from your team"
curl -X PUT -T ./image-"`date +"%Y-%m-%d-%H%M"`".jpg -H "x-ms-date: $(TZ=GMT date '+%a, %d %h %Y %H:%M:%S %Z')" -H "x-ms-blob-type: BlockBlob" "$url"
exit
