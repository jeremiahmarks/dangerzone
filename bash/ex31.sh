#!/bin/sh
# @Author: Jeremiah Marks
# @Date:   2015-02-03 23:12:05
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2015-02-03 23:12:44

# from
#	http://www.tldp.org/LDP/abs/html/special-chars.html#EX8



File=/etc/fstab

{
read line1
read line2
} < $File

echo "First line in $File is:"
echo "$line1"
echo
echo "Second line in $File is:"
echo "$line2"

exit 0
