#!/bin/bash
# @Author: Jeremiah Marks
# @Date:   2015-02-04 22:03:21
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2015-02-04 22:24:28


LOGFILE=~/thislogfile.txt
TEMPSTORAGE=~/serveremail.txt
SERVERS=( 192.168.1.110 192.168.168.1 google.com )

TOADDRESS="jeremiah@jlmarks.org"
FROMADDRESS="jeremiah.l.marks@gmail.com"
SUBJECT="Server status notification"

ipisup(){
	ping -c1 -W1 $1 >> /dev/null
}

serverup(){
	echo "At $(date +%c) server $1 was up" >> $LOGFILE
}

serverdown(){
	echo "At $(date +%c) server $1 was down" >> $LOGFILE
	modulerizedsendmessage $TOADDRESS $FROMADDRESS "$SUBJECT" $1
}

modulerizedsendmessage(){
	# this function requires four variables
	rm -f $TEMPSTORAGE
	touch $TEMPSTORAGE
	chmod 777 $TEMPSTORAGE
	echo "To: $1" >> $TEMPSTORAGE
	echo "From: $2" >> $TEMPSTORAGE
	echo "Subject: $3" >> $TEMPSTORAGE
	echo "

	At $(date +%c) server $4 was down." >> $TEMPSTORAGE
	ssmtp jeremiah@jlmarks.org < $TEMPSTORAGE
}

testips(){
	for i in "${SERVERS[@]}"
	do
		ipisup $i && serverup $i || serverdown $i
	done
}

testips