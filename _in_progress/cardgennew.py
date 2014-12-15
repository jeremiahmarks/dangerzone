#card generator
from random import choice
list_of_values= ('ace',"two","three","four","five","six","seven","eight","nine","ten","jack","queen","king")
list_of_suites=("hearts","spades","diamonds","clubs")
#the_trash=()
player_hand_1=[]
player_hand_2=[]
list_of_cards = []
def get_card():
    num_of_val=len(list_of_values)
    num_of_suites=len(list_of_suites)
    total_cards=num_of_val*num_of_suites
    card_val=choice(list_of_values)
    card_suite=choice(list_of_suites)
    print card_val + "_of_"+card_suite
def shuffle():
    k = 0
    player_hand_1=[]
    player_hand_2=[]
    for p in list_of_suites:
        for q in list_of_values:
            cardd=(q+"_of_"+p)
            #print (cardd)
            #print p
            #print q
            #print k
            list_of_cards.append(cardd)
            #k=k+1

def deal_all():
	players=2
	stack_left=len(list_of_cards)
	while stack_left>0:
		print stack_left
		dealing=choice(list_of_cards)
		player_hand_1.append(dealing)
		list_of_cards.remove(dealing)
		dealing=choice(list_of_cards)
		player_hand_2.append(dealing)
		list_of_cards.remove(dealing)
		stack_left=len(list_of_cards)
