#!/usr/local/bin/python2.7


import xmlrpclib
import time
import random

defaultStart='20000101T00:00:00'
defaultEnd='29991231T23:59:59'


class ISTag:
	def __init__(self, tagid, tagname, categoryid):
		self.tagid=tagid
		self.name=tagname
		self.categoryid=categoryid

class BasicContact(object):
	def __init__(self, contactID, fname=None, lname=None, emailAddress=None ):
		self.cid = contactID
		if (not(fname) or fname==None):
			self.fname="No fName"
		else:
			self.fname=u''.join(fname).encode('utf-8').strip()
		if (not(lname) or lname==None):
			self.lname="No lName"
		else:
			self.lname=u''.join(lname).encode('utf-8').strip()
		if (not(emailAddress) or emailAddress==None):
			self.email="no Email Listed"
		else:
			self.email=u''.join(emailAddress).encode('utf-8').strip()

class TagAppliedRecord(BasicContact):
	def __init__(self, contactID, contactFName, contactLName, contactEmail, tagName, tagID,tagtime):
		self.contactID=contactID
		super(TagAppliedRecord, self).__init__(contactID, contactFName, contactLName, contactEmail)
		self.tagname=tagName
		self.tagid=tagID
		self.whenapplied=tagtime

class ContactWithCreditCard(BasicContact):
	def __init__(self, CardID, Last4, contactID, fname, lname, emailAddress):
		super(ContactWithCreditCard, self).__init__(contactID, fname, lname, emailAddress)
		self.cardid=CardID
		self.last4=Last4

