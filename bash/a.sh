#!/usr/bin/env bash

#First, use rsync to sync my main web server

# rsync -rzunP -e "ssh" jeremiahmarks@jlmarks.org:/home/content/06/6816406/html/books ~/mycode/mysite

# rsync -rzunP -e "ssh" ~/mycode/mysite jeremiahmarks@jlmarks.org:/home/content/06/6816406



#Get files from Godaddy server:

# rsync -rzuP -e "ssh" jeremiahmarks@jlmarks.org:/home/content/06/6816406/ ~/mycode/mysite/



# BACKUPFILENAME="/home/jlmarks/BU.7z"
# 7z u -t7z -mx=9 -up1q0r2x1y2z1w2  $BACKUPFILENAME -i@/home/jlmarks/mycode/included.txt -xr@/home/jlmarks/mycode/excluded.txt

# if [[ `hostname -s` = *nv55c ]]; then
#     scp $BACKUPFILENAME lrm:$BACKUPFILENAME
# fi

# hello="A B  C   D"
# echo $hello   # A B C D
# echo "$hello" # A B  C   D
# As we see, echo $hello   and   echo "$hello"   give different results.

# a=123456789123
# echo $a
# b=${a/23/ab}
# echo $b


# echo; echo

# echo "\v\v\v\v"      # Prints \v\v\v\v literally.
# # Use the -e option with 'echo' to print escaped characters.
# echo "============="
# echo "VERTICAL TABS"
# echo -e "\v\v\v\v"   # Prints 4 vertical tabs.
# echo "=============="

# echo "QUOTATION MARK"
# echo -e "\042"       # Prints " (quote, octal ASCII character 42).
# echo "=============="

# # The $'\X' construct makes the -e option unnecessary.
# echo; echo "NEWLINE AND BEEP"
# echo $'\n'           # Newline.
# echo $'\a'           # Alert (beep).

# echo "==============="
# echo "QUOTATION MARKS"
# # Version 2 and later of Bash permits using the $'\nnn' construct.
# # Note that in this case, '\nnn' is an octal value.
# echo $'\t \042 \t'   # Quote (") framed by tabs.

# # It also works with hexadecimal values, in an $'\xhhh' construct.
# echo $'\t \x22 \t'  # Quote (") framed by tabs.
# # Thank you, Greg Keraunen, for pointing this out.
# # Earlier Bash versions allowed '\x022'.
# echo "==============="
# echo


# # Assigning ASCII characters to a variable.
# # ----------------------------------------
# quote=$'\042'        # " assigned to a variable.
# echo "$quote This is a quoted string, $quote and this lies outside the quotes."

# echo

# # Concatenating ASCII chars in a variable.
# triple_underline=$'\137\137\137'  # 137 is octal ASCII code for '_'.
# echo "$triple_underline UNDERLINE $triple_underline"

# echo

# ABC=$'\101\102\103\010'           # 101, 102, 103 are octal A, B, C.
# echo $ABC

# echo; echo

# escape=$'\033'                    # 033 is octal for escape.
# echo "\"escape\" echoes as $escape"
# #                                   no visible output.

# echo; echo

# exit 0
################################################################################
################################################################################
####
##
##	recursively calling self
##
####
# echo "continue?"
# read
# /$0
####
####
################################################################################
################################################################################

################################################################################
##
## trying various code from reddit comments
##
################################################################################


# function dirtree {                                                          
#   local file dir=$1 indent=$2
#   while read file; do
#     if [ "$file" != "$dir" ]; then
#       echo "$indent"$(basename "$file")
#       if [ -d "$file" ]; then
#         dirtree "$file" "$indent    "
#       fi
#     fi
#   done < <(find "$dir" -maxdepth 1 -type d; find "$dir" -maxdepth 1 -type f)
# }
# dirtree $PWD ''


################################################################################
################################################################################
##																	############
##																	############
##		real	4m2.205s											############
##		user	0m52.947s											############
##		sys		3m14.874s											############
																	############
																	############
# find . ! -name '.' -printf '%d %f\n' |                            ############
# while read depth file; do											############
#   for i in $(seq 1 $(($depth - 1))); do							############
#     printf "%s" "    "											############
#   done															############
#   printf "%s\n" "$file"											############
# done																############
##																	############
##																	############
################################################################################
################################################################################




# find . ! -name '.' -printf '%d %f\n' |
# while read depth file; do
#   printf '%*s\n' $((depth - 1)) | sed -e "s/\ /    /g;s/$/$file/"



# done


# ##############
# ##figuring out loops and string building
# ##############
# nstring="start of string"
# for a in {a..f}
# do
#   nstring+=$a
# done
# echo $nstring

# ##i added something

aa=true 
# bb=false
cc="python"
if [[ "$aa" ]]; then echo "Test0" ; fi
if [[ "$bb" ]]; then echo "Test0.1" ; fi
if [[ !"$aa" ]]; then echo "Test0.2" ; fi
if [[ ! "$aa" ]]; then echo "Test0.3" ; fi
if [[ "$aa" && ! "$bb" ]]; then echo "Test1" ; fi
if [[ "$aa" && ! "$aa" ]]; then echo "Test2" ; fi
if [[ "$aa" ]] && ! [[ "$bb" ]]; then echo "test3" ; fi
if [[ "$aa" ]] && ! [[ "$cc" ]]; then echo "test4" ; fi
if [[ $aa && ! $bb ]]; then echo "Test5" ; fi
if [[ $aa && ! $aa ]]; then echo "Test6" ; fi
if [[ $aa ]] && ! [[ $bb ]]; then echo "test7" ; fi
if [[ $aa ]] && ! [[ $cc ]]; then echo "test8" ; fi
if [[ $aa ]] && [[ $cc ]]; then echo "test9" ; fi