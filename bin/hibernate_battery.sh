#!/bin/bash

capacity=$(cat /sys/class/power_supply/BAT1/capacity)
status=$(cat /sys/class/power_supply/BAT1/status | grep -c Discharging)
while :
do
	if [ $capacity -le 3 ]
	then
		if [ $status -eq 1 ]
		then
			pm-hibernate
		fi
	fi
	sleep 30
done
