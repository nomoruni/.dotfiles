from libqtile.config import Key 

from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import groups

groups = groups.groups

mod = "mod4"
mod1 = "mod1"
terminal = guess_terminal()


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
    Key([mod, "shift"], "u", lazy.window.bring_to_front(), desc="Move window up"),
    Key([mod1], "space", lazy.window.toggle_minimize(), desc="Toggle Window Minimize"),
    Key([mod1, "shift"], "space", lazy.window.toggle_maximize(), desc="Toggle Window Maximize"),


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
    Key([mod], "Tab", lazy.screen.toggle_group(), desc="Toggle between layouts"),
    Key([mod1], "Tab", lazy.group.next_window(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "delete", lazy.spawn("rofi -show power-menu -modi power-menu:/home/nomoruni/.config/rofi/rofi-power-menu"), desc="Power Menu" ),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle Floating" ),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen" ),

###Programs Shortcuts Keys###

    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Rofi Menu" ),
    Key([mod], "w", lazy.spawn("firefox"), desc="Firefox" ),
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="PcManFM" ),
    # Key([mod], "r", lazy.spawn("kitty NNN_FIFO=/tmp/nnn.fifo nnn -a"), desc="Yazi File Manager" ),
    Key([mod], "b", lazy.spawn("rofi-bluetooth"), desc="Rofi Bluetooth Manager Menu" ),
    Key([mod], "p", lazy.spawn("/home/nomoruni/.config/rofi/rofi-randr"), desc="Rofi Randr" ),
    Key([mod , "shift"], "c", lazy.spawn("xcolor -s clipboard"), desc="Color Picker" ),
    Key([mod, "shift"], "n", lazy.spawn("/home/nomoruni/.config/rofi/rofi-network-manager/rofi-network-manager.sh"), desc="Rofi Network Manager Menu" ),
    Key([mod], "g", lazy.spawn("rofi -modi emoji -show emoji"), desc="Power Menu" ),
    Key([mod], "c", lazy.spawn("rofi -modi calc -show calc"), desc="Power Menu" ),
    Key([mod,"shift"], "s", lazy.spawn("rofi-screenshot"), desc="Power Menu" ),

###Audio and Brightness Control####

    Key([],"XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Volume up"),
    Key([],"XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Volume up"),
    Key([],"XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Volume up"),
    Key([],"XF86AudioMicMute", lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"), desc="Volume Down"),
    Key([],"XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Brightness Down"),
    Key([],"XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+"), desc="Brightness Up"),
]

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
