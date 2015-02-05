to create a private and public on local computer:
    ssh-keygen and follow prompts

then, from the local computer do
    ssh-copy-id -i ~/.ssh/id_rsa.pub othercomputer
        (Where other computer is the network address of the other computer)

=========================
==
==  ~/.ssh/config
==
=========================

#I have a computer in my living room that I call "lrm" (for living room machine) and I ssh to it a lot. 
#One time saving trick that I like is adding it to my config file

Host lrm
     HostName 192.168.1.135

# by doing this I can now ssh to it from the command line with only "$ ssh lrm"
