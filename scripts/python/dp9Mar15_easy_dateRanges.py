#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-03-09 14:38:00
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-03-09 18:13:29

# from: http://redd.it/2ygsxs

# example input = 2015-07-01 2015-07-04

import datetime

numberToMonth=["January","February","March","April","May","June","July","August","September","October","November","December"]
numberSuffixes=["st","nd","rd","th","th","th","th","th","th",""]

def solution(date1, date2):
	curYear=datetime.datetime.now().year
	d1split= [ int(x) for x in date1.split('-') ]
	d2split=[ int(x) for x in date2.split('-')]
	returnValue=[]
	## convert numerical month to word month
	for eachDate in [d1split,d2split]:
		returnValue.append({'m' : [numberToMonth[eachDate[1]-1]]})
	if (curYear == d1split[0]):
		if (curYear == d2split[0]):
			"""This will mean that both dates are this year"""
			yearNeeded=False
		elif ((d2split[0]==curYear+1) and )

