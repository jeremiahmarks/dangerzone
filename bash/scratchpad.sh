#!/bin/bash
# @Author: Jeremiah Marks
# @Date:   2015-02-04 22:03:21
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2015-02-04 23:34:19

# NOTE:  	This script is dependent on you having ssmtp installed and configured.
#			If you do not this script will not work as intended.

################################
# Some History:
#
# An application that I did a long time ago asked that I write a
# script in either bash or python that checks the status of a server
# and if it is down emails to a notification address.
#
# What I did then does not bear being seen, it was one of the worst
# pieces of code I think that I have ever written.
# This is that attempt, except in bash.  I hope that this is actually worth sharing!
#
# I am using the solution found at
#	http://stackoverflow.com/a/8937694/492549
# as a jumping off point
#########################
#
#
#This var is where all status checks are recorded.
LOGFILE=~/thislogfile.txt
#########################
#This var holds the email that is generated.  I really should do it on the fly, but I have not got there yet.
TEMPSTORAGE=~/serveremail.txt
#########################
#This var holds an array of servers that will be checked
SERVERS=( 192.168.1.110 192.168.168.1 google.com )
#########################
#This sets the amount of time that the server waits between checks.
WAITTIME=10m
#########################
#These hold information handy to have to send emails.
TOADDRESS="jeremiah@jlmarks.org"
FROMADDRESS="jeremiah.l.marks@gmail.com"
SUBJECT="Server status notification"
#########################


serverup(){
	#This is the function that is called if the server is up
	#Currently it records the fact that the server was up.
	echo "At $(date +%c) server $1 was up" >> $LOGFILE
}

serverdown(){
	#This is the function that is called when the server is down.
	#Currently it updates the log file with that fact
	#And then passes information to the function that emails someone
	echo "At $(date +%c) server $1 was down" >> $LOGFILE
	modulerizedsendmessage $TOADDRESS $FROMADDRESS "$SUBJECT" $1
}

modulerizedsendmessage(){
	#This function is the one that emails the notification out when it is needed
	#It takes four variables, 
	#		$1 = the to address
	#		$2 = the from address
	#		$3 = the subject line
	#		$4 = the server that is down
	rm -f $TEMPSTORAGE
	touch $TEMPSTORAGE
	chmod 777 $TEMPSTORAGE
	echo "To: $1" >> $TEMPSTORAGE
	echo "From: $2" >> $TEMPSTORAGE
	echo "Subject: $3" >> $TEMPSTORAGE
	echo "

	At $(date +%c) server $4 was down." >> $TEMPSTORAGE
	ssmtp $TOADDRESS < $TEMPSTORAGE
}

testips(){
	#this function traverses an array of servers and attempts to ping them.
	#when the ping command completes it either returns a pass/True value or a 
	#fail/False value.  
	#The line that does the evaluation does the following
	# ping
	#      -cX will ping server X times. In this example we only ping it one time
	#	   -WX sets the time out for a response to X seconds
	# >> /dev/null
	#		redirects the ping spam to null
	# && serverup $i
	#		if the preceding command executed successfully, then pass the function
	#		serverup the value stored in i
	# || serverdown $i
	#		if the preceding command did not execute successfully, then pass
	#		the function serverdown the value of i
	for i in "${SERVERS[@]}"
	do
		ping -c1 -W1 $i >> /dev/null && serverup $i || serverdown $i
	done
}

runloop(){
	while :
	do
		testips
		sleep $WAITTIME
	done
}

runloop