class ISServer:
	def __init__(self, infusionsoftapp, infusionsoftAPIKey):
		self.infusionsoftapp=infusionsoftapp
		self.infusionsoftAPIKey=infusionsoftAPIKey
		self.appurl = "https://" + self.infusionsoftapp + ".infusionsoft.com:443/api/xmlrpc"
		self.connection = xmlrpclib.ServerProxy(self.appurl)

	def getTagCats(self):
		self.tagcats={}
		p=0
		while True:
			listOfDicts=self.connection.DataService.query(self.infusionsoftAPIKey, "ContactGroupCategory", 1000, p, {}, ['Id', 'CategoryName'], 'CategoryName',True)
			for eachCat in listOfDicts:
				self.tagcats[eachCat['Id']] = eachCat['CategoryName']
			if not(len(listOfDicts)==1000):
				break
			p=p+1

	def getAllTags(self):
		self.tags={}
		p=0
		while True:
			listOfDicts=self.connection.DataService.query(self.infusionsoftAPIKey, "ContactGroup", 1000,p,{},['Id',"GroupCategoryId","GroupName"],"GroupName", True )
			for eachtag in listOfDicts:
				self.tags[eachtag['Id']]=(ISTag(eachtag['Id'], eachtag['GroupName'], eachtag['GroupCategoryId']))
			if not(len(listOfDicts)==1000):
				break
			p=p+1

	def prep(self):
		self.getTagCats()
		self.getAllTags()

	def getContactsWithTag(self, startdate="19000101T00:00:00", enddate="30001231T23:59:59", tagID=303):
		records=[]
		sdate = time.strptime(startdate, '%Y%m%dT%H:%M:%S')
		edate = time.strptime(enddate, '%Y%m%dT%H:%M:%S')
		p=0
		while True:
			listOfDicts=self.connection.DataService.query(self.infusionsoftAPIKey, 'ContactGroupAssign', 1000,p,{'GroupId':tagID},['Contact.Email', 'Contact.FirstName', 'Contact.LastName', 'Contact.Id', 'DateCreated'],"Contact.Id",True)
			for eachApplication in listOfDicts:
				datetimeapplied = time.strptime(eachApplication['DateCreated'].value, '%Y%m%dT%H:%M:%S')
				if ((datetimeapplied>=sdate) and (datetimeapplied<=edate)):
					interestingData = ["Contact.FirstName", "Contact.LastName", 'Contact.Email']
					for eachbit in interestingData:
						if not eachApplication.has_key(eachbit):
							eachApplication[eachbit]=None
					records.append(TagAppliedRecord(eachApplication['Contact.Id'],eachApplication['Contact.FirstName'],eachApplication['Contact.LastName'],eachApplication['Contact.Email'], self.tags[tagID].name, tagID, datetimeapplied))
			if not(len(listOfDicts)==1000):
				break
			p=p+1
		return records

	def getContactIDWithTag(self, tagID):
		records = []
		p=0
		while True:
			listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'ContactGroupAssign', 1000,p,{'GroupId':tagID}, ['Contact.Id', 'Contact.FirstName', 'Contact.LastName', 'Contact.Email' ], 'Contact.Id', True)
			for eachContact in listOfDicts:
				interestingData = ["Contact.FirstName", "Contact.LastName", 'Contact.Email']
				for eachbit in interestingData:
					if not eachContact.has_key(eachbit):
						eachContact[eachbit]=None
				records.append(BasicContact(eachContact['Contact.Id'], fname=eachContact['Contact.FirstName'], lname=eachContact['Contact.LastName'], emailAddress=eachContact['Contact.Email']))
			if not(len(listOfDicts)==1000):
				break
			p+=1
		return records

	def getAllContacts(self):
		records = []
		p=0
		while True:
			listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'Contact', 1000,p,{},['Id', 'FirstName', 'LastName', 'Email'], 'Id', True)
			for eachContact in listOfDicts:
				interestingData=['FirstName',"LastName",'Email']
				for eachbit in interestingData:
					if not eachContact.has_key(eachbit):
						eachContact[eachbit]=None
				records.append(BasicContact(eachContact['Id'], fname=eachContact['FirstName'], lname=eachContact['LastName'], emailAddress=eachContact['Email']))
			if not(len(listOfDicts)==1000):
				break
			p+=1
		return records

	def verifyConnection(self):
		try:
			listOfDicts=self.connection.DataService.query(self.infusionsoftAPIKey, "User", 1000, 0,{},["Email"],"Email",True)
			return True
		except:
			return False

	def getCount(self, tableName, query):
		return self.connection.DataService.count(self.infusionsoftAPIKey, tableName, query)

	def createNewTag(self, newTagName):
		return self.connection.DataService.add(self.infusionsoftAPIKey, 'ContactGroup', {'GroupName':newTagName})

	def addTagToContact(self, contactID, tagID):
		self.connection.ContactService.addToGroup(self.infusionsoftAPIKey, contactID, tagID)

	def deleteTag(self, tagID):
		self.connection.DataService.delete(self.infusionsoftAPIKey, 'ContactGroup', tagID)

	def placeOrder(self, contactID, creditCardId, payPlanId, productIds, subscriptionPlanIds, processSpecials, promoCodes, leadAffiliateId, saleAffiliateId):
		return self.connection.OrderService.placeOrder(self.infusionsoftAPIKey, int(contactID), int(creditCardId), int(payPlanId), productIds, subscriptionPlanIds, processSpecials, promoCodes, leadAffiliateId, saleAffiliateId)

	def getContactsWithCards(self):
		records=[]
		p=0
		while True:
			listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'CreditCard', 1000,p,{},['Id', 'ContactId', 'Email','FirstName', 'LastName', 'Last4'], 'Id', True)
			for each in listOfDicts:
				interestingData=["Id", 'ContactId', 'Email','FirstName', 'LastName', 'Last4']
				if not(each.has_key('Email') or each.has_key('FirstName') or each.has_key('LastName')):
					pass
				else:
					for eachbit in interestingData:
						if not each.has_key(eachbit):
							each[eachbit]=None
					records.append(ContactWithCreditCard(each['Id'], each['Last4'],each['ContactId'], each['FirstName'], each['LastName'], each['Email'] ))
			if not(len(listOfDicts)==1000):
				break
			p+=1
		return records

	def getAllProducts(self):
		records=[]
		p=0
		while True:
			listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'Product', 1000, p, {}, ['Id', 'ProductName', 'ProductPrice', 'ShippingTime', 'IsPackage', 'HideInStore'], 'Id', True)
			for each in listOfDicts:
				interestingData=['ProductName', 'ProductPrice', 'ShippingTime', 'IsPackage', 'HideInStore']
				for eachbit in interestingData:
					if not each.has_key(eachbit):
						each[eachbit]=None
				records.append((each['Id'], each['ProductName'], each['ProductPrice'], each['ShippingTime'], each['IsPackage'], each['HideInStore']))
			if not(len(listOfDicts)==1000):
				break
			p+=1
		return records

