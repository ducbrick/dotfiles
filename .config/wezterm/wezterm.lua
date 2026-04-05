-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices.

config.front_end = "WebGpu"

config.enable_tab_bar = false

config.color_scheme = 'Catppuccin Mocha'

config.default_prog = { '/usr/bin/fish', '-l' }

config.window_padding = {
  left = 15,
  right = 15,
  top = 15,
  bottom = 15,
}

config.window_background_opacity = 0.9

config.font = wezterm.font 'JetBrainsMono Nerd Font Mono'

config.font_size = 15

-- Finally, return the configuration to wezterm:
return config
