try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom
import getopt
import sys
import string
import time

myemail='jeremiah@themarkshousehold.com'
mypassword='99bottlesofb33r!'

class mycalawes:#short for MyCalendar of Awesomesauce
	
	def __init__(self):
		myemail=''
		mypassword=''

		self.client=gdata.calendar.client.CalendarClient(source="Jeremiahs twisted brain")
		self.client.ClientLogin(myemail, mypassword, self.client.source);
	
""" some stuff from my playing in dreampie today
thor='thor@themarkshousehold.com'
thorpass='applepie'
apple.ClientLogin(thor,thorpass,source="me")

openfile=open('/Users/Jeremiah/Documents/mypy/tester.jlm', 'w')
openfile.write('Something Awesome!')
openfile.close()


openfile=open('/Users/Jeremiah/Documents/mypy/tester.txt', 'wb')
openfile.tell()



"""
