#!/bin/bash

killall -q polybar
polybar mybar & 
polybar mybar2
echo "Polybar launched" 2>&1 | tee -a /tmp/polybar.log & disown
