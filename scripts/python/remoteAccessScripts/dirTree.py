
#this script will mount a remote file system using fuse and then generate a 
#directory tree using os.walk

#TODO: for some reason the files that are on the top level all have a double slash
#      I know that it is due to the line: 
#          k.write('{}{}/{}'.format(subindent,root.replace(startpath, 'http://jlmarks.org/'),f)+'\n')
#      but it seems like ALL lines should have a double slash after the .org. 
#      I will have to consult with someone about that. 

#TODO: format the results into a nice folding HTML page, either accordian style,
#      or using <details><summary></summary></details> (This does not seem to 
#      render well in Chrome, though.

#   sshfs jeremiahmarks@jlmarks.org:/home/content/06/6816406/html/ /home/jlmarks/remote/

import pw
import os

host=pw.hn
username=pw.un
remote_folder=pw.rf
local_folder=pw.lf
output=pw.fi


connectionString='sshfs '+username+'@'+host+':'+remote_folder+' '+local_folder




def list_files(startpath):
    """
    List files is the work horse of the dirTree application. it connects to my
    my hosting account by fusing the remote directory to my local file system. 
    It then crawls the file system and creates a txt file with the contents of
    the file system. 
    
    It is similar to a site-map creating spider, but it the pages do not need to
    be linked to anywhere since it can crawl the entire server via ssh.
    """
    os.system(connectionString) #This creates the actual connection. 
    k=open(output, 'w') #This opens the file for adding contents of the directory
    for root, dirs, files in os.walk(startpath):
        #The next line replaces the part of the path that takes the user to the 
        #folder, and then counts the slashes to determine how deep to indent
        #the results.
        level = root.replace(startpath, '').count(os.sep)
        #This creates four spaces for each level found above.
        indent = ' ' * 4 * (level)
        #the k.write line basically replaces the brackets with the results from 
        #first the indent and then by replacing the path to the folder with the 
        #first part of my domain.
        k.write('{}{}'.format(indent,root.replace(startpath, 'http://jlmarks.org/')+'\n'))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            k.write('{}{}/{}'.format(subindent,root.replace(startpath, 'http://jlmarks.org/'),f)+'\n')
    k.close()
    
print""" Suggested use:\n\tdirTree.list_files(dirTree.local_folder) """
