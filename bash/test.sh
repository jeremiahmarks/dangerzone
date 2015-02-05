#!/usr/bin/env bash


if grep "export TASKDDATA" ~/.bashrc
then
    echo bashrc has a TASKDDATA environment variable set.
else
    echo export TASKDDATA=~/.task/server_data >> ~/.bashrc
fi

if grep "source ~/.profile" ~/.bash_profile
	then
		echo I am not adding the line \"source ~/.profile\" to ~/.bash_profile
	else
		echo I am adding the line \"source ~/.profile\" to ~/.bash_profile
		echo source ~/.profile >> ~/.bash_profile
fi