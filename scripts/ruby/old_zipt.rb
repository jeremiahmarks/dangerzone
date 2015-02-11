#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-11 12:03:03
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-02-11 14:09:57

require 'uri'
require 'net/http'
require 'rexml/document'


$zipwise_key = "wtgi32od8rh37dee"

uri = URI.parse("http://www.zipwise.com/webservices/distance.php?key=#{$zipwise_key}&zip1=85201&zip2=79109&format=xml")
# uri = URI.parse('http://api.search.yahoo.com/WebSearchService/V1/webSearch?appid=YahooDemo&query=madonna&results=2')


http = Net::HTTP.new(uri.host, uri.port)
request = Net::HTTP::Get.new(uri.request_uri)

response = http.request(request)

data = REXML::Document.new(response.body)
data.elements.each('results/distance') do |ele|
	puts " distance : #{ele.text.to_i}"
end

#puts response