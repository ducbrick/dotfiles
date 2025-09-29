#!/usr/bin/fish

set input_file '/home/ducbrick/.config/rofi/scripts/browserlauncher/input.txt'
set theme_file '/home/ducbrick/.config/rofi/scripts/browserlauncher/theme.rasi'

set page (cut -d '|' -f1 $input_file | rofi -dmenu -matching fuzzy -i -tokenize -no-show-icons -p '󰜏 Website' -theme $theme_file)

if test "$status" = 1
	exit 0
end

set urls (grep -F "$page|" $input_file | cut -d '|' -f2)

firefox -url (string split ' ' $urls) &
