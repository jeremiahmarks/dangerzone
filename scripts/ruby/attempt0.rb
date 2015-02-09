#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-02-07 00:07:25
# @Last Modified 2015-02-08
# @Last Modified time: 2015-02-08 19:28:33

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

	def add_card(card)
		@hand << card
		@next_move = self.calculate_cards
		if @next_move==:win
			return @next_move
		end
	end

	def calculate_cards()
		value_of_hand = [0] #set zero to ensure that first value is there to add to
		@hand.each do |card|
			if card.point_value == [1,11]
				# from testing in the irb
				#   a.map! { |fred| fred ? [fred+1, fred-1] : fred  }
				value_of_hand.map! { |hand_value| hand_value ? [hand_value +1, hand_value+11] : hand_value }.flatten! 
			else
				value_of_hand.map! {|hand_value| hand_value+card.point_value}
			end
		end
		# I am sure that there was an easy way that I could test for a winner in the last iterator (esp since I created 
		# 	these) values there.) but for not I am going to use another iterator
		current_plan=:bust
		value_of_hand.each do |value|
			if value==21
				current_plan=:win
				break
			elsif value<@cutoff_point
				current_plan=:hit
				next
			elsif value<21
				current_plan=:stand
			else
				current_plan=:bust
			end
		current_plan
	end

	def get_ante(value)
		if value>@bankroll
			response = :OutOfMoney
		else
			@bankroll -=1
			response = 1
		end
		response
	end
				
############################################################################
############################################################################
###  This will be the method graveyard, where they go to die. 
############################################################################
############################################################################
	# def hit_or_stand()
	# 	value_of_hand=[]
	# 	@hand.each do |card|
	# 		if card.point_value ==[1,11]
	# 			temp_holder = []
	# 			value_of_hand.each do |potential_outcome|
	# 				temp_holder << potential_outcome + 1
	# 				temp_holder << potential_outcome + 11
	# 			end
	# 			value_of_hand = temp_holder
	# 		else
	# 			value_of_hand.map! { |potential_outcome| potential_outcome + card.point_value }
	# 		end
	# 	end
	# 	if value_of_hand.include? 21
	# 		return "win"
	# 	elsif value_of_hand
	# 	#######################
	# 	####Stopped here#######
	# 	end
	# end
############################################################################
############################################################################
# ##
# While I see that =begin and =end works, it does not stick out enough in my text editor
# So I am going to comment like this.  
# 
# I am moving the initialize to the bottom of the document becuase I always want to be able 
#   to find it quickly.  In the code that I have seen so far, it seems like it has been in different places 
# 	but this move feels like a good one to me
# ##


	def initialize(name, cutoff)
		@name=name
		@hand=[]
		@bankroll=1000
		@cutoff_point=cutoff 
	end
end


class game_of_blackJack



	def new_deck
		faces = [ j=:jack, q=:queen, k=:king, a=:ace ]
		values = (2..10).to_a + faces
		suits = [ h=:hearts, s=:spades, d=:diamonds, c=:clubs ]
		@deck = []
		suits.each do |suit|
			values.each do |value|
				if value==a
					points = [1,11]
				elsif faces.include? value
					points = 10
				else
					points = value
				end

				@deck << Card.new(suit, value, points)
			end
		end
	end

	def remove_player(player)
		

	def game_cycle()
		@current_pot=0
		@people.each do |player|
			ante=player.get_ante
			if ante==:OutOfMoney

	end


	def initialize(*players)
		@people = []
		players.each{ |player| people << Player.new(player, 17)}
		self.new_deck()
	end

end

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