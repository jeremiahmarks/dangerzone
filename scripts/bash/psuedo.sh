#!/usr/bin/env bash
#basically breaking it into truth tables 
# let a be "cmake is installed"
# let b be "cmake is the right version"
# let c be "cmake28 is installed"
# let d be "cmake name is cmake"
# let e be "cmake28 must be installed"
###################################
#A# 0 # 0 # 0 # 0 # 1 # 1 # 1 # 1##
#B#DC #DC #DC #DC # 0 # 0 # 1 # 1##
#C# 0 # 1 # 0 # 1 # 0 # 1 # 0 # 1##
###################################
#D# 0 # 0 # 0 # 0 # 0 # 0 # 1 # 1##
#E# 1 # 0 # 1 # 0 # 1 # 0 # 0 # 0##
###################################
#then if A and B then D
#	  if not C, E
NEEDED=8
CMAKEVER=$(yum info cmake | awk '/Version/ { print substr($3,2,3) }')
if [[rpm -qa | grep -qw cmake]] && [[ $CMAKEVER -ge $NEEDED ]];
then
	CM=cmake
else
	CM=cmake28
	
	if ![[rpm -qa | grep cmake28]];
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

# #not sure how I messed it up last time, lets try it again
# if cmake==installed{
# 	if cmakeVersion==right{
# 		#case cmake is installed and is right version
# 		cmakename=cmake
# 		cm28needtoinstall=false
# 	}elif cm28==installed{
# 		cmakename=cmake28
# 		cm28needtoinstall=false
# 	}else{
# 		cmakename=cmake28
# 		cm28needtoinstall=true
# 	}

# 		#statements
# 		#statements
# }



#######!/usr/bin/env bash
######
####### if cmake is installed
####### 	if version < 2.8
####### 		program to run=cmake28
####### 		if cmake28 installed
####### 			pass
####### 		else
####### 			install cmake28
####### 	else
####### 		program to run =cmake
####### else
####### 	program to run=cmake
####### 	install cmake28




####### NEEDED=8
####### if rpm -qa | grep -qw cmake 
####### then
####### 	CMAKEVER=$(yum info cmake | awk '/Version/ { print substr($3,2,3) }')
####### 	if [ $CMAKEVER -lt $NEEDED ]
####### 	then
####### 		CM=cmake28
####### 		if rpm -qa | grep -qw cmake
####### 		then
####### 			echo "both cmake and cmake28 installed"
####### 		else
####### 			mkdir ~/cmaketemp
####### 			cd ~/cmaketemp
######
####### 			wget http://www.cmake.org/files/v2.8/cmake-2.8.12.2.tar.gz
####### 			tar -zxf cmake-2.8.12.2.tar.gz 
######
####### 			cd cmake-2.8.12.2
####### 			./configure 
####### 			gmake 
####### 			sudo gmake install
####### 		fi
####### 	else
####### 		CM=cmake
####### 	fi
####### else
####### 	CM=cmake
######
####### 	mkdir ~/cmaketemp
####### 	cd ~/cmaketemp
######
####### 	wget http://www.cmake.org/files/v2.8/cmake-2.8.12.2.tar.gz
####### 	tar -zxf cmake-2.8.12.2.tar.gz 
######
####### 	cd cmake-2.8.12.2
####### 	./configure 
####### 	gmake 
####### 	sudo gmake install
####### fi
