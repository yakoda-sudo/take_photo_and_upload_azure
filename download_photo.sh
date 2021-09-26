#!/bin/bash -x
curl -X GET -H "x-ms-date: $(date -u)" "https://yourstorageaccount.blob.core.windows.net/team/?[your_sas_token]" > result.xml && xmllint --format result.xml | grep -Po '<.*?>\K.*?(?=<.*?>)' | grep jpg > filelist.txt
mapfile -t photoarray < filelist.txt
for i in "${photoarray[@]}"
    do 
	photoname="$i"
	url="https://yourstorageaccount.blob.core.windows.net/team/${photoname}?[your_sas_token]"
        curl -X GET -H "x-ms-date: $(date -u)" "$url" -o ./$photoname -s
#	echo $photoname
    done
echo "download finished"     
