#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-02-11 23:17:03
# @Last Modified 2015-02-11>
# @Last Modified time: 2015-02-11 23:20:56

require 'mysql'
require 'csv'
require_relative 'my.pw'

path_to_file="~/cityzip.csv"

CSV.foreach(path_to_file) do |row|
	puts row
end