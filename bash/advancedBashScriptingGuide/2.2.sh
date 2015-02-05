#!/usr/bin/env bash
# @Author: Jeremiah Marks
# @Date:   2014-03-27 18:52:51
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2014-03-27 19:14:42

# System administrators often write scripts to automate common tasks. 
# Give several instances where such scripts would be useful.

# Automating backup and logfile cleanup
# Automating file sorting

# Write a script that upon invocation shows the time and date, 
	#  lists all logged-in users, and gives the system uptime. 
	#  The script then saves this information to a logfile.
DATA="$(date)
$(users) 
$(uptime)"

echo "$DATA"

echo "$DATA" >> logfile.txt
