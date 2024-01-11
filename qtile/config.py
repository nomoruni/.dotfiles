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

from libqtile import layout, hook
from libqtile.config import Click, Drag, Match 
from libqtile.lazy import lazy
from libqtile.backend.wayland import InputConfig


import screens
import keys
import groups


mod = keys.mod



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
    lazy.spawn('sh /home/nomoruni/.config/qtile/autostart.sh') 


# @hook.subscribe.startup_complete
# def run_every_startup():
#     lazy.spawn("xgifwallpaper -v -s FILL /home/nomoruni/Datos/Fotos/Wallpaper/GIFs/pizza.gif")

keys = keys.keys

groups = groups.groups


layouts = [
        layout.Columns(border_focus = col_gray_20, border_normal = col_gray_300, border_width=1, margin=5),
        # layout.Max(),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(margin_y=5, margin_left=5, font='caskaydiacovenerdfont'),
        # layout.VerticalTile(),
        # layout.Zoomy(margin=5, property_big = '1.0', property_small = '0.1', property_name = 'ZOOM'),
        # layout.Floating(border_width=0, margin=5, border_focus = col_yellow_100, border_normal = col_gray_300 )
        ]

widget_defaults = dict(
        font="caskaydiacovenerdfont",
        fontsize=14,
        padding=3,
        )
extension_defaults = widget_defaults.copy()

screens = screens.screens

# Drag floating layouts.
mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        ]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True
floats_kept_above = False


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
            # Match(wm_class="feh"),             
            # Match(wm_class="vlc"),
            Match(wm_class="Windscribe"),
            Match(wm_class="pcmanfm"), 
            # Match(wm_class="VirtualBox Manager"),
            ], 
        border_width=1,
        margin=5,
        border_focus = col_yellow_100,
        border_normal = col_gray_300 
        )

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
#wl_input_rules = None

wl_input_rules = {
        "type:touchpad": InputConfig(left_handed = False, tap = True, natural_scroll = True, middle_emulation = True, tap_button_map = 'lrm'),
        #"*": InputConfig(left_handed=True, pointer_accel=True),
        "type:keyboard": InputConfig(kb_layout='us', kb_variant = 'intl'),
}

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
