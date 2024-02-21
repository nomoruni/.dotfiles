from libqtile.config import Screen
from libqtile import bar,widget

from libqtile.lazy import lazy

col_orange_200 = "#d65d0e"
col_orange_100 = "#fe8019"
col_yellow_100 = "#fabd2f"
col_yellow_200 = "#d79921"
col_gray_10 = "#fbf1c7"
col_gray_20 = "#ebdbb2"
col_gray_30 = "#bdae93"
col_gray_40 = "#a89984"
col_gray_60 = "#928374"
col_gray_80 = "#504945"
col_gray_200 = "#3c3836"
col_gray_300 = "#282828"
col_gray_400 = "#1d2021"
col_red_200 = "#cc241d"
col_red_100 = "#fb4934"
col_blue_300 = "#458588"
col_blue_200 = "#83a598"
col_aqua_300 = "#689d6a"
col_aqua_200 = "#8ec07c"
col_green_100 = "#b8bb26"
col_green_200 = "#98971a"
col_purple_100 = "#d3869b"
col_purple_200 = "#b16286"    


screens = [
        Screen(
            bottom=bar.Bar(
                [
                    # widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_gray_300),
                    # widget.CurrentLayout(foreground = col_gray_300,),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_gray_300),
                    widget.GroupBox(
                        highlight_method = 'line',
                        highlight_color = ['3c3836'],
                        this_current_screen_border='cc241d',
                        urgent_border = 'cc241d',
                        active = 'ebdbb2',
                        inactive = '928374',
                        rounded = False,
                        margin = 3,
                        ),
                    # widget.Prompt(background = col_red_200, foreground = col_gray_300),
                    widget.Sep(linewidth=0, padding=20, size_percent = 15),
                    # widget.Spacer(),
                    widget.TaskList(padding_y = 7,
                                    margin_y = 0,
                                    padding_x = 5,
                                    icon_size = 20,
                                    txt_floating = "🗗 ",
                                    txt_maximized = "🗖 ",
                                    txt_minimized = "🗕 ",
                                    rounded = False,
                                    #borderwidth = 3, 
                                    highlight_method = 'block',
                                    border = '504945', 
                                    max_title_width = 200,
                                    foreground = 'ebdbb2'
                                    ),
                    widget.Chord(
                        chords_colors={
                            "launch": (col_red_200, col_gray_10),
                            },
                        name_transform=lambda name: name.upper(),
                        ),
                    # widget.Spacer(),
                    widget.Sep(linewidth=0, padding=20, size_percent = 15),
                    # widget.Sep(linewidth=-4, padding=10, size_percent = 15),
                    # widget.Systray(),
                    # widget.Sep(linewidth=4, padding=10, size_percent = 15),
                    widget.WidgetBox([
                        #widget.Bluetooth(background = col_yellow_100, foreground = col_gray_300), 
                        # widget.Sep(linewidth=4, padding=10, size_percent = 15),
                        widget.CPU(foreground = col_gray_20, format = " {load_percent}%"),
                        widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                        widget.Memory(foreground = col_gray_20, format = "{MemUsed: .0f}{mm}b"),
                        widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                        widget.Net(foreground = col_gray_20, format='󰣺 {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', mouse_callbacks = {'Button1' : lazy.spawn("kitty nmtui")}),
                        widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                                     ],
                                     # background = col_yellow_200, 
                                     foreground = col_red_100,
                                     text_open = "   ", 
                                     text_closed = "   "
                                     ),
                    widget.Battery(battery = "CMB1",
                                   format = '{char} {percent:2.0%}',
                                   # background = col_green_200,
                                   low_background = col_red_200, 
                                   # foreground = col_gray_300, 
                                   foreground = col_gray_20,
                                   low_foreground = col_gray_20,
                                   charge_char = "󰂄", 
                                   discharge_char = "󰁿", 
                                   full_char = "󱟢",
                                   empty_char = "󰂎", 
                                   ),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                    widget.Volume(foreground = col_gray_20, limit_max_volume = True, fmt = '󰕾 {}'),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                    widget.Backlight(foreground = col_gray_20, backlight_name = "intel_backlight", fmt = ' {}'),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                    widget.Clock(foreground = col_gray_20, format="󰥔 %I:%M%p", mouse_callbacks = {'Button1' : lazy.spawn()}),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                    # widget.Sep(linewidth=4, padding=10, size_percent = 15), 
                    #widget.QuickExit(),
                ],
                30,
                border_width = 0,  # Draw top and bottom borders
                border_color= col_gray_200,  # Borders are magenta
                background = col_gray_200,
                foreground = col_gray_20,
                margin = [0,5,4,5],
                ),
                wallpaper = '/home/nomoruni/Datos/Fotos/Wallpaper/new/fkfxk6hl7pp41.jpg',
                wallpaper_mode = 'fill',
            ),
            
            #For dual Screen configuration


        Screen(
            bottom=bar.Bar(
                [
                    # widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_gray_300),
                    # widget.CurrentLayout(foreground = col_gray_300,),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_gray_300),
                    widget.GroupBox(
                        highlight_method = 'line',
                        highlight_color = ['3c3836'],
                        this_current_screen_border='cc241d',
                        urgent_border = 'cc241d',
                        active = 'ebdbb2',
                        inactive = '928374',
                        rounded = False,
                        margin = 3,
                        ),
                    # widget.Prompt(background = col_red_200, foreground = col_gray_300),
                    widget.Sep(linewidth=0, padding=20, size_percent = 15),
                    # widget.Spacer(),
                    widget.TaskList(padding_y = 7,
                                    margin_y = 0,
                                    padding_x = 5,
                                    icon_size = 20,
                                    txt_floating = "🗗 ",
                                    txt_maximized = "🗖 ",
                                    txt_minimized = "🗕 ",
                                    rounded = False,
                                    #borderwidth = 3, 
                                    highlight_method = 'block',
                                    border = '504945', 
                                    max_title_width = 200,
                                    foreground = 'ebdbb2'
                                    ),
                    widget.Chord(
                        chords_colors={
                            "launch": (col_red_200, col_gray_10),
                            },
                        name_transform=lambda name: name.upper(),
                        ),
                    # widget.Spacer(),
                    widget.Sep(linewidth=0, padding=20, size_percent = 15),
                    # widget.Sep(linewidth=-4, padding=10, size_percent = 15),
                    # widget.Systray(),
                    # widget.Sep(linewidth=4, padding=10, size_percent = 15),
                    widget.WidgetBox([
                        #widget.Bluetooth(background = col_yellow_100, foreground = col_gray_300), 
                        # widget.Sep(linewidth=4, padding=10, size_percent = 15),
                        widget.CPU(foreground = col_gray_20, format = " {load_percent}%"),
                        widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                        widget.Memory(foreground = col_gray_20, format = "{MemUsed: .0f}{mm}b"),
                        widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                        widget.Net(foreground = col_gray_20, format='󰣺 {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}', mouse_callbacks = {'Button1' : lazy.spawn("kitty nmtui")}),
                        widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                                     ],
                                     # background = col_yellow_200, 
                                     foreground = col_red_100,
                                     text_open = "   ", 
                                     text_closed = "   "
                                     ),
                    widget.Battery(battery = "CMB1",
                                   format = '{char} {percent:2.0%}',
                                   # background = col_green_200,
                                   low_background = col_red_200, 
                                   # foreground = col_gray_300, 
                                   foreground = col_gray_20,
                                   low_foreground = col_gray_20,
                                   charge_char = "󰂄", 
                                   discharge_char = "󰁿", 
                                   full_char = "󱟢",
                                   empty_char = "󰂎", 
                                   ),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                    widget.Volume(foreground = col_gray_20, limit_max_volume = True, fmt = '󰕾 {}'),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                    widget.Backlight(foreground = col_gray_20, backlight_name = "intel_backlight", fmt = ' {}'),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                    widget.Clock(foreground = col_gray_20, format="󰥔 %I:%M%p", mouse_callbacks = {'Button1' : lazy.spawn()}),
                    widget.Sep(linewidth=0, padding=10, size_percent = 15, foreground = col_blue_300),
                    # widget.Sep(linewidth=4, padding=10, size_percent = 15), 
                    #widget.QuickExit(),
                ],
                30,
                border_width = 0,  # Draw top and bottom borders
                border_color= col_gray_200,  # Borders are magenta
                background = col_gray_200,
                foreground = col_gray_20,
                margin = [0,5,4,5],
                ),
                wallpaper = '/home/nomoruni/Datos/Fotos/Wallpaper/new/fkfxk6hl7pp41.jpg',
                wallpaper_mode = 'fill',
            ),
]       

