#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

class TaskwarriorTask():
	def __init__(self,ID,taskuuid):
		self.uuid=taskuuid
		self.ID=ID





try:
	output==subprocess.Popen(["task","--version"], stdout=subprocess.PIPE)
	version=output.stdout.read()
except OSError:
	print "It appears that taskwarrior is not installed"

output=subprocess.Popen(["task", "information"], stdout=subprocess.PIPE)

while output.stdout.next():
	

alltaskinfo=output.stdout.read()

