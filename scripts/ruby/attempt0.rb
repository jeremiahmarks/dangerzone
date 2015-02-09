#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-02-07 00:07:25
# @Last Modified 2015-02-09
# @Last Modified time: 2015-02-09 01:40:18

# this is a first attempt at anything after browsing up to chapter 9 of "ruby wizardry" a kids book on ruby.
#  you can see the publishers page here : http://www.nostarch.com/rubywizardry

class Card
  attr_reader :suit, :value, :point_value
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
  attr_reader :facedown
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



class Player
  attr_reader :name
  @@NumOfPlayers = 0

  def add_card(card)
    @hand << card
    @next_move = self.calculate_cards
  end
end

def calculate_cards()
  @value_of_hand = [0] #set zero to ensure that first value is there to add to
  @hand.each do |card|
    if card.point_value == [1,11]
      # from testing in the irb
      #   a.map! { |fred| fred ? [fred+1, fred-1] : fred  }
      @value_of_hand.map! { |hand_value| hand_value ? [hand_value +1, hand_value+11] : hand_value }.flatten!
    else
      @value_of_hand.map! {|hand_value| hand_value+card.point_value}
    end
  end
  # I am sure that there was an easy way that I could test for a winner in the last iterator (esp since I created
  #   these) values there.) but for not I am going to use another iterator
  current_plan=:bust
  @value_of_hand.each do |value|
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
end

def hit_stand_bust
  return @next_move
end

def get_value_of_hand
  closest=0
  @value_of_hand.each do |value|
    if 21-value < 21-closest
      closest = value
    end
  end
  return closest
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

def display_cards
  puts "\n\n"
  if @hand.empty?
  else
    @hand.each do |card|
      if card.facedown==true
        print " facedown "
      else
        print card.get_values
      end
    end
  end
  print "\n"
end

def game_end
  @hand[0].flip
  @hand
end

def accept_payment(amount)
  @bankroll+=amount
end


############################################################################
############################################################################
###  This will be the method graveyard, where they go to die.
############################################################################
############################################################################
# def hit_or_stand()
#   @value_of_hand=[]
#   @hand.each do |card|
#     if card.point_value ==[1,11]
#       temp_holder = []
#       @value_of_hand.each do |potential_outcome|
#         temp_holder << potential_outcome + 1
#         temp_holder << potential_outcome + 11
#       end
#       @value_of_hand = temp_holder
#     else
#       @value_of_hand.map! { |potential_outcome| potential_outcome + card.point_value }
#     end
#   end
#   if @value_of_hand.include? 21
#     return "win"
#   elsif @value_of_hand
#   #######################
#   ####Stopped here#######
#   end
# end
############################################################################
############################################################################
# ##
# While I see that =begin and =end works, it does not stick out enough in my text editor
# So I am going to comment like this.
#
# I am moving the initialize to the bottom of the document becuase I always want to be able
#   to find it quickly.  In the code that I have seen so far, it seems like it has been in different places
#   but this move feels like a good one to me
# ##


def initialize(name, cutoff)
  @name=name
  @hand=[]
  @bankroll=1000
  @cutoff_point=cutoff
end
end




class Game_of_blackJack



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

        @deck << Card_Down.new(suit, value, points)
      end
    end
  end

  def remove_player(player_to_remove)
    rv=nil
    @people.remove(player_to_remove)
    if @people.length == 1
      @winner=@people[0]
    end
  end

  def determine_winner(statuses)
    flat_stats=Hash(statuses.map.with_index.to_a)
    if statuses.include? :win
      number_of_winners = statuses.count(:win)
      if number_of_winners == 1
        winner_loc = flat_stats[:win]
        winner = @people[winner_loc]
        winner.accept_payment(@current_pot)
        2.times { puts "************************"}
        puts "Winner! #{@winner.name} won our pot of #{@current_pot}"
      else
        winners_share = @current_pot / number_of_winners
        puts "There were #{number_of_winners} winners!"
        @people.each { |person| person.hit_stand_bust == :win ? puts "#{person.name} won #{winners_share!}";person.accept_payment{winners_share} : next}
      end
    else
      number_of_standers = statuses.count(:stand)
      if number_of_standers == 1
        winner_loc = flat_stats[:stand]
        winner = @people[winner_loc]
        winner.accept_payment(@current_pot)
        2.times { puts "************************"}
        puts "Winner! #{@winner.name} won our pot of #{@current_pot}"
      else
        # winners_share = @current_pot / number_of_standers
        values_stood_on=[]
        list_of_winners = []
        @people.each do |person|
          if person.hit_stand_bust == :stand
            values_stood_on << person.get_value_of_hand
          end
        end
        #values_stood_on_flat=values_stood_on.map.with_index.to_a
        values_stood_on.each_with_index.to_a.each do |value, position|
          if list_of_winners.empty?
            list_of_winners << [value, position]
          elsif list_of_winners[0][0]<value
            list_of_winners = [[value, position]]
          elsif list_of_winners[0][0]==value
            list_of_winners << [value, position]
          end
        end
        winners_share = @current_pot / list_of_winners.count
        list_of_winners.each do |winnerLocation|
          thiswinner=@people[winnerLocation[1]]
          thiswinner.accept_payment(winners_share)
          puts "#{thiswinner.name} has won #{winners_share.to_s}"
        end
      end
    end
  end #ends determine winner

  def check_status
    statuses=[]
    @people.each do |person|
      statuses << person.hit_stand_bust
    end # ends @people.each do |person|
    if statuses.include? :hit
      rv=:continue
    else
      rv=self.determine_winner(statuses)
    end
  end #ends check_status


  def game_cycle()
    round_winner = nil
    @current_pot=0
    @people.each do |player|
      ante=player.get_ante(1)
      if ante==:OutOfMoney
        self.remove_player(player)
        if @winner
          break
        end
      else
        @current_pot+=ante
      end
      a=@deck.delete @deck.sample
      b=@deck.delete @deck.sample
      b.flip
      player.add_card(a)
      player.add_card(b)
    end
    self.check_cards
    until round_winner
      round_hit = 0
      round_stand = 0
      round_bust = 0
      @people.each do |player|
        player_status = player.hit_stand_bust
        if player_status == :hit
          round_hit += 1
          new_card=@deck.delete @deck.sample
          new_card.flip
          player.add_card(new_card)
        elsif player_status == :stand
          round_stand +=1
          next
        elsif player_status == :bust
          round_bust += 1
        end # ends if statement
      end # ends @people.each do |player|
      self.check_status
      if round_bust==@people.length
        #refund money, declar roundwinner="no one"
      elsif round_bust>0
        #see if all other members stand, if so calculate winner



      end
      round_winner=true
      @winner=true
    end
  end

  def check_cards
    @people.each do |person|
      person.display_cards
    end
  end



  def initialize(*players)
    @winner=nil
    @people = []
    players.each do |player|
      @people << Player.new(player.to_s, 17)
    end
    until @winner
      self.new_deck()
      game_cycle()
    end

  end

end


def a
  a=Game_of_blackJack.new("a", "b")
  0
end
