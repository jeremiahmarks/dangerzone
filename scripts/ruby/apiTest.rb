#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-10 14:00:49
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-02-10 14:39:16

#############################################################
##
## This file is the testing ground for the infusionsoft API
##
#############################################################

require 'xmlrpc/client'

$appname = 'if188'
$api_key = 'cba73d2468b0ac184e63ae047ccdd852'

$server = XMLRPC::Client.new2("https://#{$appname}.infusionsoft.com:443/api/xmlrpc")

def create_contact_hash ( firstName: "Testy", lastName: "McTesterPants", email: "example@example.com" )
	#This method creates a hash that stores a contact record
	contact={}
	contact["FirstName"] = firstName
	contact["LastName"] = lastName
	contact["Email"] = email
	contact
end

def add_contact_to_application
	contact = create_contact_hash()
	contact_id = $server.call("ContactService.add", $api_key, contact)
	puts "Contact with ID = #{contact_id} was created"
	contact_id
end

def dupe_add(email:"example@example.com")
	contact=create_contact_hash(email: email)
	puts contact
	contact_id = $server.call("ContactService.addWithDupCheck", $api_key, contact, "Email")
	puts "Contact with ID = #{contact_id} was created"
	contact_id
end

def get_list_of_tags
	tag_list=[]
end


def test
	#add_contact_to_application
	dupe_add
	dupe_add("dupeadd@til.la")
end
