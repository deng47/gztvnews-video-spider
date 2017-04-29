#!/bin/bash

links=$(python3 /home/pi/test/gztvnews/gztv_news_addr.py | head -3) && echo "$(date) $links" >> "$dir"/testlog
dir='/home/pi/gztvnews'

for link in $links;do
    name=$(echo "$link" | echo "$link" | cut -d'/' -f7)
    echo "$(date) processing $name" >> "$dir"/testlog
    size=$(wget --spider "$link" 2>&1 | grep Length | cut -d' ' -f2)
    ls -l "$dir/$name".mp4 | grep -q $size && echo "$(date) $name.mp4 found" >> "$dir"/testlog && continue
    echo "$(date) run wget -c -t 5 -O $name.mp4" >> "$dir"/testlog
    sudo wget -c -t 5 -O "$dir/$name".mp4 $link && echo "$(date) downloaded $name.mp4" >> "$dir"/testlog
done

archive=$(ls "$dir" | wc -l)
[ $archive -gt 5 ] && rm -f "$dir"/$(ls "$dir" | head -1) && echo "$(date) rm $dir/$(ls "$dir" | head -1)" >> "$dir"/testlog

sudo rm -f /home/pi/gztvnews/db/* && echo "$(date) rm -f /home/pi/gztvnews/db/\*" >> "$dir"/testlog
sudo service minidlna force-reload && echo "$(date) service minidlna force-reload" >> "$dir"/testlog
echo "$(date) job finished" >> "$dir"/testlog
