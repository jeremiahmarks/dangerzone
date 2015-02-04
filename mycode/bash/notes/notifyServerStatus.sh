#!/bin/sh
# @Author: Jeremiah Marks
# @Date:   2015-02-03 23:29:02
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2015-02-04 01:37:09

# An application that I did a long time ago asked that I write a 
# script in either bash or python that checks the status of a server
# and if it is down emails to a notification address.

# What I did then does not bear being seen, it was one of the worst
# pieces of code I think that I have ever written.
# This is that attempt, except in bash.  I hope that this is actually worth sharing!

# I am using the solution found at 
#	http://stackoverflow.com/a/8937694/492549
# as a jumping off point

LOGFILE=~/nsslog.txt

TOADDRESS="jeremiah@jlmarks.org"
FROMADDRESS="jeremiah.l.marks@gmail.com"
SUBJECT="I think that I have tried sagan times tonight."
BODY="

This is the body of this message.  Oh my joy if I see it"

setips()
{
	ip_addr=192.168.1.110
	ip_addr2=192.168.112.2
}

echotest()
{
	ping -c1 -W1 $ip_addr || echo 'server is down'
	ping -c1 -W1 $ip_addr2 || echo 'server2 is down'
}

sendmessage(){
	rm ~/thismessage.txt
	touch ~/thismessage.txt
	chmod 777 ~/thismessage.txt
	echo "To: $TOADDRESS" >> ~/thismessage.txt
	echo "From: $FROMADDRESS" >> ~/thismessage.txt
	echo "Subject: $SUBJECT" >> ~/thismessage.txt
	echo "$BODY" >> ~/thismessage.txt
	ssmtp jeremiah@jlmarks.org < ~/thismessage.txt
}

echofunction(){
	#This function will accept the ip address of a server and state if it is up or not
	echo "\n\nNew File attempt\n\n" >> LOGFILE
	ping -c1 -W1 $1 >> LOGFILE || echo "\n\n$1 is down\n\n"

}

modulerizedsendmessage(){
	# this function requires four variables
	rm ~/thismessage.txt
	touch ~/thismessage.txt
	chmod 777 ~/thismessage.txt
	echo "To: $1" >> ~/thismessage.txt
	echo "From: $2" >> ~/thismessage.txt
	echo "Subject: $3" >> ~/thismessage.txt
	createmessage $4  #This is the ip address of the server
	# echo "$4" >> ~/thismessage.txt

}

createmessage(){
	#this function requires the ipaddress that failed and the location of the file to save it to
	dtstamp=$(date +%c)
	echo $dtstamp
	message="At $dtstamp server $1 was down."
	echo "

	$message" >> ~/thismessage.txt
}

ipisup(){
	ping -c1 -W1 $1 >> LOGFILE
}


setips
ipisup $ip_addr || echo "That server is not up"
#echotest
#modulerizedsendmessage $TOADDRESS $FROMADDRESS "$SUBJECT" $ip_addr
#echofunction $ip_addr
#echofunction $ip_addr2
#createmessage
#sendmessage

