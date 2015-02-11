#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-10 14:40:29
# @Last Modified 2015-02-10
# @Last Modified time: 2015-02-10 21:19:08


# def foo(str: "foo", num: 424242)
#   [str, num]
# end

# foo(num: 123)
require 'xmlrpc/client'
unless require './my.pw.rb'
	$app_name="AppNameHere"
	$api_key="YouAPIKey"
end

$server = XMLRPC::Client.new2("https://#{$app_name}.infusionsoft.com:443/api/xmlrpc")

contact={"FirstName"=>"Justin", "LastName"=>"Morris","Email"=>"justinm@infusionsoft.com"}
contact_id = $server.call("ContactService.add", $api_key, contact)
puts "Contact with ID = #{contact_id} was created"