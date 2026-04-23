#!/usr/bin/env fish

# Set timer values in minutes
set work_time 25
set break_time 5

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
