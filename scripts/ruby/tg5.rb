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


