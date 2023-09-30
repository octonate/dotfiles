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

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = 'alacritty'
browser = 'qutebrowser'


clear='#00000000'
black='#000000'
#bright colors
yellow_ryb='#fffe12'
medium_aquamarine='#1de8af'
imperial_red='#fd042f'
violet_ryb='#8c05a4'
blue='#1607fe'
aqua='#00ffff'
magenta='ff3ffe'
green='#00f304'

#purples (and light yellow)
light_goldenrod_yellow='#f2e205'
magenta_dye='#ba1b73'
purple_mountain_dye='#a177b3'
flirt='#9e007c'
maximum_blue_purple='#b9a3fe'
rose_pink='#ff73d2'
pink_lace='#ffcffe'
scarletty='#a80541'
purpley='#63038c'

def triangle1(bg_color, fg_color):
    return widget.TextBox(
            text='\u25e5',
            padding=-1,
            fontsize=35,
            background=bg_color,
            foreground=fg_color
            )

def triangle2(bg_color, fg_color):
    return widget.TextBox(
            text='\u25e4',
            padding=-1,
            fontsize=35,
            background=bg_color,
            foreground=fg_color
            )

def triangle3(bg_color, fg_color):
    return widget.TextBox(
            text='\u25e3',
            padding=0,
            margin=0,
            fontsize=35,
            background=bg_color,
            foreground=fg_color
            )

def triangle4(bg_color, fg_color):
    return widget.TextBox(
            text='\u25e2',
            padding=0,
            margin=0,
            fontsize=35,
            background=bg_color,
            foreground=fg_color
            )


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl s 5%+')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl s 5%-')),
    Key([], 'XF86AudioMute', lazy.spawn('ponymix toggle')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('ponymix increase 5')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('ponymix decrease 5')),
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
    layout.Columns(border_focus=imperial_red, border_normal=aqua, border_width=3, margin=6),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(border_focus=aqua, border_normal=light_goldenrod_yellow, border_width=2, margin=6),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='mononoki bold',
    fontsize=12,
    padding=6,
    foreground='#000000'
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=7, background=magenta),
                widget.CurrentLayout(background=magenta, padding=0),
                triangle1(magenta, purpley),
                widget.GroupBox(
                    highlight_method='line', 
                    disable_drag='True', 
                    highlight_color=yellow_ryb, 
                    this_current_screen_border=yellow_ryb, 
                    background=purpley, 
                    padding=3, 
                    margin_x=0,
                    block_highlight_text_color='#000000',
                    inactive='#000000',
                    ),
                triangle2(clear, purpley),
                widget.Prompt(),
                widget.Spacer(),
                #widget.Chord(
                #    background=light_goldenrod_yellow,
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),

                triangle1(clear, medium_aquamarine),
                widget.KeyboardLayout(configured_keyboards=['us colemak', 'us'], background=medium_aquamarine, padding=0), 
                triangle2(yellow_ryb, medium_aquamarine),
                widget.Battery(discharge_char='v', format='{char} {percent:2.0%}', background=yellow_ryb, padding=0),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                triangle1(yellow_ryb, imperial_red),
                widget.Clock(format="%a, %b %d %I:%M %p", background=imperial_red, padding=0),
                triangle2(scarletty, imperial_red),
                widget.QuickExit(background=scarletty, padding=0),
                widget.Spacer(length=7, background=scarletty),
            ],
            18,
            background=clear,
            #border_width=[0, 0, 3, 0],  # Draw top and bottom borders
            #border_color=["000000", "000000", "000000", "000000"]  # Borders are magenta
        ),
        wallpaper='~/Pictures/wallpapers/facerevealwallpaperpixel.png',
        wallpaper_mode='stretch',
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
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
