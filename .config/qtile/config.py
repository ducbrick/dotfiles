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

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

####################################################################################################
#                                                                                                  # 
# █▄▀ █▀▀ █▄█ █▄▄ █ █▄ █ █▀▄ █▀                                                                    #
# █ █ ██▄  █  █▄█ █ █ ▀█ █▄▀ ▄█                                                                    #
#                                                                                                  #
####################################################################################################

mod = "mod4"
terminal = "alacritty"

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

    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, 'shift'], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], 's', lazy.layout.toggle_split()),

    # Close focused window
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),

    # Toggle fullscreen
    Key(
        [mod],
        "m",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    # Toggle floating
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Bring focused window to front
    Key([mod], "f", lazy.window.bring_to_front(), desc="Bring focused window to front"),

    # Reload config
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # Quit
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Launch app
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch an application"),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show run"), desc="Launch an application"),

    # Switch to window
    Key([mod], "w", lazy.spawn("rofi -show window"), desc="Switch to a window"),

    # Screenshot 
    Key([], "Print", lazy.spawn("xfce4-screenshooter"), desc="Take a screenshot"),

    # Volume control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle"), desc='Volume Mute'),
    Key([], "XF86AudioMicMute", lazy.spawn("pactl set-source-mute 0 toggle"), desc='Microphone Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='Pause/Unpause media'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='Play previous'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='Play next'),
]

####################################################################################################
#                                                                                                  #
# █▀▀ █▀█ █▀█ █ █ █▀█ █▀                                                                           #
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█                                                                           #
#                                                                                                  #
####################################################################################################

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

colors = {
    'Rosewater': '#f5e0dc',
    'Pink': '#f5c2e7',
    'Bright Red': '#f37799',
    'Red': '#f38ba8',
    'Maroon': '#eba0ac',
    'Peach': '#fab387',
    'Yellow': '#f9e2af',
    'Lavender': '#b4befe',
    'Green': '#a6e3a1',
    'Teal': '#94e2d5',
    'Sapphire': '#74c7ec',
    'Blue': '#89b4fa',
    'Overlay 0': '#6c7086',
    'Text': '#cdd6f4',
    'Surface 0': '#313244',
    'Base': '#1e1e2e',
    'Mantle': '#181825',
    'Crust': '#11111b',
}

layout_config = {
    'border_focus': colors['Pink'],
    'border_normal': colors['Base'],
    'border_on_single': True,
    'border_width': 2,
    'margin': 5,

}

layouts = [
    layout.Columns(**layout_config, 
                   border_focus_stack = colors['Pink'], 
                   border_normal_stack = colors['Base']),
    layout.Max(**layout_config),
    layout.Bsp(**layout_config),
    layout.Spiral(**layout_config, new_client_position = 'bottom'),
    # layout.MonadTall(**layout_config),
    # layout.MonadWide(**layout_config),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(**layout_config),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.Floating(**layout_config),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

####################################################################################################
#                                                                                                  # 
# █▄▄ ▄▀█ █▀█                                                                                      #
# █▄█ █▀█ █▀▄                                                                                      #
#                                                                                                  #
####################################################################################################

widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=16,
    padding=10,
    foreground=colors['Crust'],
)
extension_defaults = widget_defaults.copy()

# Widgets
separator_config = {
    'fontsize': 24,
    'padding': 0,
}

extra_space = widget.Spacer(length = 10,
                            background = colors['Pink'])
power_button = widget.Image(filename = '~/.config/qtile/icons/power.png',
                            background = colors['Pink'],
                            mouse_callbacks = {'Button1': lazy.spawn('xfce4-session-logout')},)
pink_peach = widget.TextBox(text = '\uE0B0', 
                            background = colors['Peach'], 
                            foreground = colors['Pink'], 
                            **separator_config)
cpu = widget.CPU(format = ' {load_percent:04.1f}%',
                 background = colors['Peach'])
peach_green = widget.TextBox(text = '\uE0B0', 
                            background = colors['Green'], 
                            foreground = colors['Peach'], 
                            **separator_config)
memory = widget.Memory(format = ' {MemUsed:05.2f}{mm}',
                       measure_mem = 'G',
                       background = colors['Green'])
