#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-02-07 00:07:25
# @Last Modified 2015-02-08
# @Last Modified time: 2015-02-08 09:04:00

# this is a first attempt at anything after browsing up to chapter 9 of "ruby wizardry" a kids book on ruby.
#  you can see the publishers page here : http://www.nostarch.com/rubywizardry

class Card
	attr_reader :suit, :value, :point_value
	def initialize(suit, value, point_value)
		@suit = suit
		@value = value
		@point_value = point_value
	end
end

class Player
	@@NumOfPlayers = 0

	def initialize(name, cutoff)
		@name=name
		@deck=[]
		@bankroll=1000
		@cutoff_point=cutoff 
	end

	def add_card(card)
		@deck << card
	end

	def hit_or_stand()
		value_of_hand=[]
		@deck.each do |card|
			=start
			I am going to bed, so I am going to rough this out.

			if card.point_value ==[1,11]
				temp_holder = []
				for each in value_of_hand
					temp_holder << each + 1
					temp_holder << each + 11
				end
			else

			value_of_hand = value_of_hand + card.point_value }
		if value_of_hand



faces = [ j=:jack, q=:queen, k=:king, a=:ace ]
values = (2..10).to_a + faces
suits = [ h=:hearts, s=:spades, d=:diamonds, c=:clubs ]
deck = []


suits.each do |suit|
	values.each do |value|
		if value==a
			points = [1,11]
		elsif faces.include? value
			points = 10
		else
			points = value
		end

		deck << Card.new(suit, value, points)
	end
end

deck.each do |card|
	puts card.value.to_s + " of " + card.suit.to_s + " point value: " + card.point_value.to_s
end




#values.each { |this_card| puts this_card.to_s }