def prehead():
	pagehtml="""Content-type: text/html\n\n\n"""
	return pagehtml

def htmlHead():
	pagehtml = """
	<html>
		<head>
			<link rel="stylesheet" href="//code.jquery.com/ui/1.11.2/themes/smoothness/jquery-ui.css">
			<script src="//code.jquery.com/jquery-1.10.2.js"></script>
			<script src="//code.jquery.com/ui/1.11.2/jquery-ui.js"></script>
			<script>
				$(function() {
					$( ".datepicker" ).datepicker();
				});
			</script>
			<style>
				@import url(http://fonts.googleapis.com/css?family=Open+Sans:400,700);
				* {
				  padding:0;
				  margin:0;
				  position:relative;
				  box-sizing:border-box;
				}
				body {
				  font-size:16px;
				  font-family: 'Open Sans', sans-serif;
				}
				h1,h2,h3 {
				  color:#ff0000;
				  text-align:center;
				}
				.errormessage{
					color: red;
					text-align: center;
					font-size: 64px;
				}
			</style>
			<meta http-equiv="Content-type" content="text/html;" />
			<title> Crackbrain: One off functions for Infusionsoft</title>
			<meta name="description" Content="One off searches and functions that are not a part of Infusionsoft." />
		</head>
		<body>
	"""
	return pagehtml

def menu():
	pagehtml="""
	<div>
		<form method="POST">
			<input type="submit" name="logout" value="Logout">
			<input type="submit" name="btar" value="Better tag application report">
			<input type="submit" name="rancon" value="Pick Random Contacts">
			<input type="submit" name="alltags" value="All tags">
			<input type="submit" name="ordertest" value="Test Order Creation" />
		</form>
	</div>
	"""
	return pagehtml

def selectionScreen(dictOfTags):
	pagehtml = """
			<div class="btarExplanation">
				<p>
					This report will show all applications of the chosen tag to contacts within the given range.
					<br /> <br />
					If a tag has been removed its record has been removed from it as well.  This means that the
					report will only show records that still have the tag if it was applied within the date range.
					This also means that if a contact has had the same tag applied more than once, only the most
					recent application will populate in this report.
					<br /><br />
					After you get the results of this report you can create a new tag to apply to the contacts who meet
					the search criteria so that you can find them in the application.
				</p>
			</div>
			<form method="POST" action="">
				<div class="btarReportSettings">
					<div class="datepickers">
						<table>
							<tr>
								<td width="310px">
									<input type="hidden" name="runbtar" value="run">
									<label for="startdate" >Start Date:</label>
									<input type="text" class="datepicker text" name="startdate" style="width:300px;">
								</td>
								<td width="310px">
									<label for="enddate">End Date:</label>
									<input type="text" class="datepicker text" name="enddate" style="width:300px;">
								</td>
							</tr>
						</table>
					</div>
					<div>
						<label for="tags">Tag of interest: </label>
						<select  name="tags">
							<option value="" disabled selected>Select a tag</option>
	"""
	tagids=dictOfTags.keys()
	taglist=[]
	for eachid in tagids:
		taglist.append((eachid,dictOfTags[eachid].name))
	taglist.sort(key=lambda val:val[1])
	for eachid in taglist:
		pagehtml = pagehtml + """
					<option value="%s">%s</option>
		""" %(str(eachid[0]), eachid[1])
	pagehtml = pagehtml + """
						</select>

					</div>
				</div>
				<input type="Submit" value="Search">
			</form>
	"""
	return pagehtml

