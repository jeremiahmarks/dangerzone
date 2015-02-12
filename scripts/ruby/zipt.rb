#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-11 12:03:03
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-02-11 16:32:56

require 'uri'
require 'net/http'
require 'rexml/document'
require_relative 'my.pw'
# $zipwise_key = "Your key would be here"


def get_distance_between_zips(zip1, zip2)
	uri = URI.parse("http://www.zipwise.com/webservices/distance.php?key=#{$zipwise_key}&zip1=#{zip1.to_s}&zip2=#{zip2.to_s}&format=xml")
	http = Net::HTTP.new(uri.host, uri.port)
	request = Net::HTTP::Get.new(uri.request_uri)
	response = http.request(request)
	data = REXML::Document.new(response.body)
	data.elements.each('results/distance') do |ele|
		puts " distance : #{ele.text.to_i}"
	end
end

# uri = URI.parse("http://www.zipwise.com/webservices/distance.php?key=#{$zipwise_key}&zip1=85201&zip2=79109&format=xml")
# uri = URI.parse('http://api.search.yahoo.com/WebSearchService/V1/webSearch?appid=YahooDemo&query=madonna&results=2')


# http = Net::HTTP.new(uri.host, uri.port)
# request = Net::HTTP::Get.new(uri.request_uri)
# response = http.request(request)
# data = REXML::Document.new(response.body)
# data.elements.each('results/distance') do |ele|
# 	puts " distance : #{ele.text.to_i}"
# end

get_distance_between_zips(85201, 85001)

#puts response
