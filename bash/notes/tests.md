<!-- File Name: tests.md  -->
<!-- Author: Jeremiah Marks -->
<!-- Date:   2014-03-27 22:45:11 -->
<!-- Last Modified by:   Jeremiah Marks -->
<!-- Last Modified time: 2014-03-27 22:45:11 -->
<!-- Email: jeremiah@jlmarks.org-->

#[if/then](#ifthen)
- An **if/then** tests whether the exit status of a list of commands is **0** If 
it is it then excutes other commands. 

```bash
let "1<2" 		#returns 0 (as "1<2" expands to "1")
(( 0 && 1 )) 	#returns 1 (as "0 && 1" expands to "0")
```

- An if can test any command, not just conditions enclosed within brackets

```bash

if cmp a b &> /dev/null  # Suppress output.
then echo "Files a and b are identical."
else echo "Files a and b differ."
fi

if grep -q Bash file
then echo "File contains at least one occurrence of Bash."
fi

if COMMAND_WHOSE_EXIT_STATUS_IS_0_UNLESS_ERROR_OCCURRED
then echo "Command succeeded."
else echo "Command failed."
fi
```

- An if/then construct can contain nested comparisons and tests. 


```bash
if echo "Next *if* is part of the comparison for the first *if*."

  if [[ $comparison = "integer" ]]
    then (( a < b ))
  else
    [[ $a < $b ]]
  fi

then
  echo '$a is less than $b'
fi
```

***

#[\[\[](#extendedtest)

- The [[ ]] construct is the more versatile Bash version of [ ]. 
This is the *extended test command*, adopted from ksh88.

***
#[(())](#arithmeticTesting)

- If the expression within the "(())" construct evaluates as zero, it returns a 1, or "false"
- If the expression within the "(())" construct evaluates as anything other than zero, it returns a 0 or "true"

***
#File Test Operators

Returns true if...

-e 			file exists

-f 			file is a regular file (not a directory or device file)

-s 			file is not zero size

-d 			file is a directory

-b 			file is a block device (floppy, cdrom, etc.) 

-c 			file is a character device (keyboard, modem, sound card, etc.)

-p 			file is a pipe

-h 			file is a symbolic link

-L 			file is a symbolic link

-S 			file is a socket

-t 			file (descriptor) is associated with a terminal device 

This test option may be used to check whether the stdin ([ -t 0 ]) or stdout ([ -t 1 ]) in a given script is a terminal.

-r 			file has read permission (for the user running the test)

-w 			file has write permission (for the user running the test)

-x 			file has execute permission (for the user running the test)

-g 			set-group-id (sgid) flag set on file or directory
			
If a directory has the sgid flag set, then a file created within that directory belongs to the group that owns the directory, not necessarily to the group of the user who created the file. This may be useful for a directory shared by a workgroup.

-u 			set-user-id (suid) flag set on file
			
A binary owned by root with set-user-id flag set runs with root privileges, even when an ordinary user invokes it. [1] This is useful for executables (such as pppd and cdrecord) that need to access system hardware. Lacking the suid flag, these binaries could not be invoked by a non-root user.
     	    
     	      		-rwsr-xr-t    1 root       178236 Oct  2  2000 /usr/sbin/pppd
    		
A file with the suid flag set shows an s in its permissions.

-k 			sticky bit set
    		
Commonly known as the "sticky bit", the save-text-mode flag is a special type of file permission. If a file has this flag set, that file will be kept in cache memory, for quicker access. [2] If set on a directory, it restricts write permission. Setting the sticky bit adds a t to the permissions on the file or directory listing.
     	    
     	      		drwxrwxrwt    7 root         1024 May 19 21:26 tmp/
    		
If a user does not own a directory that has the sticky bit set, but has write permission in that directory, he can only delete files in it that he owns. This keeps users from inadvertently overwriting or deleting each other's files in a publicly accessible directory, such as /tmp.

-O 			you are owner of file

-G 			group-id of file same as yours

-N 			file modified since it was last read

f1 -nt f2 	file f1 is newer than f2

f1 -ot f 	file f1 is older than f2

f1 -ef f2 	files f1 and f2 are hard links to the same file

! 			"not" -- reverses the sense of the tests above (returns true if condition absent).