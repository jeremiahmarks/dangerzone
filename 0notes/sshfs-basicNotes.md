to mount a directory with sshfs:
	sshfs remote: /path/to/mountpoint
////Note: the remote directory needs to end with the colon (or probably a path to a folder)
////	  this includes if you are mounting a remote you have set up in .ssh/config

to unmount:
	fusermount -u /path/to/mountpoint