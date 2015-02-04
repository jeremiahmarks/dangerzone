#!/bin/sh
# @Author: Jeremiah Marks
# @Date:   2015-02-03 23:29:02
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2015-02-04 00:30:12

# An application that I did a long time ago asked that I write a 
# script in either bash or python that checks the status of a server
# and if it is down emails to a notification address.

# What I did then does not bear being seen, it was one of the worst
# pieces of code I think that I have ever written.
# This is that attempt, except in bash.  I hope that this is actually worth sharing!

# I am using the solution found at 
#	http://stackoverflow.com/a/8937694/492549
# as a jumping off point

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
	messageText="To:jeremiah@jlmarks.org	
	From: jeremiah.l.marks@gmail.com	
	Subject: Crossing my fingers on the first attempt!	
	Hey this is just me. "	
	echo $messageText  > ~/thismessage.txt
	ssmtp jeremiah@jlmarks.org < ~/thismessage.txt
}

#setips
#echotest
sendmessage

