sunset=$(ps -a | grep wlsunset)

if [[ $sunset ]]; then 

	pkill wlsunset

else
	
	swaymsg --quiet exec wlsunset 

fi

