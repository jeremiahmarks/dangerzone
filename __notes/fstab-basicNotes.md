to add a sshfs volume add this line:

sshfs#jlmarks@192.168.1.108:/home/jlmarks /home/jlmarks/brilliantjenny  fuse defaults,idmap=user,_netdev,allow_other,identityfile=/home/jlmarks/.ssh/id_rsa 	0 	0

the line should end with a newline

to mount ntfs on centos:
	if epel is enabled : yum install ntfs-3g



on BJ:
	the silver drive is currently sdc1
	so to mount in folder /media/silver:
		# mount /dev/sdc1 /media/silver
