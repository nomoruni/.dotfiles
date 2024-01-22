# The Sway configuration file in ~/.config/sway/config calls this script.
# You should see changes to the status bar after saving this script.
# If not, do "killall swaybar" and $mod+Shift+c to reload the configuration.

# Produces "21 days", for example
uptime_formatted=$(uptime | cut -d ',' -f1  | cut -d ' ' -f4,5)

# The abbreviated weekday (e.g., "Sat"), followed by the ISO-formatted date
# like 2018-10-06 and the time (e.g., 14:01)
date_formatted=$(date "+%a %F")
time_formatted=$(date "+%H:%M")

volumen=$(awk -F"[][]" '/Left:/ { print $2 }' <(amixer sget Master))

# Get the Linux version but remove the "-1-ARCH" part
# linux_version=$(uname -r | cut -d '-' -f1)

# Returns the battery status: "Full", "Discharging", or "Charging".
battery_status=$(cat /sys/class/power_supply/CMB1/capacity)
battery_status_chargin=$(cat /sys/class/power_supply/CMB1/status) 

network_wlan=$(networkctl status wlan0 | grep 'Online state: online')
network_eth=$(networkctl status enp0s31f6 | grep 'Online state: online')
network_eth_2=$(networkctl status enp0s20f0u1 | grep 'Online state: online')

if [[ $network_eth_2 ]]; then
  net_icon_eth="󰣺"
else
  net_icon_eth="󰣼"
fi

if [[ $network_eth ]]; then
  net_icon_eth_2="󰈁"
else
  net_icon_eth_2="󰈂"
fi

if [[ $network_wlan ]]; then
  net_icon_wlan="󰖩"
else
  net_icon_wlan="󰖪"
fi

if [[ "$battery_status_chargin" == "Charging" ]]; then
  bat_icon="󱐋"
fi
  
if [[ "$battery_status_chargin" == "Full" ]]; then
  bat_icon="󰩐"
fi

if [[ "$battery_status_chargin" == "Not charging" ]]; then
  bat_icon=""
fi

if [[ $battery_status -lt 15 ]]; then
  bat_icon=""
fi

#if [[ $battery_status == 10 ]]; then
#  exec notify-send 'Battery at 10%, charge now!' 
#else


echo $net_icon_wlan " " $net_icon_eth " " $net_icon_eth_2 "  " "  "$volumen " " 󱊣 $battery_status% $bat_icon " " "  "$date_formatted " " "  "$time_formatted " "

