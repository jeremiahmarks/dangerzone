#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-10 13:00:15
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-02-10 14:20:19


########################################
##
## examples to add:
## 		Add tag to contact
## 		find all contacts with tag
## 		search for existing contact
## 		create new tag
## 		add people to FUS
## 		record order to contact record
##  	make new order for contact


#Initialize xmlrpc
require 'xmlrpc/client'
  require 'pp'

  #Encrypted API Key
  key="EncryptedAPIKey"

  #Define the servers URL
  server = XMLRPC::Client.new2("https://AppName.infusionsoft.com:443/api/xmlrpc")

  #Create Contact Hash
  contact={"FirstName"=>"Justin", "LastName"=>"Morris","Email"=>"justinm@infusionsoft.com"}

  #Make the server call to add a contact.
  result = server.call("ContactService.add", key, contact)
  pp "Contact added: #{result}"

  #Make the server call to add it to the group with ID 94
  result=server.call("ContactService.addToGroup",key,result,94)
  pp "Added to group: #{result}"