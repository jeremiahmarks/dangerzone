#!/usr/bin/env bash
# @Author: Jeremiah Marks
# @Date:   2014-03-30 05:10:31
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2014-03-30 05:16:41

for files in 1*.abc
do
 mv "$files" "${files%c}.png"
done