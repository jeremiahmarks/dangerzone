#!/bin/bash
# @Author: jlmarks
# @Date:   2015-02-16 18:39:32
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2015-02-16 19:02:14
# echo "hello"
# for file in connection.php  functions.php index.php my.pw.php
# do
#   # scp $file  gd:~/html/links/
#  scp ~/dangerzone/scripts/php/$file gd:~/html/links/
#  echo
#  echo $file
# done


scp ~/dangerzone/scripts/php/connection.php ~/dangerzone/scripts/php/functions.php ~/dangerzone/scripts/php/index.php ~/dangerzone/scripts/php/my.pw.php gd:~/html/links/