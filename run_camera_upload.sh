#!/bin/sh
cd /home/stevek
filename=image-"`date +"%Y-%m-%d-%H%M"`".jpg
url="https://hackerphotoea.blob.core.windows.net/team/${filename}?sv=[your_storage_account_sas_token_here]"
sudo /usr/bin/raspistill -o /home/stevek/$filename -w 1200 -h 1600 -t 1000 -a "Hello from your team"
curl -X PUT -T ./$filename -H "x-ms-date: $(TZ=GMT date '+%a, %d %h %Y %H:%M:%S %Z')" -H "x-ms-blob-type: BlockBlob" "$url"
exit