def processInfo(postdata,server):
	contacts=[]
	taglist=[]
	alltags=[]
	server.prep()
	tagids=server.tags.keys()
	for eachid in tagids:
		alltags.append((eachid, server.tags[eachid].name))
	alltags.sort(key=lambda val:val[1])
	if postdata.has_key('startdate'):
		smonth, sday, syear=postdata['startdate'].value.split('/')
		smonth = "%02d" %int(smonth)
		sday = "%02d" %int(sday)
		sstring=syear+smonth+sday+"T00:00:00"
	else:
		sstring="19000101T00:00:00"
	if postdata.has_key('enddate'):
		emonth, eday, eyear = postdata['enddate'].value.split('/')
		emonth = "%02d" %int(emonth)
		eday = "%02d" %int(eday)
		estring=eyear+emonth+eday+"T23:59:59"
	else:
		estring="30001231T23:59:59"
	if (type(postdata['tags'])==type(())):
		for eachtag in postdata['tags']:
			contacts.append(server.getContactsWithTag(sstring,estring,int(eachtag['tags'].value)))
			taglist.append(server.tags[int(eachtag['tags'].value)].name)
	else:
		contacts.append(server.getContactsWithTag(sstring,estring,int(postdata['tags'].value)))
		taglist.append(server.tags[int(postdata['tags'].value)].name)
	contacts[0].sort(key=lambda val:val.whenapplied)
	tagstring=''
	for eachtagname in taglist:
		tagstring = tagstring + eachtagname
	newtagstring=tagstring + """ applied from """ + sstring + " to " + estring
	pagehtml= """
			<form method="POST" action="">
				<div>
					<table>
						<tr>
							<td width = "500">
								<input type="radio" name="neworold" value="old" checked>
								<label for="tags">
									Apply existing tag to all contacts:
								</label>

								<select name="tags" style="width: 300px;">
									<option value="" disabled selected>Select a tag</option>
	"""
	for eachid in alltags:
		pagehtml = pagehtml + """
									<option value="%s">%s</option>
		""" %(str(eachid[0]), eachid[1])
	pagehtml += """
								</select>

							</td>
							<td width = "500">
								<input type="radio" name="neworold" value="new">
								<label>Create and apply this tag</label>
								<input type='text' name='tagtoapply' class="text">

							</td>
						</tr>
					</table>
					<input type="submit" name="createandapplytag" value="Apply tag">
				</div>
				<table>
					<tr>
						<td width="50">Id</td>
						<td width="200">Name</td>
						<td width="200">Email</td>
						<td width="200">Tag</td>
						<td width="200">Applied</td>
					</tr>
	"""
	for eachsearch in contacts:
		for eachrecord in eachsearch:
			recordURL="https://" + server.infusionsoftapp + ".infusionsoft.com/Contact/manageContact.jsp?view=edit&ID=" + str(eachrecord.contactID)
			pagehtml = pagehtml + """
					<tr>
						<td>
							<input type="text" name="update%s" value="%s" readonly>
						</td>
						<td><a href="%s">%s</a></td>
						<td>%s</td>
						<td>%s</td>
						<td>%s</td>
					</tr>
			""" %(str(eachrecord.contactID), str(eachrecord.contactID), recordURL, eachrecord.fname + " " + eachrecord.lname, eachrecord.email, eachrecord.tagname, time.strftime('%d%b%Y %H:%M:%S', eachrecord.whenapplied))
	pagehtml = pagehtml + """
				</table>
			</form>
	"""
	return pagehtml

