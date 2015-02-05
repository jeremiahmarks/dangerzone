#!/usr/bin/env bash
# @Author: Jeremiah Marks
# @Date:   2014-03-19 10:20:27
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2014-03-19 10:20:27

#This script will be used to sync the deletions that I have made.

echo "##################################################################"
echo "##################################################################"
echo "## Warning!"
echo "##################################################################"
echo "This script will delete things from your remote directories"
echo "is that ok?"
echo "enter y to proceed:"
echo ""
echo ": "

read CONFIRM

if [[ $CONFIRM == y* ]]; then
	FILE=/home/jlmarks/mycode/mylogs/gddelete-$(date +"%F-%T").log
	echo "TO gd : $(date +"%F-%T")" >> $FILE 2>&1
	rsync -iurtP --exclude '.git' --delete /home/jlmarks/mycode/mysite/ -e "ssh" gd:~/html/ >> $FILE
	echo "DONE : $(date +"%F-%T")" >> $FILE 2>&1
fi
