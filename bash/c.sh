#!/usr/bin/env bash

#First, use rsync to sync my main web server

# rsync -rzunP -e "ssh" jeremiahmarks@jlmarks.org:/home/content/06/6816406/html/books ~/mycode/mysite

# rsync -rzunP -e "ssh" ~/mycode/mysite jeremiahmarks@jlmarks.org:/home/content/06/6816406



#Get files from Godaddy server:

rsync -rzuP -e "ssh" jeremiahmarks@jlmarks.org:/home/content/06/6816406/ ~/mycode/mysite/



TARFILENAME="/home/jlmarks/BU.tar"

tar --update -v -f $TARFILENAME ~/.bash_history
tar --update -v -f $TARFILENAME ~/.bash_profile
tar --update -v -f $TARFILENAME ~/.bashrc
tar --update -v -f $TARFILENAME ~/mycode
tar --update -v -f $TARFILENAME ~/notes
tar --update -v -f $TARFILENAME ~/.ssh/config
tar --update -v -f $TARFILENAME ~/Documents