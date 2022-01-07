# IMPORTS

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess


# RUN AUTOSTART

@hook.subscribe.startup_once
def autostart():
	home = os.path.expanduser('~/.config/qtile/autostart.sh')
	subprocess.run([home])


# SET DEFAULTS
mod = "mod4"
terminal = "kitty"
browser = "qutebrowser"


# KEYBINDS
keys = [
    # SWITCH WINDOWS
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # MOVE WINDOWS
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # RESIZE WINDOWS
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen Window"),

    # TOGGLE SPLIT
    Key([mod, "control"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    
    # SPAWN STUFF
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Web Browser"),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget"),

    # TOGGLE LAYOUTS
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # KILL WINDOW
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # RELOAD/EXIT
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # VOLUME
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 -q set Master 2+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 2-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -c 0 -q set Master toggle")),
]


# GROUPS

#groups = [Group(i) for i in "12345"]

groups = [
        Group(name = "1", label = "🌐"),
        Group(name = "2", layout = "Max",  label = "🎮"),
        Group(name = "3", label = "🗔"),
]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


#LAYOUTS

layouts = [
    
    layout.Columns(
        border_focus=['#FA5E62'],
        border_normal=['#4B1D48'],
        border_width=1,
        grow_amount=2,
        num_colums=3,
        margin = [5,10,5,10]
		),
    layout.Max(
	border_width=0,
	),
    #  Try more layouts by unleashing below layouts.
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
]


#WIDGET DEFAULTS

widget_defaults = dict(
    font='hack',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


#BAR

screens = [
    Screen(
        top=bar.Bar(
            [
	    widget.Spacer(
		length = 5
		),
            widget.CurrentLayoutIcon(
		foreground = 'ab9a6d', 
		scale=.7
		),
            widget.Sep(
		padding = 10, 
		foreground = 'BE4754', 
		linewidth = 3, 
		size_percent = 100
		),
            widget.GroupBox(
		active = 'ab9a6d',
		highlight_method = 'border',
		fontsize = 16
		),
            widget.Sep(
		padding = 10, 
		foreground = 'BE4754', 
		linewidth = 3, 
		size_percent = 100
		),
            widget.Prompt(),
            widget.WindowName(
		foreground = 'ab9a6d', 
		empty_group_string = 'Do Something', 
		fontsize = 16, 
		format = '{name}', 
		markup = False
		),
            #widget.Sep(padding = 10, foreground = 'BE4754', linewidth = 3, size_percent = 100),
            widget.Spacer(
		length = 1500
		),
            #widget.Systray(fontsize = 16),
            widget.Spacer(
		length = 5
		),
            widget.Sep(
		padding = 10, 
		foreground = 'BE4754', 
		linewidth = 3, 
		size_percent = 100
		),
            widget.PulseVolume(
		foreground = 'ab9a6d', 
		fontsize = 16, 
		padding = 3
		),
            widget.Sep(
		padding = 10, 
		foreground = 'BE4754', 
		linewidth = 3, 
		size_percent = 100
		),
	    widget.Clock(
		foreground = 'ab9a6d', 
		format='%A, %B %d %Y - %I:%M %p', 
		fontsize = 16
		),
            widget.Sep(
		padding = 10, 
		foreground = 'BE4754', 
		linewidth = 3, 
		size_percent = 100
		),
	    widget.QuickExit(
		foreground = 'ab9a6d', 
		default_text = 'Logout', 
		fontsize = 16, 
		padding = 3
		),
            widget.Spacer(
		length = 5
		)
	    ],
         30,
         background = "#120612",
	 border_color = "#BE4754",
	 border_width = [2, 2, 2, 2],
	 margin=[6, 10, 6, 10],
         opacity = .7
         ),
    ),
]


# FLOATING STUFF

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


# CONFIG SETTINGS
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = False

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


