if status is-interactive
	# Commands to run in interactive sessions can go here

	set --universal fish_greeting
	set --universal tide_left_prompt_items pwd git newline character
	set --universal tide_pwd_bg_color brmagenta
	set --universal tide_pwd_color_anchors black
	set --universal tide_pwd_color_dirs black
	set --universal tide_pwd_color_truncated_dirs brblack

	fish_add_path /home/ducbrick/.local/bin
	fish_add_path /home/ducbrick/.cargo/bin/

	set -x EDITOR nvim

	zoxide init fish | source
	fzf --fish | source

end

function yaz
	set tmp (mktemp -t "yazi-cwd.XXXXXX")
	yazi $argv --cwd-file="$tmp"
	if read -z cwd < "$tmp"; and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
		builtin cd -- "$cwd"
	end
	rm -f -- "$tmp"
end

function za
	set sessions (zellij list-sessions --no-formatting)
	set chosen (printf '%s\n' $sessions | fzf --prompt='Enter session name: ')

	if test -n "$chosen"
		zellij attach (string split ' [' $chosen)[1]
	end
end

function zd
	set sessions (zellij list-sessions --no-formatting)
	set chosens (printf '%s\n' $sessions | fzf --multi --prompt='Enter session name: ')

	for chosen in $chosens
		set sessionName (string split ' [' "$chosen")[1]
		zellij kill-session $sessionName
		zellij delete-session $sessionName
	end
end
