#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-10 14:00:49
# @Last Modified 2015-02-11
# @Last Modified time: 2015-02-12 19:12:15

#############################################################
##
## This file is the testing ground for the infusionsoft API
##
#############################################################
#making edit to update get
require 'xmlrpc/client'
require_relative 'my.pw'

#$app_name = ' '
#$api_key = ' '

$server = XMLRPC::Client.new2("https://#{$app_name}.infusionsoft.com:443/api/xmlrpc")

def create_contact_hash ( parameters={} )
	#This method creates a hash that stores a contact record
	contact={}
	contact["FirstName"] = parameters[:fn]
	contact["LastName"] = parameters[:ln]
	contact["Email"] = parameters[:em]
	contact
end

def add_contact_to_application
	contact = create_contact_hash( { :fn => "Another Testy", :ln => "McTesterPants", :em => "at@example.com"} )
	contact_id = $server.call("ContactService.add", $api_key, contact)
	puts "Contact with ID = #{contact_id} was created"
	contact_id
end

def add_with_dup_check(email = "example@example.com")
	contact=create_contact_hash({ :fn => "Another Testy", :ln => "McTesterPants", :em => email})
	contact_id = $server.call("ContactService.addWithDupCheck", $api_key, contact, "Email")
	puts "Contact with ID = #{contact_id} was created"
	contact_id
end

# def add_with_dup_check(email:"example@example.com")
# 	contact=create_contact_hash(email: email)
# 	puts contact
# 	contact_id = $server.call("ContactService.addWithDupCheck", $api_key, contact, "Email")
# 	puts "Contact with ID = #{contact_id} was created"
# 	contact_id
# end

def mark_contact_as_marketable(contact_id)
	#this method will take a contact id, find its matching email address, and then
	#opt in that email address.
	# algorithm :  find email addresses by id
	# opt them in.
	results = $server.call("DataService.query", $api_key, "Contact", 1000,p,{'Id' => contact_id},['Email'],'Id', true )
	for results.each do |result|
		puts result
	end
end

def get_list_of_tag_categories
	$current_tag_cat={}
	p=0
	while true
		results = $server.call("DataService.query", $api_key, "ContactGroupCategory", 1000,p,{},['Id',"CategoryName","CategoryDescription"],'Id', true )
		results.each do |result|
			$current_tag_cat[result['Id']] = { :id => result['Id'], :name => result['CategoryName'], :desc => result["GroupDescription"]}
		end
		unless results.count==1000
			break
		end
		p+=1
	end
end
def get_list_of_tags
	#Find the way that I looped this in python
	# https://github.com/jeremiahmarks/betterTagApplicationReport/blob/9e6f010b30060fe5cd5f62ff58cfe8bdba1adde5/myfunc.py#L66-L75
	get_list_of_tag_categories
	$current_tags={}
	p=0
	while true
		group_of_tags = $server.call("DataService.query", $api_key, "ContactGroup", 1000,p,{},['Id',"GroupCategoryId","GroupName","GroupDescription"],"GroupName", true )
		group_of_tags.each do |tag|
			$current_tags[tag['Id']] = { :id => tag['Id'], :Group => tag['GroupName'], :Description => tag['GroupDescription'], :GroupCategoryId=>tag['GroupCategoryId'], :GroupCategoryName=>$current_tag_cat[tag['GroupCategoryId']]}
			# unless $current_tags[tag['GroupCategoryId']]
			# 	$current_tags[tag['GroupCategoryId']] = [{ :Id => tag['Id'], :Group => tag['GroupName'], :Description => tag['GroupDescription']}]
			# else
			# 	$current_tags[tag['GroupCategoryId']] << { :Id => tag['Id'], :Group => tag['GroupName']}
			# end
		end
		unless group_of_tags.count == 1000
			break
		end
		p+=1
	end
end

def print_tags
	#a quick and easy meathod to see
	get_list_of_tags
	##
	## Since I changed the way that $current_tags stores information, I need to change this too
	## The end goal will have it to display in the format of "id = category => tag"
	groups = $current_tag_cat.keys.to_a << nil
	groups.each do |category_id|
		$current_tags.each do |tag_id, tag_data|
			if tag_data[:GroupCategoryId]==category_id
				puts "#{tag_data[:id].to_s} = #{tag_data[:GroupCategoryName][:name]} => #{tag_data[:Group]}"
			end
		end
	end
end


def find_contacts(parameters={})
	$current_contacts={}
	p=0
	while true
		results = $server.call("DataService.query", $api_key, "Contact", 1000,p,parameters,['Id',"Email","FirstName","Groups", "LastName", "Validated"],"Id", true )
		results.each do |result|
			$current_contacts[result['Id']]={:em => result['Email'], :fn => result['FirstName'], :groups => result["Groups"], :ln => result['LastName'], :validated => result['validated']}
		end
		unless results.count == 1000
			break
		end
		p+=1
	end
end

def get_list_of_tags_on_contact(parameters={})
	get_list_of_tags
	find_contacts(parameters)
	$current_contacts.each do |contact_id, contact|
		puts "#{contact[:fn]} #{contact[:ln]} at #{contact[:em]} has the following tags:"
		contact[:groups].split(',').map { |s| s.to_i}.each do |gid|
			puts "#{gid} -> #{$current_tags.select {|tag| tag[:Id]==gid}}"
		end
	end
end

def test
	#add_contact_to_application
	get_list_of_tags
	puts $current_tags
end
