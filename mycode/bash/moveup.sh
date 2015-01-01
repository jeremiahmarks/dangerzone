#!/usr/bin/env bash
# @Author: Jeremiah Marks
# @Date:   2014-03-30 00:30:15
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2014-03-30 13:59:45

#This script is intended to be used to consolidate all files that match a search 
#pattern into a destination folder through a recursive search of a target folder.
#Basically you tell it what to look for, where to look, and where to collect its 
#findings. The search paramaters need to be quoted.
#Example use of this script: <br>
# moveup.sh ~/Pictures "*.jpg" .


moveup() {
  local file dest=$1 searchstr=$2 dir=$3
  cd "$dir" || return
  for file in .* *; do
    # skip current/previous dirs and unresolved wildcards
    case "$file" in
    "." | ".." | ".*" | "*" ) continue ;;
    esac

    if [[ "$file" = $searchstr ]]; then 
      fcounter=0    
      newname="$file"

      #As long as the file exists in the future home it runs through the do loop
      #changing the potential name and incrementing the counter 
      while [[ -e "$dest$newname" ]]; do  
        newname="$fcounter.$file"
        ((fcounter++))
      done
      mv "$file" "$dest$newname"
    fi 
    # recursively traverse/indent directories that are not symlinks
    if [[ -d "$file" && ! -L "$file" ]]; then
      moveup "$dest" "$searchstr" "$file"
    fi
  done
  cd ..
}

#Add a slash to the end of the $1 variable for two reasons:
#   1. many people will not add a / to the end of the folder name and it needs to be there
#   2. if the variable is empty, that can affect tests.  
dest="$1/"

#Check and see if we added an extra / at the end of the destination. if we did: remove it.
[[ "$dest" = *// ]] && dest="${dest#?}" 

#if the dest = / that indicates that it was not passed to the script
#so we assume that the $PWD is the desired location.
#we also change relative links to absolute links using the readlinks command.
if [[ "$dest" = / ]]; then dest="$PWD/"; else dest="$(readlink -m $dest)/"; fi
if [[ -z "$3" ]]; then startloc=$PWD; else startloc="$(readlink -m $3)"; fi


echo "I intend to move files that match the pattern"
echo "${2:-*.txt}"
echo "recursively from"
echo "$startloc"
echo "into"
echo "$dest"
read -p "do you want to continue?" -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
  then
    moveup "$dest" "${2:-*.txt}" "$startloc" 
    # calls the function "moveup" with three paramaters. 
    # 1 is set it uses that as the directory to place the files in
    # 2 look for files that match the pattern. if not set look for *.txt files
    # 3 start directory. If not set it will start in the current working directory
fi
