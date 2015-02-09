#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-02-08 17:38:18
# @Last Modified 2015-02-09
# @Last Modified time: 2015-02-09 01:27:44

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
			puts a.delete(some_value) + "deleted"
		else
			puts some_value
		end
	end
	line="**************\n"
	5.times{|a| puts line}
	a.each { |x| puts x }
end

class Card

  def initialize(suit, value, point_value)
    @suit = suit
    @value = value
    @point_value = point_value
  end

  def get_values
    [ @suit, @value, @point_value ]
  end

end

class Card_Down < Card
	##############################################
	##This will be the card that only the player can see
	##############################################
	def initialize(suit, value, point_value)
    	@facedown = true
    	super
  	end

  	def flip
    	@facedown = !@facedown
  	end

  	def get_values
	    if @facedown
	    	[nil,nil,nil]
	    else
	    	[@suit, @value, @point_value ]
	    end
	end

end


def ab
	cards = [ Card.new(:h, :v, [1,11]), Card_Down.new(:h, :v, [1,11]) ]
	cards.each do |card|
		puts "*********************\n" + card.get_values.to_s
	end
	puts "\n\n\n\n\n"
	cards[1].flip
	cards.each do |card|
		puts "*********************\n" + card.get_values.to_s
	end

end



def ac
	aa=[1,2,3,9,4,5,9,8]
	aa.each_with_index.to_a.each do |test, location|
		puts test.to_s + " " + location.to_s
	end
end
