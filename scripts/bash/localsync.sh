#!/usr/bin/env bash

# this code will sync ~/mycode between my personal computers
rsync -urtP -e "ssh" 192.168.1.110:~/mycode/ /remote/pathTo/mycode/
rsync -urtP  /remote/pathTo/mycode/ -e "ssh" 192.168.1.110:~/mycode/

# I am unsure why the -e "ssh" was I remember that it was 
# neccessary to use that.