def gatherInfo():
	pagehtml= """
				<div class="p1">
					<h3>Welcome to Crackbra.in.</h3>
					<p>
						This is my personal collection of Infusionsoft functions that provide some added functionality to the core application.
						These functions are in no way affiliated with Infusionsoft nor any of its affiliates, they are just a set of functions
						that I expect that users will find useful.
						<br />
						These functions are provided with absolutely no warranty, guarantee, or any avenue of real meaningful support.  As of the
						time of this writing there are no functions that remove data from your Infusionsoft application, nor are there any that store data anywhere except in a cookie on your computer.  I use this so that I do not have to pass the app name and API key through hidden fields the whole time you are browsing. If you log out it will delete the cookie.
						<br />
						You can examine the most recent copy of the source code (that I have been bothered to upload) <a href="https://github.com/jeremiahmarks/betterTagApplicationReport">on its github page</a>, so you can self host this if you so wish.  This is also available so that you can improve it, please do fork the daylights out of it!.
					</p>
				</div>
				<div class="p2">
					<p>
						If the most recent version of code that is operating here does not appear to be hosted on github, or there is some
						functionality that you would like to see implemented, please do <a href="mailto:jeremiah@crackbra.in">email me</a>
						and let me know.
					</p>
				</div>
			<form method="POST">
				<label for="appname">Appname</label>
				<input type="text" name="appname" id="appname">
				<label for="apikey">API Key</label>
				<input type="text" name="apikey" id="apikey">
				<input type='submit' name="submit" value="submit">
			</form>
	"""
	return pagehtml

def overview(server, errormessage=None):
	totalTags = server.getCount('ContactGroup',{})
	totalContacts=server.getCount('Contact',{})
	pagehtml = """
			<table>
				<tr>
					<td>Total Tags</td>
					<td>%s</td>
				</tr>
				<tr>
					<td>Total Contacts</td>
					<td>%s</td>
				</tr>
			</table>""" %(str(totalTags), str(totalContacts))
	if errormessage:
		pagehtml+= """
		<div class="errormessage">%s</div>
		""" %(errormessage)
	return pagehtml

def updateSeveralContacts(postdata, newTagId, server):
	allpostkeys=postdata.keys()
	for eachkey in allpostkeys:
		if (eachkey[:6]=="update"):
			cid=int(postdata[eachkey].value)
			server.addTagToContact(cid, newTagId)

def randomContacts(postdata, server):
	alltags=[]
	server.prep()
	tagids=server.tags.keys()
	for eachid in tagids:
		alltags.append((eachid, server.tags[eachid].name))
	alltags.sort(key=lambda val:val[1])
	pagehtml = """
	<div class="ranconExplanation" >
		<p>
			This function will allow you to choose a number of your contacts at random.  You can choose either
			from the pool of all contacts, or just the contacts with one particular tag.
		<p>
	</div>
	<form method="POST">
		<table>
			<tr>
				<td>
					<input type="radio" name="allorsome" value="all" checked>Use all contacts
				</td>
				<td>
					<input type="radio" name="allorsome" value="some">Only use contacts with this tag:
					<select name="tags">
						<option value="" disabled selected>Select a tag</option>
	"""
	for eachid in alltags:
		pagehtml = pagehtml + """
									<option value="%s">%s</option>
		""" %(str(eachid[0]), eachid[1])
	pagehtml += """
					</select>
				</td>
			</tr>
			<tr>
				<td colspan="2">
					<label for="numcon">Number Of Contacts To Choose:</label>
					<input type="text" name="numcon">
				</td>
			</tr>
		</table>
		<input type="submit" name="rancon2" value="Get Results">
	</form>
	"""
	return pagehtml