green_blue = widget.TextBox(text = '\uE0B0', 
                            background = colors['Blue'], 
                            foreground = colors['Green'], 
                            **separator_config)
current_layout_icon = widget.CurrentLayoutIcon(background = colors['Blue'],
                                               scale = 0.7,
                                               custom_icon_paths = ['~/.config/qtile/icons'])
blue_crust = widget.TextBox(text = '\uE0B0', 
                             background = colors['Crust'], 
                             foreground = colors['Blue'], 
                             **separator_config)
group_box = widget.GroupBox(background = colors['Crust'],
                            inactive = colors['Crust'],
                            active = colors['Pink'],
                            highlight_method = 'line',
                            margin_x = 10,
                            padding_x = 5,
                            spacing = 0,
                            highlight_color = [colors['Crust'], colors['Surface 0']],
                            this_current_screen_border = colors['Pink'])
crust_base = widget.TextBox(text = '\uE0B0', 
                            background = colors['Base'], 
                            foreground = colors['Crust'], 
                            **separator_config)
window_name = widget.WindowName(background = colors['Base'],
                                foreground = colors['Pink'],
                                max_chars = 80)
base_crust = widget.TextBox(text = '\uE0B2', 
                            background = colors['Base'], 
                            foreground = colors['Crust'], 
                            **separator_config)
current_song_icon = widget.Mpris2(background = colors['Crust'],
                                  foreground = colors['Pink'],
                                  display_metadata = [],
                                  paused_text = '',
                                  playing_text = '',
                                  max_chars = 1)
current_song = widget.Mpris2(background = colors['Crust'],
                             foreground = colors['Pink'],
                             width = 300,
                             display_metadata = ['xesam:title'],
                             no_metadata_text = '~~',
                             paused_text = '{track}',
                             playing_text = '{track}',
                             scroll_delay = 1,
                             scroll_step = 3)
crust_blue = widget.TextBox(text = '\uE0B2', 
                            foreground = colors['Blue'], 
                            background = colors['Crust'],
                            **separator_config)

systray = widget.Systray(background = colors['Blue'])

status_notifier = widget.StatusNotifier(background = colors['Blue'])

blue_green = widget.TextBox(text = '\uE0B2', 
                            background = colors['Blue'], 
                            foreground = colors['Green'], 
                            **separator_config)

battery_icon = widget.BatteryIcon(background = colors['Green'], 
                                  theme_path = '~/.config/qtile/icons')

battery = widget.Battery(format = "{percent:2.0%}", 
                         low_foreground = colors['Bright Red'], 
                         low_percentage = 0.2, 
                         show_short_text = False, 
                         background = colors['Green'])

green_peach = widget.TextBox(text = '\uE0B2', 
                             background = colors['Green'], 
                             foreground = colors['Peach'], 
                             **separator_config)

volume_icon = widget.PulseVolume(volumn_app = "pavucontrol", 
                           background = colors['Peach'],
                           emoji_list = ['', '', '', ''],
                           emoji = True,
                           fontsize = 20,
                           padding = 13)
volume = widget.PulseVolume(volumn_app = "pavucontrol", 
                       mute_format = 'Mut', 
                       background = colors['Peach'])

peach_pink = widget.TextBox(text = '\uE0B2', 
                            background = colors['Peach'], 
                            foreground = colors['Pink'], 
                            **separator_config)

clock = widget.Clock(format = "󱛡 %H:%M %a %d-%m", 
                     background = colors['Pink'])

screens = [
    Screen(
        top=bar.Bar(
            [
                extra_space,
                power_button,
                pink_peach,
                cpu,
                peach_green,
                memory,
                green_blue,
                current_layout_icon,
                blue_crust,
                group_box,
                crust_base,
                window_name,
                base_crust,
                current_song_icon,
                current_song,
                crust_blue,
                systray,
                status_notifier,
                blue_green,
                battery_icon,
                battery,
                green_peach,
                volume_icon,
                volume,
                peach_pink,
                clock,
            ],
            30,
            margin = [10, 5, 5, 5],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper='~/.config/qtile/wallpaper.png',
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
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
floats_kept_above = True
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
        Match(title="Volume Control"),
        Match(title="Bluetooth Devices"),
    ],
    **layout_config,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

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