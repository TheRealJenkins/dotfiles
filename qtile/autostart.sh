#!/bin/sh
xrandr --output DP-0 --mode 3440x1440 --rate 144.00
nitrogen --restore &
picom --experimental-backends --backend glx --xrender-sync-fence &
openrgb --startminimized --profile purple.orp &
spotifyd &

