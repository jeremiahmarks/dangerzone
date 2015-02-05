#!/usr/bin/env bash
# @Author: jlmarks
# @Date:   2014-03-18 16:59:18
# @Last Modified by:   jlmarks
# @Last Modified time: 2014-03-18 18:28:29

#This script basically takes any files that are created or updated on my local 
#server and uploads them to my godaddy server. 


FILE=/home/jlmarks/mycode/mylogs/gdsync-$(date +"%F-%T").log
#echo "FROM gd : $(date +"%F-%T")" >> $FILE 2>&1
#rsync -iurtP -e "ssh" gd:~/html/ /home/jlmarks/mycode/mysite/ >> $FILE 2>&1
echo "TO gd : $(date +"%F-%T")" >> $FILE 2>&1
rsync -iurtP --exclude '.git' /home/jlmarks/mycode/mysite/ -e "ssh" gd:~/html/ >> $FILE
echo "DONE : $(date +"%F-%T")" >> $FILE 2>&1
