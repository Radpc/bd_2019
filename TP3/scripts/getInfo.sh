#!/bin/bash
# Script para o TP3


INFOFOLDER="info"

mkdir -p $INFOFOLDER
lscpu >> $INFOFOLDER/lscpu.txt
lshw >> $INFOFOLDER/lshw_incomplete.txt

df -h >> $INFOFOLDER/df_all.txt
df -h /home >> $INFOFOLDER/df_this_disk.txt