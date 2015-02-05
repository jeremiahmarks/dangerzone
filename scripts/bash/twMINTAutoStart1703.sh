#!/usr/bin/env bash
################################################################################
#9March2014 1534
	#
	#This file will contain the edits that I am making to get taskd running without
	#any user input: in other words to get the daemon to start without needing to 
	#log into the machine. 
	#Intended changes:
		#1. move the server_settings file to a more appropriate location: likely 
			#one in /var (Since apache keeps its files in /var/www/ i think that
			#that is probably the right location for the files)
		#2. add " export TASKDDATA=~/.task/server_data " and "taskdctl start" to /etc/export

		#3 chmod all the correct folders: so far sudo chmod -R 777 /var/task* ~/.task/*
		#4 move the pidfile and other files that have accidently got added to the wrong location to a 
		#	better location

		



#On ubuntu 12.04 this script will ensure that all dependencies are met to
#install and build task and taskd, it will then install them, set up a taskd 
#server that task can sync with, and generate a taskdconfig file that can
#be imported into mirakel to allow syncing from mirakel to the server

#NOTE: it is likely that the user will need to change the .tasdconfig information
#	to include the address of the server as the default settings are simply "localserver"

#TODO: figure out the whole .bash_profile, .profile, .bashrc thing in order to get it set up 
#	so that $TASKDDATA is a permanant environment variable and taskdctl start is run
#	either at login or poweron

#I think that these are the prereqs, will test later
#apt-get update
apt-get install build-essential cmake libqt4-dev python-setuptools qt4-qmake uuid-dev qt4-dev-tools git gnutls-bin libgnutls-dev


#I choose to keep everything in one local hidden folder. Since .task is used anyway
#I choose to keep all of taskwarrior and taskserver information in that folder

mkdir -p ~/.task
cd ~/.task
export TASKDDATA=/var/taskserver
mkdir -p $TASKDDATA

#These may change, but for now they are the correct download links for both
#task and taskd
git clone https://git.tasktools.org/scm/tm/task.git
git clone https://git.tasktools.org/scm/tm/taskd.git

#cmake, make, and make install taskd and task
cd taskd
cmake .
make
make install

cd ../task
cmake .
make
make install

cd ../taskd
taskd init

#This creates the various certs that you will need to authenticate back and forth.
cd pki
./generate

#copying the various certs into the servers area
cp client.cert.pem $TASKDDATA
cp client.key.pem  $TASKDDATA
cp server.cert.pem $TASKDDATA
cp server.key.pem  $TASKDDATA
cp server.crl.pem  $TASKDDATA
cp ca.cert.pem     $TASKDDATA

#initial configuration of taskd
taskd config --force client.cert $TASKDDATA/client.cert.pem
taskd config --force client.key $TASKDDATA/client.key.pem
taskd config --force server.cert $TASKDDATA/server.cert.pem
taskd config --force server.key $TASKDDATA/server.key.pem
taskd config --force server.crl $TASKDDATA/server.crl.pem
taskd config --force ca.cert $TASKDDATA/ca.cert.pem

cd $TASKDDATA/..
taskd config --force log $PWD/taskd.log
taskd config --force pid.file $PWD/taskd.pid
taskd config --force server localhost:53589
taskd config --force ip.log 1
taskd config --force client.allow '^task [2-9],^taskd,^libtaskd,^Mirakel [1-9]'


# http://mirakel.azapps.de/scripts/add_user.sh
###########################################
##This is the start of a modified add_user.sh script from http://mirakel.azapps.de/scripts/add_user.sh
ROOT_CA=~/.task/taskd/pki/ca.cert.pem

 
#read username and org from comandline
read -p "Username?`echo $'\n> '`" USER
read -p "Org?`echo $'\n> '`" ORG
#create org if nessersary
taskd add --data $TASKDDATA org $ORG >&2>/dev/null
#create user
taskd add --data $TASKDDATA user --quiet $ORG $USER 1> user.key
#find configs
taskd config --data $TASKDDATA |grep  '^server ' >server
SERVER=$(sed 's/server//g' server)
(cd ~/.task/taskd/pki && ./generate.client $ORG$USER)
cd $PWD
cp ~/.task/taskd/pki/$ORG$USER.cert.pem $USER.cert
cat ~/.task/taskd/pki/$ORG$USER.key.pem |sed -n '/-----BEGIN RSA PRIVATE KEY-----/,/-----END RSA PRIVATE KEY-----/p' >$USER.key

#if user-config already exists remove it
rm -rf $USER.taskdconfig

#Write to user-conf file
echo "username: "$USER>>$USER.taskdconfig
echo "org: "$ORG>>$USER.taskdconfig
cat user.key| sed 's/New user key:/user key:/g'>>$USER.taskdconfig
echo "server: "`cat server| sed 's/^server//g'|sed 's/^[ \t]*//'`>>$USER.taskdconfig
echo "Client.cert:">>$USER.taskdconfig
cat $USER.cert>>$USER.taskdconfig
echo "Client.key:">>$USER.taskdconfig
cat $USER.key>>$USER.taskdconfig
echo "ca.cert:">>$USER.taskdconfig
cat $ROOT_CA>>$USER.taskdconfig

USERKEY=$(sed 's/New user key: //g' user.key)

#remove temp-files
rm -rf user.key server $USER.cert
rm -rf user.key server $USER.key

mv $USER.taskdconfig ~/$USER.taskdconfig


#####################################
cp ~/.task/taskd/pki/$ORG$USER.cert.pem ~/.task
cp ~/.task/taskd/pki/$ORG$USER.key.pem ~/.task
cp ~/.task/taskd/pki/ca.cert.pem ~/.task



task config taskd.certificate ~/.task/$ORG$USER.cert.pem
task config taskd.key         ~/.task/$ORG$USER.key.pem
task config taskd.credentials $ORG/$USER/$USERKEY
task config taskd.server      $SERVER
task config taskd.ca ~/.task/ca.cert.pem

taskdctl start

task sync initialize




echo "I have placed your taskdconfig file in your home directory. Copy it to your device in order to enable sync."

#Note: I was able to sync from another computer to this server
#		after reboot, prior to logging in, though I was unable to 
#		ssh'd in and was able to sync again.
#		logged out of ssh and I was able to successfully sync
#		I added "export TASKDDATA=/home/jlmarks/.task/server_data" 
#		to the end of ~/bashrc and "taskdctl start" to the end of ~/.profile

#I should experiment with setting the TASKDDATA to /etc/task_server (or a root folder, anyway)
#and appending the export and taskctl start to /etc/profile
