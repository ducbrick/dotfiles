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

function pomodoro -a work_time break_time -d "Start a pomodoro timer"
	# Set default values if arguments are not provided
	if test -z "$work_time"
		set work_time 25
	end
	if test -z "$break_time"
		set break_time 5
	end

	notify-send "Pomodoro" "Work for the next $work_time minutes" -i "timer"

	# --- WORK TIMER ---
	# Multiply by 60 to convert minutes to seconds
	sleep (math "$work_time * 60")

	set work_msg "Great job! Time for a $break_time minute break."

	# Send desktop notification for break
	notify-send "Pomodoro" "$work_msg" -i "timer"

	# --- BREAK TIMER ---
	sleep (math "$break_time * 60")

	set break_msg "Break is over! Time to get back to work."

	# Send desktop notification to get back to work
	notify-send "Pomodoro" "$break_msg" -i "timer"
end
