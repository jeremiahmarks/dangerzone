"""
>>> nevent=gdata.calendar.data.CalendarEventEntry()
>>> nevent.title=atom.data.Title(text="First event created!!")
>>> nevent.content=atom.data.Content(text="This is the content field")
>>> nevent.where.append(gdata.calendar.data.CalendarWhere(value='from my front room'))
>>> start_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())
>>> start_time
5: '2011-03-31T02:48:33.000Z'
>>> end_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime(time.time() + 36))
>>> end_time
6: '2011-03-31T02:50:07.000Z'
>>> nevent.when.append(gdata.calendar.data.When(start=start_time, end=end_time))
>>> new_event = apple.calClient.InsertEvent(nevent)
>>> new_event.get_html_link()
7: <atom.data.Link object at 0x0371BDD0>
>>> new_event.get_html_link().href
8: 'https://www.google.com/calendar/event?eid=YWl0aDRzanNxZWpkbDcyMHBnbTQ5dDk3M2sgamVyZW1pYWgubC5tYXJrc0Bt'

"""

# this is a program to manage and update calendars on google calendars
# this is for personal use



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

class mypycal:

	def __init__(self, email='jeremiah.l.marks@gmail.com', password='99b0ttles0fb33r'):
		"""This creates the mypycal client and logs in """

		self.calClient=gdata.calendar.client.CalendarClient(source='JeremiahsClasses v0.1')
		self.calClient.ClientLogin(email, password, self.calClient.source);
		self.CalFeed=self.calClient.GetAllCalendarsFeed();
		self.Run()

	def _PrintCalList(self):
		"""This prints the list of calendars, with their position in the list"""

		for i, calname in zip(xrange(len(self.CalFeed.entry)), self.CalFeed.entry):
			print '%s. \t\t %s' %(i, calname.title.text)

	def _CalToEdit(self):
		"""This will prompt the user to select a calender to edit"""


		self.workingCalendar=raw_input('Please enter the calendar you wish to edit')
		self.workingCalendar=int(self.workingCalendar)
		self.eVentFeed=self.calClient.GetCalendarEventFeed(uri=self.CalFeed.entry[self.workingCalendar].content.src)


	def _PrintSchedule(self):
		"""This will print all of the events and the whens of the event """

		for event in range(len(self.eVentFeed.entry)):
			for times in range(len(self.eVentFeed.entry[event].when)):
				print(self.eVentFeed.entry[event].title.text, self.eVentFeed.entry[event].when[times].start, self.eVentFeed.entry[event].when[times].end)




	def Run(self):
		"""This is the testing grounds for the object"""

		self._PrintCalList()
		self._CalToEdit()
		self._PrintSchedule()