def randomContacts2(postdata, server):
	"""
	This function takes the criteria for the random selection of contacts, verifies that they are logical (ie: there
	are enough contacts in the pool to meet the number of contacts) and then displays the list of randomly chosen
	contacts.  There will be a button to apply tags to the selected contacts.
	"""
	alltags=[]
	contactsinpool=[]
	selectedcontacts=set()
	server.prep()
	if not(postdata.has_key('numcon')):
		return """Error: No number of contacts Selected"""
	else:
		try:
			numberToSelect=int(postdata['numcon'].value)
		except:
			return """Error: Number of contacts must only contain integers and no other characters"""
	if not(postdata.has_key('allorsome')):
		return """Error: You must either select all contacts or just a subset of contacts"""
	if (postdata['allorsome'].value == 'some'):
		if not(postdata.has_key('tags')):
			return """Error: If "Use all contacts" is not selected you must choose a tag"""
		else:
			pooltagID = int(postdata['tags'].value)
			contactsinpool = server.getContactIDWithTag(pooltagID)
	else:
		contactsinpool = server.getAllContacts()
	if (numberToSelect>len(contactsinpool)):
		return """Error: You cannot select %s records when there are only %s in the pool"""%(str(numberToSelect), str(len(contactsinpool)))
	elif (numberToSelect == len(contactsinpool)):
		selectedcontacts = set(contactsinpool)
	else:
		while (len(selectedcontacts)<numberToSelect):
			selectedcontacts.add(random.choice(contactsinpool))
	tagids=server.tags.keys()
	for eachid in tagids:
		alltags.append((eachid, server.tags[eachid].name))
	alltags.sort(key=lambda val:val[1])
	pagehtml = """
	<form method="POST">
		<div class="whatToDo">
			<table border="2">
				<tr>
					<td>
						<label>
							<input type="radio" name="neworold" value="new" checked>
							Apply New Tag
						</label><br />
						<input type="text" name="tagToCreate" />
					</td>
					<td>
						<label>
							<input type="radio" name="neworold" value="old">
							Apply existing Tag
						</label><br />
						<select name="tags">
						<option value="" disabled selected>Select a tag</option>
	"""
	for eachid in alltags:
		pagehtml = pagehtml + """
									<option value="%s">%s</option>
		""" %(str(eachid[0]), eachid[1])
	pagehtml += """
						</select>
					</td>
				</tr>
				<tr>
					<td colspan="2">
						<input type="submit" name="updateRanCon" value = "Apply tag to selected Contacts">
					</td>
				</tr>
			</table>
		</div>
		<div class="selected Records" >
			<table border="2">
	"""
	for eachrecord in selectedcontacts:
		pagehtml +="""
				<tr>
					<td width="50">
						<input type="hidden" name="contactID" value="%s">
						%s
					</td>
					<td width="200">
						%s
					</td>
					<td width="200">
						%s
					</td>
					<td width="500">
						%s
					</td>
				</tr>
		""" %(str(eachrecord.cid), str(eachrecord.cid), str(eachrecord.fname), str(eachrecord.lname), str(eachrecord.email))
	pagehtml += """
			</table>
		</div>
	"""
	return pagehtml

def updateRandomContacts(postdata,server):
	server.prep()
	if (postdata['neworold'].value=="new"):
		if not(postdata.has_key('tagToCreate')):
			return """Error: Need To Type in tag to create"""
		else:
			tagID=server.createNewTag(postdata['tagToCreate'].value)
	else:
		if not(postdata.has_key('tags')):
			return """Error: No Tag Selected"""
		else:
			tagID=int(postdata['tags'].value)
	for eachrecord in postdata['contactID']:
		server.addTagToContact(int(eachrecord.value), tagID)
	return "Completed!"

def tagsWithContacts(postdata, server):
	server.prep()
	tagids = server.tags.keys()
	tagcounts = []
	for eachid in tagids:
		tagcounts.append((eachid, server.tags[eachid].name, server.getCount('ContactGroupAssign',{'GroupId':eachid})))
	tagcounts.sort(key=lambda val:val[2])
	pagehtml = """
	<table name="tagsApplied">
	<tr>
		<td width="250">tagID</td>
		<td width="500">Tag Text</td>
		<td width="250">Number of contacts with tag</td>
	</tr>
	"""
	for eachrecord in tagcounts:
		pagehtml += """
			<tr>
				<td >%s</td>
				<td >%s</td>
				<td >%s</td>
			</tr>
		""" %(str(eachrecord[0]),str(eachrecord[1]), str(eachrecord[2]))
	pagehtml += """
	</table>
	"""
	return pagehtml

