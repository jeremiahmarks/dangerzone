#!/usr/bin/env bash
#sudo yum update
#sudo yum groupinstall "Development Tools"
#sudo yum install gnutls-devel* libuuid-devel* gnutls-utils*

NEEDED=8
CMAKEVER=$(yum info cmake | awk '/Version/ { print substr($3,3,1) }')
if [ "rpm -qa | grep -qw cmake" ]  && [[ $CMAKEVER -ge $NEEDED ]];
then
	CM=cmake
else
	CM=cmake28
	
	if [! "rpm -qa | grep cmake28"];
	then
		mkdir ~/cmaketemp
		cd ~/cmaketemp
		wget http://www.cmake.org/files/v2.8/cmake-2.8.12.2.tar.gz
		tar -zxf cmake-2.8.12.2.tar.gz 
		cd cmake-2.8.12.2
		./configure 
		gmake 
		sudo gmake install
	fi
fi

