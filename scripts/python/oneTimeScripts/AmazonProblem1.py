#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Jeremiah Marks
# Contact: Jeremiah@JLMarks.org

# A quick aside: 
	# I had begun this question earlier, however my computer powered off 
	# unexpectidly while working on my solution. After that I did several things, 
	# among them doing some light reading on Graph mapping algorithms. 
	# The reading was not in depth, in the language that I am using, nor actually
	# pertinant to the problem. The url that I read was: 
	# http://www.programcreek.com/2012/12/leetcode-clone-graph-java/
	#
	#
	# Also after restarting my machine I found that I had been moved to the second
	# test problem. I have closed my browser and restarted from the begining. 

################################################################################
################################################################################
##
##	Basic assumptions
##  1. There are a relatively finate number of users
##	2. Since there are a relatively finate number of users, allowing the function to
##		run until it finds no more unique users is not too terriably bad.
##	3. The printSocialGraph method is independent of the Member class
##	4. The output will be in the format of:
##		LevelX<tab>friendname<tab>friendemail
##	5. Friends should only be listed one time, in the closest position to Member M
##	6. Email address are unique in the system
################################################################################
################################################################################
################################################################################
##
## Approach:
##
## printSocialGraph(member=M)
##	friendsatdepth=dictionary{0:M} 						# because level 0 = self
##	emailaddressesused=set() 							# using a set to quickly determine if a friend has already been listed
##	emailaddressesused.add(M.email)						# to avoid looping back on myself
##	friendsatdepth[1]=getFriendsof(M,emailaddressesused)# all friends associated with 
##
##	emailsbefore=0										# updating the sentinal value
##	thisdepth=1 										# setting the initial level of friends to cycle through
##  while (emailsbefore != len(emailaddressesused)):	# basically if you run through everyone at a level and there are no new email addresses used, you are done
##		emailsbefore=len(emailaddressesused) 			# updating the sentinal value
##		nextdepth=thisdepth+1 							
##		friendsatdepth[nextdepth]=[]					#starting a blank list to add friends to
##		for eachfriend in friendsatdepth[thisdepth]:	# cycle through all friends at this level and get a list of their frinds
##			friendsatdepth[nextdepth].append(getFriendsof(friend, emailaddressesused)) 
##		thisdepth+=1 									# after we go through all of the friends at this level, start the next level.
##
##
## getFriendsof(user, usedemails):						# method to get all new, unlisted friends
##	friendslist=[]										# start with an empty list
##	for friend in user.friends:							#
##		if friend.email not in emailaddressesused:		# if the friend has not yet been listed
##			emailaddressesused.add(friend.email)		# then add their email to the set of used emails
##			friendslist.append(friend)					# and add the friend to the list
##	return friendslist									# return the list
################################################################################
################################################################################
################################################################################
##																			  ##
##	Creating Test Data														  ##
##																			  ##
################################################################################
################################################################################
##	class Member():
##
##		def __init__(self, name, email):
##			self.name=name
##			self.email=email
##			self.friends=[]
##		def addfriend(self, friendtoadd):
##			self.friends.append(friendtoadd)
##
##	def simplenetwork():
##		allnodes=[]
##		for x in range(65,78):
##			allnodes.append(Member(chr(x), chr(x)+"@"+chr(x)))
##		mainnode=allnodes[12] #this is Member"M"
##		connections={'M':[0,1,2,3],'A':[12,1,2,4,5],'B':[12,0,3,5],'C':[12,0,4],'D':[12,1,6],'E':[0,2,6,7],'F':[0,1,7,8],'G':[3,4,8,9],'H':[4,5],'I':[5,6,9],'J':[6,8]}
##		for node in connections.keys():
##			thisnode=allnodes[ord(node)-65]
##			for friend in connections[node]:
##				thisnode.addfriend(allnodes[friend])
##		return allnodes
################################################################################
################################################################################

def getFriendsof(user, usedemails):
	"""
	This method is used to get all "new" friends of a desired user. It accepts a
	Member object and a set object of email addresses that are not "new" to the 
	map.
	"""
	friendslist=[]							# creates a new, empty list object to hold all new friends added.
	for friend in user.friends:				# 
		if friend.email not in usedemails:	# if the email address has not been added to the usedemails set
			usedemails.add(friend.email)	# it adds that email, and then
			friendslist.append(friend)		# adds the friend to the friend list
	return friendslist						# which it returns.

def printSocialGraph(memberM):
	"""
	This method accepts a Member object and then prints out the list of friends 
	that object has at progressive distances from itself. 

	"""
	friendsatdepth={0:[memberM]}								#due to the way that I am printing these object out, memberM needed to be in a list
	emailaddressesused=set()									#a new, empty set to hold all of the email addresses that have already been used.
	emailaddressesused.add(memberM.email)						#adding the first email to that list so that we don't loop back on ourselves
	
	emailsbefore=thisdepth=0
  	while (emailsbefore != len(emailaddressesused)):			#This loop is where we actually start building our output
  																#If there are no email addresses added at any level, then we have found the maximum depth
  																#	of the users network
  		emailsbefore=len(emailaddressesused)
		nextdepth=thisdepth+1
		friendsatdepth[nextdepth]=[]
		for eachfriend in friendsatdepth[thisdepth]:
			friendsatdepth[nextdepth]+=getFriendsof(eachfriend, emailaddressesused)
		thisdepth+=1 

	for eachlevel in friendsatdepth.keys():						#This loop is where we start printing the output
		for efriend in friendsatdepth[eachlevel]:
			print(str(eachlevel)+"\t"+efriend.name+"\t"+efriend.email)
