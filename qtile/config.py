# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
mod1 = "mod1"
terminal = guess_terminal()


##
## COLOR SETS
##

col_orange_200 = "#d65d0e"
col_orange_100 = "#fe8019"
col_yellow_100 = "#fabd2f"
col_yellow_200 = "#d79921"
col_gray_10 = "#fbf1c7"
col_gray_20 = "#ebdbb2"
col_gray_30 = "#bdae93"
col_gray_40 = "#a89984"
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

##
##


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


        Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),


        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


        Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),


        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


        Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),


        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes

#Key(
#        [mod, "shift"],
#        "Return",
#        lazy.layout.toggle_split(),
#        desc="Toggle between split and unsplit sides of stack",
#        ),

Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "delete", lazy.spawn("rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu"), desc="Power Menu" ),
    Key([mod, "shift"], "n", lazy.spawn("/home/nomoruni/.config/rofi/rofi-network-manager/rofi-network-manager.sh"), desc="Rofi Network Manager Menu" ),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle Floating" ),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen" ),
    Key([mod, "shift"], "b", lazy.spawn("rofi-bluetooth"), desc="Rofi Network Manager Menu" ),

###Programs Shortcuts Keys###

    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Rofi Menu" ),
    Key([mod], "w", lazy.spawn("firefox"), desc="Rofi Menu" ),
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="Rofi Menu" ),
    Key([mod], "r", lazy.spawn("alacritty -e ranger"), desc="Rofi Menu" ),

###Audio and Brightness Control####

    Key([],"XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Volume up"),
    Key([],"XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Volume up"),
    Key([],"XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Volume up"),
    Key([],"XF86AudioMicMute", lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"), desc="Volume Down"),
    Key([],"XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Brightness Down"),
    Key([],"XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+"), desc="Brightness Up"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + letter of group = move focused window to group
                # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                      #     desc="move focused window to group {}".format(i.name)),
                ]
            )

layouts = [
        layout.Columns(border_focus = col_yellow_100, border_normal = col_gray_200, border_width=4, margin=5),
        # layout.Max(),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
        layout.floating.Floating(border_focus = col_yellow_100, border_normal = col_gray_200, border_width=4)
        ]

widget_defaults = dict(
        font="caskaydiacovenerdfont",
        fontsize=14,
        padding=3,
        )
extension_defaults = widget_defaults.copy()



screens = [
        Screen(
            bottom=bar.Bar(
                [
                    widget.CurrentLayout(),
                    widget.GroupBox(
                        highlight_method = 'block',
                        this_current_screen_border='8ec07c',
                        rounded = False,
                        background = col_aqua_300,
                        margin = 3,
                        ),
                    widget.Prompt(background = col_red_200, foreground = col_gray_300),
                    widget.Sep(linewidth=0, padding=10),
                    widget.TaskList(padding_y = 3,
                                    margin_y = 0,
                                    icon_size = 16,
                                    txt_floating = "🗗 ",
                                    txt_maximized = "🗖 ",
                                    txt_minimized = "🗕 ",
                                    rounded = False,
                                    #borderwidth = 3, 
                                    highlight_method = 'block',
                                    border = '458588', 
                                    max_title_width = 200),
                    #widget.Chord(
                    #    chords_colors={
                    #        "launch": (col_red_200, col_gray_10),
                    #        },
                    #    name_transform=lambda name: name.upper(),
                    #    ),
                    widget.Sep(linewidth=-1, padding=5),
                    widget.Systray(),
                    widget.Sep(linewidth=0, padding=10),
                    widget.Battery(battery = "CMB1",
                                   format = '{char} {percent:2.0%} {watt:.2f}W',
                                   background = col_green_200,
                                   low_background = col_red_200, 
                                   foreground = col_gray_300, 
                                   low_foreground = col_gray_10,
                                   charge_char = "󰂄", 
                                   discharge_char = "󰁿", 
                                   full_char = "󱟢",
                                   empty_char = "󰂎", 
                                   ),
                    widget.Sep(linewidth=0, padding=5),
                    widget.Clock(format="%d/%m/%Y %I:%M%p", background = col_yellow_100, foreground = col_gray_300),
                    widget.Sep(linewidth=0, padding=5),
                    widget.PulseVolume(background = col_orange_100, foreground = col_gray_200,limit_max_volume = True, fmt = '󰕾 {}'),
                    widget.Sep(linewidth=0, padding=5),
                    widget.Backlight(background = col_gray_20, foreground = col_gray_200, backlight_name = "intel_backlight", fmt = ' {}'),
                    widget.Sep(linewidth=0, padding=5), 
                    widget.WidgetBox([
                        #widget.Bluetooth(background = col_yellow_100, foreground = col_gray_300), 
                        widget.Sep(linewidth=0, padding=5),
                        widget.CPU(background = col_blue_200, foreground = col_gray_300),
                        widget.Sep(linewidth=0, padding=5),
                        widget.Memory(background = col_red_100, foreground = col_gray_300),
                        widget.Sep(linewidth=0, padding=5),
                        widget.Net(background = col_purple_100, foreground = col_gray_300),
                        ],
                                     background = col_yellow_200, 
                                     foreground = col_gray_300,
                                     ),
                    #widget.QuickExit(),
                ],
                24,
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                background = col_gray_200,
                foreground = col_gray_10,
                ),
                wallpaper = '/home/nomoruni/.config/qtile/Gruvbox/ALLqk82.png',
                wallpaper_mode = 'fill',
            ),
        ]

# Drag floating layouts.
mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            Match(wm_type="utility"),
            Match(wm_type="notification"),
            Match(wm_type="toolbar"),
            Match(wm_type="splash"),
            Match(wm_type="dialog"),
            Match(wm_class="file_progress"),
            Match(wm_class="confirm"),
            Match(wm_class="dialog"),
            Match(wm_class="download"),
            Match(wm_class="error"),
            Match(wm_class="notification"),
            Match(wm_class="splash"),
            Match(wm_class="toolbar"),
            Match(func=lambda c: c.has_fixed_size()),
            Match(func=lambda c: c.has_fixed_ratio()),
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            Match(wm_class="feh"),  # GPG key password entry
            Match(wm_class="vlc"),  # GPG key password entry
            Match(wm_class="Windscribe"),  # GPG key password entry
            ], 
        border_width = 4,
        border_focus = col_blue_200,
        border_normal = col_gray_200,
        )
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
follow_mouse_focus = True 

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
#wl_input_rules = None

"""
wl_input_rules = {
        "type:touchpad": InputConfig(left_handed = False, tap = True, natural_scroll = True),
        #"*": InputConfig(left_handed=True, pointer_accel=True),
        "type:keyboard": InputConfig(kb_layout='us', kb_variant = 'intl'),
        }
"""

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
