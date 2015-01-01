#!/usr/bin/env bash
# @Author: Jeremiah Marks
# @Date:   2014-03-28 11:23:03
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2014-03-28 13:37:16

# From http://www.faqs.org/docs/abs/HTML/writingscripts.html
# Home Directory Listing
#     Perform a recursive directory listing on the user's home directory and 
#		save the information to a file. Compress the file, have the script 
# 		prompt the user to insert a floppy, then press ENTER. Finally, save the 
# 		file to the floppy.
################################################################################
##
##	Modifications:
##
##		I don't have a floppy drive, nor a floppy disk. I intend to simply save 
##			the file to the homeDirectory
##
################################################################################
##
##	Thoughts:
	##	Call script with folder, indent level, and output file as flags
	##	Move script to folder
	##	get ls -la
	##	for each file in ls -la
		## if file = . or ..
			## ignore
		## append indent level + file name
		##	if file is a folder:
			## call script with folder, indentlevel+1, and output file as flags


################################################################################
##
##	Current output
##
## jlmarks@NV55C:~/mycode/mybash/advancedBashScriptingGuide$ ./hdl.sh 
## ./hdl.sh: line 62: 07:06:27.932587.html: command not found
##
################################################################################

if [ -z $1 ]					#If there is not a first paramater
	then
		start_dir=$HOME 		#then sets home to the users home directory, 
		indent=0 				# the indent to zero
		outfile=$HOME/hdl.txt 	# and clears/creates the out file.
		:>$outfile
	else
		start_dir=$1
fi

if [ -z $2 ]
	then
		indent=0
		outfile=$HOME/hdl.txt
	else
		indent=$2
fi

if [ -z $3 ]
	then
		outfile=outfile=$HOME/hdl.txt
	else
		outfile=$3
fi

# files_in_dir=$(echo ls -a)
cd $start_dir
files_in_dir=(*)
# FILE_ARRAY=($files_in_dir)
echo $files_in_dir
# echo $FILE_ARRAY