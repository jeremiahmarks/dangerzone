
#This script will connect to a remote server and then crawl that site
#in order to generate a comprehensive site map of what is on the server. 

import sftptoserver

#ssh=sftptoserver.getSSH()


print 'ssh got'




def printAll(tupleOfChannelFiles):
  for eachFile in tupleOfChannelFiles:
    try:
      print(eachFile.readlines())
      print"============================"
    except IOError:
      print "That didn't work"







#results=ssh.exec_command('ls -l')

print 'results got'
#clearAll(results)
