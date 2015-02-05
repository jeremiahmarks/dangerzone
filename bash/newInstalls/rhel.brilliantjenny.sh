
################################################################################
################################################################################
##
##Gotta get that epel

wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
sudo rpm -ivh epel-release-6-8.noarch.rpm

##
##
################################################################################
################################################################################

sudo yum install httpd
sudo yum install mysql-server

sudo service httpd start
sudo service mysqld start

sudo /usr/bin/mysql_secure_installation
sudo yum install php php-mysql

sudo chkconfig httpd on
sudo chkconfig mysqld on


################################################################################
################################################################################
##For whatever reason centos 6 does not include 
##python 2.7 nor python 3. These instructions come from
##http://toomuchdata.com/2014/02/16/how-to-install-python-on-centos/


sudo yum groupinstall "Development tools"
sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel

# Python 2.7.6:
wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz
tar xf Python-2.7.6.tar.xz
cd Python-2.7.6
./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make && make altinstall

# Python 3.3.4:
wget http://python.org/ftp/python/3.3.4/Python-3.3.4.tar.xz
tar xf Python-3.3.4.tar.xz
cd Python-3.3.4
./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make && make altinstall
##
##After running the commands above your newly installed Python interpreter will be available as /usr/local/bin/python2.7 or /usr/local/bin/python3.3
################################################################################
################################################################################
################################################################################
################################################################################

##same site: setting up setup tools for each python version

# First get the setup script for Setuptools:
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py

# Then install it for Python 2.7 and/or Python 3.3:
python2.7 ez_setup.py
python3.3 ez_setup.py

# Now install pip using the newly installed setuptools:
easy_install-2.7 pip
easy_install-3.3 pip

# With pip installed you can now do things like this:
pip2.7 install [packagename]
pip2.7 install --upgrade [packagename]
pip2.7 uninstall [packagename]


################################################################################
################################################################################
################################################################################
################################################################################

##
##Same site: setting up virtualenvs for 2.7

####   # Install virtualenv for Python 2.7 and create a sandbox called my27project:
####   pip2.7 install virtualenv
####   virtualenv-2.7 my27project
####   
####   # Use the built-in pyvenv program in Python 3.3 to create a sandbox called my33project:
####   pyvenv-3.3 my33project
####   
####   # Check the system Python interpreter version:
####   python --version
####   # This will show Python 2.6.6
####   
####   # Activate the my27project sandbox and check the version of the default Python interpreter in it:
####   source my27project/bin/activate
####   python --version
####   # This will show Python 2.7.6
####   deactivate
####   
####   # Activate the my33project sandbox and check the version of the default Python interpreter in it:
####   source my33project/bin/activate
####   python --version
####   # This will show Python 3.3.4
####   deactivate


################################################################################
################################################################################
################################################################################
################################################################################

## application to attempt to install: shellinabox
## http://code.google.com/p/shellinabox/

################################################################################
################################################################################
################################################################################
################################################################################