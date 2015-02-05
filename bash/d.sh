#!/usr/bin/env bash

TARFILENAME="/home/jlmarks/BU.tar"

tar --update -v -f $TARFILENAME ~/.bash_history
tar --update -v -f $TARFILENAME ~/.bash_profile
tar --update -v -f $TARFILENAME ~/.bashrc
tar --update -v -f $TARFILENAME ~/mycode
tar --update -v -f $TARFILENAME ~/notes
tar --update -v -f $TARFILENAME ~/.ssh/config
tar --update -v -f $TARFILENAME ~/Documents