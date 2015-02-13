#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-10 14:00:49
# @Last Modified 2015-02-13
# @Last Modified time: 2015-02-13 00:53:19

#############################################################
##
## This file is the testing ground for the infusionsoft API
##
#############################################################
## Interesting methods to explore
## DataService.getAppSetting
## DataService.addCustomField
## DataService.updateCustomField
## DiscountService.addCategoryAssignmentToCategoryDiscount
## different email template merge context.
## Fileservice.uploadFile
## FileService.getDownloadURL
## do a funnel service.achieveGoal example
## look at some Invoice service stuff
## OrderService.placeOrder
## SearchService.getAllReportColumns
## SearchService.getSavedSearchResultsAllFields
## SearchService.getSavedSearchResults

##TABLES

##CCharge
##CProgram
##CampaignStep
##ContactAction
##DataFormField
##Expense
##FileBox
##Invoice
##InvoiceItem
##InvoicePayment
##Job
##JobRecurringInstance
##Lead
##MtgLead
##OrderItem
##PayPlan
##PayPlanItem
##Payment
##Product
##ProductOption
##RecurringOrderWithContact
##Referral
##SavedFilter
##Stage
##StageMove
##Template
##User
##UserGroup

#making edit to update get
require 'xmlrpc/client'
require_relative 'my.pw'

#$app_name = ' '
#$api_key = ' '

$server = XMLRPC::Client.new2("https://#{$app_name}.infusionsoft.com:443/api/xmlrpc")


def data_service_query(parameters={ })
	results={}
	p=0
	while true
		data_set = $server.call("DataService.query", $api_key, parameters[]||="ContactGroupCategory", parameters[]||=1000,parameters[]||=p,parameters[]||={},parameters[]||=['Id',"CategoryName","CategoryDescription"],parameters[]||='Id',parameters[]||= true )
		data_set.each do |result|
			results[datum['Id']] = { :id => datum['Id'], :name => datum['CategoryName'], :desc => datum["GroupDescription"]}
		end
		unless data_set.count==1000
			break
		end
		p+=1
	end
end
def get_custom_fields


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

def mark_contact_as_marketable(contact_id, optin_reason)
	#this method will take a contact id, find its matching email address, and then
	#opt in that email address.
	# algorithm :  find email addresses by id
	# opt them in.
	addresses = $server.call("DataService.query", $api_key, "Contact", 1000,p||=0,{ 'Id' => contact_id },['Email'],'Id', true )
	address = addresses[0]["Email"]
	if address
		optedIn = $server.call("APIEmailService.optIn", $api_key, address, optin_reason)
		if optedIn
			return :address
		end
		return nil
	end
	return :emailMissing
end
def create_new_tag (new_tag_name)
	#returns the tag id of the tag created
	return $server.call("DataService.add", $api_key, 'ContactGroup', {'GroupName' => new_tag_name})
end
def apply_tag_to_contact( contact_id, tag_id)
	#returns true if it did apply the tag to the contact. If the 
	#contact already has the tag, though, returns false
	return $server.call("ContactService.addToGroup", $api_key, contact_id, tag_id)
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
# 							from_address, to_address, subject, htmlBody, textBody
def sendWithStatus (parameters = {})
	return $server.call("APIEmailService.sendEmailWithStatus", $api_key, parameters[:from], parameters[:to], parameters[:cc]||="", parameters[:bcc]||="",parameters[:subject], parameters[:text], parameters[:html])
end