def purchasepage1():
	pagehtml="""
	<h1>WARNING:</h1>
	<h3>If you do not have a Demo merchant account, this process can and will charge against a real merchant account.</h3>
	<p>Basically:  Unless you really really want to do this, don't.</p>
	<form method="POST">
		<input type="submit" name="goto2" value="I understand, please proceed">
	</form>
	"""
	return pagehtml

def purchasepage2(server):
	contacts = []
	contacts = server.getContactsWithCards()
	pagehtml = """
	<h1>Purchase Step 1</h1>
	<h3>Select a contact</h3>
	<p>This is a list of all contact with credit cards.</p>
	<form method="POST">
		<table>
			<tr>
				<td>Select</td>
				<td>First Name</td>
				<td>Last Name</td>
				<td>Email Address</td>
				<td>Last 4 of CC on file</td>
			</tr>
	"""
	for each in contacts:
		pagehtml+="""
			<tr>
				<td><input type="radio" name="cid" value="%s_%s" /></td>
				<td>%s</td>
				<td>%s</td>
				<td>%s</td>
				<td>%s</td>
			</tr>
		"""%(str(each.cid), str(each.cardid), str(each.fname), str(each.lname), str(each.email), str(each.last4))
	pagehtml+="""
		</table>
		<input type="submit" name="goto3" value="Use Selected Contact" />
	</form>
	"""
	return pagehtml

def purchasepage3(postdata, server):
	products=server.getAllProducts()
	cid, ccid = postdata['cid'].value.split('_')
	pagehtml="""
	<form method="POST" >
		<table>
			<tr>
				<td>Promo Code:(required)</td>
				<td><input type="hidden" name="promocode" value="apitest" /> </td>
			</tr>
		</table>
		<input type="hidden" name="cid" value="%s" />
		<input type="hidden" name="ccid" value="%s" />
		<table>
			<tr>
				<td>Select</td>
				<td>Product Name</td>
				<td>Product Price</td>
			</tr>
	"""%(cid, ccid)
	for each in products:
		pagehtml+="""
			<tr>
				<td><input type="radio" name="product" value="%s" /></td>
				<td>%s</td>
				<td>%s</td>
		"""%(str(each[0]),str(each[1]), str(each[2]))
	pagehtml+="""
		</table>
		<input type="submit" name="goto4" value="Use Selected Product">
	</table>
	"""
	return pagehtml

def purchasepage4(postdata, server):
	cid = int(postdata['cid'].value)
	ccid = int(postdata['ccid'].value)
	payPlanId=0
	product=[]
	product.append(int(postdata['product'].value))
	subscriptions=[]
	processSpecials=True
	promoCodes=[]
	promoCodes.append(postdata['promocode'].value)
	leadAff=0
	salesAff=0
	argsString = """
	cid = %s <br />
	ccid = %s <br />
	payPlanId = %s <br />
	productIds = %s <br />
	subscriptionPlanIds = %s <br />
	processSpecials = %s <br />
	promoCodes = %s <br />
	leadAffiliateId = %s <br />
	saleAffiliateId = %s <br />
	"""%(str(cid), str(ccid), str(payPlanId), str(product), str(subscriptions), str(processSpecials), str(promoCodes), str(leadAff), str(salesAff))
	try:
		orderresults=server.placeOrder(cid, ccid, payPlanId,product, subscriptions, processSpecials, promoCodes,leadAff,salesAff)
		updateStatus="""
		Order %s was successfully created.
		"""%(str(orderresults['OrderId']))
	except Exception as e:
		updateStatus="""<h1>Failure</h1><br /> """ + argsString
	return updateStatus

def footer():
	pagehtml="""
		</body>
	</html>
	"""
	return pagehtml
Status API Training Shop Blog About
© 2015 GitHub, Inc. Terms Privacy Security Contact
