sleep 0.3
volumen=$(awk -F"[][]" '/Left:/ { print $2 }' <(amixer sget Master))

notify-send " 󰕾 Volume $volumen" -t 500
