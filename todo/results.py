#!/usr/bin/python
import cgi
print "Content-Type: text/html\n"
dynhtml='''<HTML><HEAD><TITLE>
Personal Details</TITLE></HEAD>
<BODY><H2>Personal details for: %s %s</H2>
<p>Your date of birth is: <b>%s</b></p>
<p>Your home address is: <b> %s </b></p>
<p>Your home phone is: <b> %s </b></p>
<p>Your e-mail address is: <b> %s </b></p>
<p>You have opted for the <b>%s</b> course</p>
</BODY></HTML>'''
fs = cgi.FieldStorage()
title = fs['studtitle'].value
name = fs["studname"].value
dob=fs["studdob"].value
add=fs["studadd"].value
phone=fs["studphone"].value
email=fs["emailadd"].value
course=fs["studcourse"].value
print dynhtml % (title,name,dob,add,phone,email,course)
