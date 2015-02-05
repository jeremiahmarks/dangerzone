# @Author: Jeremiah Marks
# @Date:   2014-03-18 16:44:41
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2014-03-18 16:58:45

to mount ntfs on centos:
	if epel is enabled : yum install ntfs-3g



on BJ:
	the silver drive is currently sdc1
	so to mount in folder /media/silver:
		# mount /dev/sdc1 /media/silver
