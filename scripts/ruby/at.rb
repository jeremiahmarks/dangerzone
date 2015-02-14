#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-13 18:41:59
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-02-13 18:51:28

def asdf(red={ })
	puts "hello!"
end

def test()
	asdf( {
		:a =>"A",
		:b => "B",
		})
end