vnc=$(ps -a | grep wayvnc)

if [[ $vnc ]]; then
	killall wayvnc
else
	swaymsg exec kitty wayvnc 
fi
