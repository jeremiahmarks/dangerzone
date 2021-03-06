#!/bin/bash
TASKD=../../src/taskd
ROOT=$PWD/root
ROOT_CA=../../pki/ca.cert.pem

#read username and org from comandline
read -p "Username?`echo $'\n> '`" USER
read -p "Org?`echo $'\n> '`" ORG

#create org if nessersary
$TASKD add --data $ROOT org $ORG >&2>/dev/null

#create user
$TASKD add --data $ROOT user --quiet $ORG $USER 1> user.key

#find configs
$TASKD config --data $ROOT |grep  '^server ' >server

(cd ../../pki && ./generate.client $ORG$USER)
cd $PWD
cp ../../pki/$ORG$USER.cert.pem $USER.cert
#cat `$TASKD config --data $ROOT |grep  '^client.cert '| sed -e 's/client.cert//'`>$USER.cert
cat ../../pki/$ORG$USER.key.pem |sed -n '/-----BEGIN RSA PRIVATE KEY-----/,/-----END RSA PRIVATE KEY-----/p' >$USER.key

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

#remove temp-files
rm -rf user.key server $USER.cert
rm -rf user.key server $USER.key
#rm -f ../../pki/$ORG$USER.cert.pem


echo 
echo "You're ready!"
echo "Copy the "$USER.taskdconfig" to your device and don't forget to start the server:"
echo "./run"
