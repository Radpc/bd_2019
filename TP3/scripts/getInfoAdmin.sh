#!/bin/bash
# Get info while being superuser

if [ "$EUID" -ne 0 ]
  then echo "rs tu precisa ser sudo amigao"
  exit
fi

INFOFOLDER="infoAdmin"

mkdir -p $INFOFOLDER
hdparm -I /dev/sda >> $INFOFOLDER/hdparm_sda.txt
blockdev --getsize64 /dev/sda >> $INFOFOLDER/disksize.txt
