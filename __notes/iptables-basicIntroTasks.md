references:
	http://www.cyberciti.biz/faq/rhel-fedorta-linux-iptables-firewall-configuration-tutorial/
	http://wiki.centos.org/HowTos/Network/IPTables

display default rules:
	iptables --line-numbers -n -L

There are total 4 chains:

    INPUT - The default chain is used for packets addressed to the system. Use this to open or close incoming ports (such as 80,25, and 110 etc) and ip addresses / subnet (such as 202.54.1.20/29).
    OUTPUT - The default chain is used when packets are generating from the system. Use this open or close outgoing ports and ip addresses / subnets.
    FORWARD - The default chains is used when packets send through another interface. Usually used when you setup Linux as router. For example, eth0 connected to ADSL/Cable modem and eth1 is connected to local LAN. Use FORWARD chain to send and receive traffic from LAN to the Internet.
    RH-Firewall-1-INPUT - This is a user-defined custom chain. It is used by the INPUT, OUTPUT and FORWARD chains.

to edit iptables:
	vi /etc/sysconfig/iptables

to open a port:
	-A RH-Firewall-1-INPUT -m tcp -p tcp --dport 80 -j ACCEPT 
	#opens port 80 to tcp traffic

allow traffic from only addresses on the network
	-A RH-Firewall-1-INPUT -s 192.168.1.0/24 -m state --state NEW -p tcp --dport 22 -j ACCEPT

##unsure why this made it, but the tutorial mentions it before restarting the firewall:
Save and close the file. Edit /etc/sysconfig/iptables-config, enter:
	vi /etc/sysconfig/iptables-config
Make sure ftp module is loaded with the space-separated list of modules:
	IPTABLES_MODULES="ip_conntrack_ftp"

Then restart the firewall:
	service iptables restart