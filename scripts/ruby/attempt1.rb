#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-09 14:01:01
# @Last Modified 2015-02-10>
# @Last Modified time: 2015-02-10 00:17:51


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
		@current_plan=nil
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
	def ante_check(value)
		if value<=@bankroll
			:deal_in
		end
	end
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
	def cards_as_array
		temp_holder = []
		@hand.each do |card|
			temp_holder << card.get_values
		temp_holder
	end
	def game_end
		@hand[0].flip
		self.display_cards
	end # end game_end
	def accept_payment(amount)
		#
		@bankroll+=amount
	end # end acceptPayment
	def clear_hands
		#making sure that hands are empty when starting a new hand
		@hand=[]
	end
	def initialize(name, cutoff)
		@name=name
		@hand=[]
		@bankroll=1000
		@cutoff_point=cutoff
		@current_plan=:hit
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
    def deal_a_card_up(player=nil)
    	if player
    		a=@deck.delete @deck.sample
    		a.flip
    		player.add_card(a)
    	else
	    	@people.each do |person|
    			a=@deck.delete @deck.sample
    			a.flip
    			person.add_card(a)
    		end
    	end
    end
    def deal_a_card_down(player=nil)
    	if player
    		a=@deck.delete @deck.sample
    		player.add_card(a)
    	else
	    	@people.each do |person|
    			a=@deck.delete @deck.sample
    			person.add_card(a)
    		end
    	end
    end
    def get_players_cards
    	@people.each do |person|
    		person.display_cards
    	end
    end
    def award_winner(winner, winnings=@current_pot)
    	winner.accept_payment(winnings)
    	puts "\n\n\n\tWinner!\n#{winner.name} won #{winnings.to_s}\n"
    	@current_pot = @current_pot - winnings
    end
    def need_to_deal?
    	needs_cards=0
    	@players.each { |player| player.hit_stand_bust == :hit ? needs_cards +=1 }
    	needs_cards > 0
    end
    def determine_winner
    	##This probably took up most of the area of the paper I outlined. 
    	##Things that will be good to have to figure this out:
    	## 		array with players planned moves
    	## 		array with players cards and current plan and current stand
    	plans={}
    	stand_values={}
    	full_cards={}
    	counter=0
    	@players.each do |player|
    		player.game_end
    		plans[counter]= player.hit_stand_bust
    		stand_values[counter] = player.current_stand
    		full_cards[counter] = player.cards_as_array
    	end
    	if plans.has_value? :win
    		if plans.values.count(:win)==1
    			#there is only one winner
    			award_winner(@players[plans.key(:win)])
    		else
    			total_wins=plans.values.count(:win)
    			takings = @current_pot / total_wins
    			@players.each {|player| player.hit_stand_bust== :win ? self.award_winner(player, takings) : nil }
    		end
    	elsif plans.has_value? :stand
    		total_stands=plans.values.count(:stand)
    		if total_stands == 1
    			award_winner(@players[plans.key(:stand)])
    		else
    			#figure out who is closest
    			
    			






    end
    def one_hand
    	#Make sure that the pot is empty
    	@current_pot=0
    	#and that the sentinel variable stands ready
    	@hand_winner=nil
    	#get a deck of cards
    	self.new_deck
    	#make sure that the players are not trying to slide an extra card in
    	@people.each do |player|
    		player.clear_hands
    		#now their hands are clear, lets collect their ante and deal them in
    		if player.ante_check  #If a player can ante in, check if they are added to the table already. 
    			unless @players.include? player# If they are not, in the table
    				self.add_to_table(player) #invite them
    			end
    			@current_pot+=player.get_ante(@ante) # take their money
    			self.deal_a_card_down(player) # and give them a card down
    		else #basically if they did not pass the ante check
    			if @players.include? player #if they are at the table, ask them to leave
    				self.remove_from_table(player)
    			end
    		end
    	end
    	if @players.count == 0 
    		@game_winner = :No_one
    	elsif @players.count == 1
    		@game_winner = @players[0]
    		self.award_winner(@game_winner)
    	else
    		while self.need_to_deal?
    			@players.each do |player|
    				if player.hit_stand_bust == :hit
    					deal_a_card_up(player)
    					player.calculate_cards
    				end
    			end
    		end



    			


    end
    def add_to_table(player)
    	@players << player
    end
    def remove_from_table(player)
    	@players.delete(player)
    end
  	def initialize(*players)
  		@ante=1
  		@game_winner=nil
  		@round_winner=nil
  		@people=[] #this includes people who have gone broke
  		@players=[] #This is people who are still at the table
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