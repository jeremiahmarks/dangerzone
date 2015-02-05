
# This script is to create the sftp connection to jlmarks.org
# this connection will be usable by other scripts. 

import paramiko
import pw

host=pw.hn
port = 22
username=pw.un
password=pw.pw

def getSSH():
  thisShell=paramiko.SSHClient()
  #
  #The next line is iffy if you are not sure what you are connecting to.
  #It should really only be used in an environment where you control
  #the server as well, but this is hacky and for personal use, so I am going
  #to set it to automatically trust the remote computer. 
  thisShell.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  thisShell.connect(host, username=username, password=password)
  return thisShell
  
  
