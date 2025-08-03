# dotfiles

# Dependencies

+ ***Qtile**: Window manager
+ ***Picom**: Compositor
+ **pactl**: Volume control
+ **playerctl**: Control currently playing media
+ **alacritty**: Terminal emulator
+ **fish**: Shell
+ ***fisher**: Package manager for fish
+ ***tide**: Fish prompt
+ **pyxdg**: Required for Qtile's StatusNotifier widget
+ **dbus-fast** (or dbus-next): Required for Qtile's StatusNotifier widget
+ **dbus-next**: Required for Qtile's Mpris2 widget
+ **psutil**: Required for Qtile's CPU widget
+ **xfsettingsd**: XFCE's settings daemon (convenient to have)
+ **dunst**: Notification daemon
+ **XFCE4 Power Manager**: Power manager from the XFCE DE

# Important notes

+ Dependencies with an asterist(*) should be built from source
+ `chmod +x` the following files: `.config/qtile/autostart.sh`, `.config/rofi/scripts/powermenu/power`
