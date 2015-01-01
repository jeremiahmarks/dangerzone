#!/usr/bin/env bash

# this code will sync ~/mycode between my personal computers
rsync -urtP -e "ssh" 192.168.1.110:~/mycode/ /home/jlmarks/mycode/
rsync -urtP  /home/jlmarks/mycode/ -e "ssh" 192.168.1.110:~/mycode/