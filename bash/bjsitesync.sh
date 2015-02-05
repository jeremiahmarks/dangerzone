#!/usr/bin/env bash
# @Author: Jeremiah Marks
# @Date:   2014-03-19 08:26:51
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2014-03-19 20:30:40


#
# 
#Goal have this run with potential flags. 
# noflags = upload content normally
# --delete = delete stuff from remote if it no longer exists locally
# pull = pull files off of remote to local folders

FILE=/home/jlmarks/mycode/mylogs/bjsync-$(date +"%F-%T").log
echo "TO bj : $(date +"%F-%T")" >> $FILE 2>&1
rsync -iurtP --exclude '.git' /home/jlmarks/mycode/mysite/ -e "ssh" bj:/media/silver/mysite/ >> $FILE
echo "DONE : $(date +"%F-%T")" >> $FILE 2>&1
