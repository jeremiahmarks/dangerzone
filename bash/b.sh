#!/bin/bash

BACKUPFILENAME="/home/jlmarks/BU.7z"
7z u -t7z -mx=9 -up1q0r2x1y2z1w2 $BACKUPFILENAME ~/.bash_history
7z u -t7z -mx=9 -up1q0r2x1y2z1w2 $BACKUPFILENAME ~/.bash_profile
7z u -t7z -mx=9 -up1q0r2x1y2z1w2 $BACKUPFILENAME ~/.bashrc
7z u -t7z -mx=9 -up1q0r2x1y2z1w2 $BACKUPFILENAME ~/mycode
7z u -t7z -mx=9 -up1q0r2x1y2z1w2 $BACKUPFILENAME ~/notes
7z u -t7z -mx=9 -up1q0r2x1y2z1w2 $BACKUPFILENAME ~/.ssh
7z u -t7z -mx=9 -up1q0r2x1y2z1w2 $BACKUPFILENAME ~/Documents