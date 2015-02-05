
#this script will mount a remote file system using fuse and then generate a 
#directory tree using os.walk
import pw
import os

host=pw.hn
username=pw.un
#folder=pw.fo
remote_folder=pw.rf
local_folder=pw.lf
output=pw.fi


connectionString='sshfs '+username+'@'+host+':'+remote_folder+' '+local_folder

#os.system(connectionString)


def list_files(startpath):
    os.system(connectionString)
    k=open(output, 'w')
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        k.write('{}{}'.format(indent,root.replace(startpath, 'http://jlmarks.org/')+'\n'))
        #print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            k.write('{}{}/{}'.format(subindent,root.replace(startpath, 'http://jlmarks.org/'),f)+'\n')
            #print('{}{}'.format(subindent, f))
    k.close()
    
print""" Suggested use:\n\tdirTree.list_files(dirTree.local_folder) """
