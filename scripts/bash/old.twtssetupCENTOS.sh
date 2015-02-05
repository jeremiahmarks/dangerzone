#!/usr/bin/env bash
su -c "yum update"
su -c 'yum groupinstall "Development Tools"'
su -c "yum install gnutls-devel* libuuid-devel* gnutls-utils*"

NEEDED=8
if rpm -qa | grep -qw cmake 
then
	CMAKEVER=$(yum info cmake | awk '/Version/ { print substr($3,3,1) }')
	if [ $CMAKEVER -lt $NEEDED ]
	then
		CM=cmake28
		if rpm -qa | grep cmake28
		then
			echo "both cmake and cmake28 installed"
		else
			mkdir ~/cmaketemp
			cd ~/cmaketemp

			wget http://www.cmake.org/files/v2.8/cmake-2.8.12.2.tar.gz
			tar -zxf cmake-2.8.12.2.tar.gz 

			cd cmake-2.8.12.2
			./configure 
			gmake 
			sudo gmake install
		fi
	else
		CM=cmake
	fi
else
	CM=cmake

	mkdir ~/cmaketemp
	cd ~/cmaketemp

	wget http://www.cmake.org/files/v2.8/cmake-2.8.12.2.tar.gz
	tar -zxf cmake-2.8.12.2.tar.gz 

	cd cmake-2.8.12.2
	./configure 
	gmake 
	sudo gmake install
fi


mkdir -p ~/.task
cd ~/.task
export TASKDDATA=~/.task/server_data
mkdir -p $TASKDDATA

git clone https://git.tasktools.org/scm/tm/task.git
git clone https://git.tasktools.org/scm/tm/taskd.git

cd taskd
$CM .
make
sudo make install

cd ../task
$CM .
make
sudo make install

cd ../taskd
taskd init

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
ROOT_CA=$TASKDDATA/../taskd/pki/ca.cert.pem

 
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
(cd $TASKDDATA/../taskd/pki && ./generate.client $ORG$USER)
cd $PWD
cp $TASKDDATA/../taskd/pki/$ORG$USER.cert.pem $USER.cert
cat $TASKDDATA/../taskd/pki/$ORG$USER.key.pem |sed -n '/-----BEGIN RSA PRIVATE KEY-----/,/-----END RSA PRIVATE KEY-----/p' >$USER.key

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
cp $TASKDDATA/../taskd/pki/$ORG$USER.cert.pem ~/.task
cp $TASKDDATA/../taskd/pki/$ORG$USER.key.pem ~/.task
cp $TASKDDATA/../taskd/pki/ca.cert.pem ~/.task



task config taskd.certificate ~/.task/$ORG$USER.cert.pem
task config taskd.key         ~/.task/$ORG$USER.key.pem
task config taskd.credentials $ORG/$USER/$USERKEY
task config taskd.server      $SERVER
task config taskd.ca ~/.task/ca.cert.pem

taskdctl start

task sync initialize

# su -c "iptables -A INPUT -p tcp --dport 53589 -j ACCEPT"
# su -c "/sbin/service iptables save"
# STRA="export TASKDDATA=$TASKDDATA"
# STRB="taskdctl start"

# su -c "echo $STRA >> /etc/rc.d/rc.local"
# su -c "echo $STRB >> /etc/rc.d/rc.local"


echo "I have placed your taskdconfig file in your home directory. Copy it to your device in order to enable sync."

####
##testing
###installed centos 6.4 i386 on virtual machine (Desktop?)
###copied and ran script from home folder

