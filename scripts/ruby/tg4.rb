#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-02-08 17:38:18
# @Last Modified 2015-02-08
# @Last Modified time: 2015-02-08 19:28:31

# Testing some class functionality

class Aa

	def fred
		puts "fred"
	end

	def initialize
		self.fred
	end
end


def test1
	value_of_hand=[17,19]
	current_plan=:bust
	value_of_hand.each do |value|
		if value==21
			current_plan=:win
			break
		elsif value<17
			current_plan=:hit
			next
		elsif value<21
			current_plan=:stand
		else
			current_plan=:bust
		end
	end
	current_plan
end

def test1a
	a=test1
	q="**************************\n"
	puts q
	puts a.to_s
	puts q
	if a==:stand
		puts "STAND!!!!!"
	else
		puts "Do not stand"
	end
end

def aa
	# This will test how an array reacts when deleting elements from within 
	# a loop
	a=["a",'b','classify { ||  }','d','e','ed']
	a.each do |some_value|
		if some_value=='classify { ||  }'
			a.delete(some_value)
		else
			puts some_value
		end
	end
	line="**************\n"
	5.times{|a| puts line}
	a.each { |x| puts x }
end