def sendTest
	params = {}
	params[:html] = <<-eos
		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
		<meta name="viewport" content="width=device-width" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<title>Really Simple HTML Email Template</title>
		<style>
		/* -------------------------------------
				GLOBAL
		------------------------------------- */
		* {
			margin: 0;
			padding: 0;
			font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
			font-size: 100%;
			line-height: 1.6;
		}

		img {
			max-width: 100%;
		}

		body {
			-webkit-font-smoothing: antialiased;
			-webkit-text-size-adjust: none;
			width: 100%!important;
			height: 100%;
		}


		/* -------------------------------------
				ELEMENTS
		------------------------------------- */
		a {
			color: #348eda;
		}

		.btn-primary {
			text-decoration: none;
			color: #FFF;
			background-color: #348eda;
			border: solid #348eda;
			border-width: 10px 20px;
			line-height: 2;
			font-weight: bold;
			margin-right: 10px;
			text-align: center;
			cursor: pointer;
			display: inline-block;
			border-radius: 25px;
		}

		.btn-secondary {
			text-decoration: none;
			color: #FFF;
			background-color: #aaa;
			border: solid #aaa;
			border-width: 10px 20px;
			line-height: 2;
			font-weight: bold;
			margin-right: 10px;
			text-align: center;
			cursor: pointer;
			display: inline-block;
			border-radius: 25px;
		}

		.last {
			margin-bottom: 0;
		}

		.first {
			margin-top: 0;
		}

		.padding {
			padding: 10px 0;
		}


		/* -------------------------------------
				BODY
		------------------------------------- */
		table.body-wrap {
			width: 100%;
			padding: 20px;
		}

		table.body-wrap .container {
			border: 1px solid #f0f0f0;
		}


		/* -------------------------------------
				FOOTER
		------------------------------------- */
		table.footer-wrap {
			width: 100%;	
			clear: both!important;
		}

		.footer-wrap .container p {
			font-size: 12px;
			color: #666;
			
		}

		table.footer-wrap a {
			color: #999;
		}


		/* -------------------------------------
				TYPOGRAPHY
		------------------------------------- */
		h1, h2, h3 {
			font-family: "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;
			line-height: 1.1;
			margin-bottom: 15px;
			color: #000;
			margin: 40px 0 10px;
			line-height: 1.2;
			font-weight: 200;
		}

		h1 {
			font-size: 36px;
		}
		h2 {
			font-size: 28px;
		}
		h3 {
			font-size: 22px;
		}

		p, ul, ol {
			margin-bottom: 10px;
			font-weight: normal;
			font-size: 14px;
		}

		ul li, ol li {
			margin-left: 5px;
			list-style-position: inside;
		}

		/* ---------------------------------------------------
				RESPONSIVENESS
				Nuke it from orbit. It's the only way to be sure.
		------------------------------------------------------ */

		/* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
		.container {
			display: block!important;
			max-width: 600px!important;
			margin: 0 auto!important; /* makes it centered */
			clear: both!important;
		}

		/* Set the padding on the td rather than the div for Outlook compatibility */
		.body-wrap .container {
			padding: 20px;
		}

		/* This should also be a block element, so that it will fill 100% of the .container */
		.content {
			max-width: 600px;
			margin: 0 auto;
			display: block;
		}

		/* Let's make sure tables in the content area are 100% wide */
		.content table {
			width: 100%;
		}

		</style>
		</head>

		<body bgcolor="#f6f6f6">

		<!-- body -->
		<table class="body-wrap">
			<tr>
				<td></td>
				<td class="container" bgcolor="#FFFFFF">

					<!-- content -->
					<div class="content">
					<table>
						<tr>
							<td>
								<p>Hi there,</p>
								<p>Sometimes all you want is to send a simple HTML email with a basic design.</p>
								<h1>Really simple HTML email template</h1>
								<p>This is a really simple email template. Its sole purpose is to get you to click the button below.</p>
								<h2>How do I use it?</h2>
								<p>All the information you need is on GitHub.</p>
								<table>
									<tr>
										<td class="padding">
											<p><a href="https://github.com/leemunroe/html-email-template" class="btn-primary">View the source and instructions on GitHub</a></p>
										</td>
									</tr>
								</table>
								<p>Feel free to use, copy, modify this email template as you wish.</p>
								<p>Thanks, have a lovely day.</p>
								<p><a href="http://twitter.com/leemunroe">Follow @leemunroe on Twitter</a></p>
							</td>
						</tr>
					</table>
					</div>
					<!-- /content -->
					
				</td>
				<td></td>
			</tr>
		</table>
		<!-- /body -->

		<!-- footer -->
		<table class="footer-wrap">
			<tr>
				<td></td>
				<td class="container">
					
					<!-- content -->
					<div class="content">
						<table>
							<tr>
								<td align="center">
									<p>Don't like these annoying emails? <a href="#"><unsubscribe>Unsubscribe</unsubscribe></a>.
									</p>
								</td>
							</tr>
						</table>
					</div>
					<!-- /content -->
					
				</td>
				<td></td>
			</tr>
		</table>
		<!-- /footer -->

		</body>
		</html>
	eos
	params[:from] = "jeremiah@jlmarks.org"
	params[:to] = "jeremiah.l.marks@gmail.com"
	params[:subject] = "Hello World!  I am testing Something new!"
	params[:text]="This is a simple text message.  I sent an html message, but I guess you wont be seeing it, huh?"
	statuses=sendWithStatus(params)
	puts statuses
end

def tm
	#this will get all of the different types of merge field for each type of template
	context = ["Contact", "Opportunity", "Invoice", "CreditCard"]
	context.each do |type|
		storage = File.open("#{type}.txt", "w")
		fields_available = $server.call("APIEmailService.getAvailableMergeFields", $api_key, type)
		fields_available.sort!
		fields_available.each do |field|
			storage << field + "\n"
		end
		storage.close
	end
end
