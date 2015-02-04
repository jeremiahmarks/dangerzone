#!/bin/sh
# @Author: Jeremiah Marks
# @Date:   2015-02-03 23:29:02
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2015-02-04 01:01:24

# An application that I did a long time ago asked that I write a 
# script in either bash or python that checks the status of a server
# and if it is down emails to a notification address.

# What I did then does not bear being seen, it was one of the worst
# pieces of code I think that I have ever written.
# This is that attempt, except in bash.  I hope that this is actually worth sharing!

# I am using the solution found at 
#	http://stackoverflow.com/a/8937694/492549
# as a jumping off point

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
	#echo $messageText  > ~/thismessage.txt
	cat ~/thismessage.txt
	ssmtp jeremiah@jlmarks.org < ~/thismessage.txt
}

#setips
#echotest
sendmessage

