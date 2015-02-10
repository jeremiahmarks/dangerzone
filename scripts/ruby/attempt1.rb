#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-09 14:01:01
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-02-09 17:56:30


# A cleaner version of ./attempt0.rb

class Card
	attr_reader :suit, :value, :point_value, :facedown

	def get_values
	    if @facedown
	      [nil,nil,nil]
	    else
	      [@suit, @value, @point_value ]
	    end
	end

	def flip
		@facedown = !@facedown
	end

	def initialize(suit, value, point_value)
		@facedown = true
		@suit = suit
	    @value = value
	    @point_value = point_value
	end
end

class Player
	attr_reader :name, :current_stand

	def add_card(card)
		#to add a card to their hand.
		@hand << card
	end

	def calculate_cards()
		@value_of_hand = [0]
		@hand.each do |card|
			if card.point_value == [1,11]
				@value_of_hand.map! { |hand_value| hand_value ? [hand_value +1, hand_value+11] : hand_value }.flatten!
			else
				@value_of_hand.map! {|hand_value| hand_value+card.point_value}
			end #end of if
		end # end of for each do

		@value_of_hand.each do |value|
			if value==21
				@current_plan=:win
				@current_stand = 0
				break
			elsif value<@cutoff_point
				@current_plan = :hit
				@current_stand = 0
			elsif value<21 && !@current_plan
				if value > @current_stand
					@current_stand = value
				end
				@current_plan = :stand
			else
				if !@current_plan
					@current_plan=:bust
				end #end small if
			end #end larger if
		end #end each do
	end # end calculate Cards

	def hit_stand_bust
		# get what the next move should be
		return @current_plan
	end #end hitstandbust

	def get_ante(value)
		if value>@bankroll
		    response = :OutOfMoney
		else
		    @bankroll -=1
		    response = 1
		end # end if
		response
	end # end get_ante

	def display_cards
		puts "\n\n"
	  	if @hand.empty?
		  	puts "Hand is empty"
	  	else
		    @hand.each do |card|
		    	if card.facedown==true
	        		print " facedown "
	      		else
	        		print card.get_values
	      		end # end nested if
	    	end # end each do
	  	end # end if
	  	print "\n"
	end # end display cards

	def game_end
		@hand[0].flip
		self.display_cards
		@hand=[]
	end # end game_end

	def accept_payment(amount)
		@bankroll+=amount
	end # end acceptPayment

	def initialize(name, cutoff)
		@name=name
		@hand=[]
		@bankroll=1000
		@cutoff_point=cutoff
	end #end init
end #end player





class Game_of_blackjack

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

    def deal_a_card_up
    	@people.each do |person|
    		a=@deck.delete @deck.sample
    		a.flip
    		person.add_card(a)
    	end
    end

    def deal_a_card_down
    	@people.each do |person|
    		a=@deck.delete @deck.sample
    		person.add_card(a)
    	end
    end

    def get_players_cards
    	@people.each do |person|
    		person.display_cards
    	end
    end

  	def initialize(*players)
  		@game_winner=nil
  		@round_winner=nil
  		@people=[]
  		players.each do |player|
  			@people << Player.new(player.to_s, 17)
  		end
  	end
end

def a
	s=Game_of_blackjack.new('a','b')
	s.new_deck
	s.deal_a_card_down
	s.deal_a_card_up
	s.get_players_cards
	return 0
end