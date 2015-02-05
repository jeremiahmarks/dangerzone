#intent: create a script that will create an HTML page and post it to my website 
#via python and html. The argument it will accept is the text for the newest post. 

# server.org/SERVERDIRECTORY/yyyyMonDayhhmmss.html

SERVER='ftp.yourhost.org'
USERNAME='yourFTPusername'
PASSWORD='yourFTPpassword'
SERVERDIRECTORY='theDirectoryOnTheServer' #this currently must be created already, but
#                                          '/' should be acceptable as well.


def getContent():
  import argparse
  parser=argparse.ArgumentParser(description="Retrieves the content and returns it to the main running process.")
  parser.add_argument('--c',dest='c', help="This is where the content would go")
  args=parser.parse_args()
  return args.c

def getTime():
  import time
  currentTime=time.localtime()
  currentTime=str(currentTime.tm_year)+'_'+str(currentTime.tm_mon)+'_'+str(currentTime.tm_mday)+'_'+str(currentTime.tm_hour)+'_'+str(currentTime.tm_min)+'_'+str(currentTime.tm_sec)
  return currentTime

def htmlMaker(content, time):
  from string import Template
  htmlTemplate=Template('<html>\n<head>\n<title>$thetime</title>\n</head>\n<body>\n$thecontent\n</body>\n</html>')
  htmlTemplate=htmlTemplate.substitute(thetime=time, thecontent=content)
  htmlFile=file(time+'.html', 'w')
  htmlFile.write(htmlTemplate)
  htmlFile.close()
  return htmlFile
  

  

def uploadPage(newFile):
  from ftplib import FTP
  ftp=FTP(SERVER)
  ftp.login(USERNAME, PASSWORD)
  ftp.cwd(SERVERDIRECTORY)
  newFile=open(newFile.name, 'rb')
  ftp.storbinary('STOR '+newFile.name, newFile)
  newFile.close()
  ftp.close()
  print "it should be live at "+SERVER+'/'+SERVERDIRECTORY+'/'+newFile.name
  

  
if __name__ == '__main__':
  content=getContent()
  time=getTime()
  newFile=htmlMaker(content, time)
  uploadPage(newFile)  
