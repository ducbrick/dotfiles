if status is-interactive
	# Commands to run in interactive sessions can go here

	set --universal fish_greeting
	set --universal tide_left_prompt_items pwd newline character
	set --universal tide_pwd_bg_color brmagenta
	set --universal tide_pwd_color_anchors black
	set --universal tide_pwd_color_dirs black
	set --universal tide_pwd_color_truncated_dirs brblack
	set --universal tide_time_bg_color green

	fish_add_path /home/ducbrick/.local/bin

	set -x EDITOR nvim

	zoxide init fish | source

end

function yaz
	set tmp (mktemp -t "yazi-cwd.XXXXXX")
	yazi $argv --cwd-file="$tmp"
	if read -z cwd < "$tmp"; and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
		builtin cd -- "$cwd"
	end
	rm -f -- "$tmp"
end
