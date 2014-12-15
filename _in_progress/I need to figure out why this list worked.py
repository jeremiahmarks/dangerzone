PyCrust 0.9.5 - The Flakiest Python Shell
Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from random import choice
>>> list_of_values= ('ace',"two","three","four","five","six","seven","eight","nine","ten","jack","queen","king")
>>> list_of_suites=("hearts","spades","diamonds","clubs")
>>> the_trash=[]
>>> def get_card():
...     num_of_val=len(list_of_values)
...     num_of_suites=len(list_of_suites)
...     total_cards=num_of_val*num_of_suites
...     card_val=choice(list_of_values)
...     card_suite=choice(list_of_suites)
...     print card_val + " of "+card_suite
...     
>>> get_card()
nine of hearts
>>> x=get_card()
ten of spades
>>> x
>>> print x
None
>>> def get_card(x):
...     num_of_val=len(list_of_values)
...     num_of_suites=len(list_of_suites)
...     total_cards=num_of_val*num_of_suites
...     card_val=choice(list_of_values)
...     card_suite=choice(list_of_suites)
...     print card_val + " of "+card_suite
...     
>>> x
>>> get_card()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: get_card() takes exactly 1 argument (0 given)
>>> get_card(x)
seven of clubs
>>> x
>>> print x
None
>>> def get_card(x):
...     num_of_val=len(list_of_values)
...     num_of_suites=len(list_of_suites)
...     total_cards=num_of_val*num_of_suites
...     card_val=choice(list_of_values)
...     card_suite=choice(list_of_suites)
...     x=card_val + " of "+card_suite
...     print x
...     
>>> get_card(x)
ten of spades
>>> print x
None
>>> x=get_card(x)
five of clubs
>>> print x
None
>>> a=7
>>> b=(a,7)
>>> print b
(7, 7)
>>> a="house"
>>> print b
(7, 7)
>>> b=(a,7)
>>> print b
('house', 7)
>>> for t in b:
...     print t
...     
house
7
>>> list_of_cards
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'list_of_cards' is not defined
>>> for p in list_of_suites:
...     for q in list_of_values:
...         list_of_cards.append[q, " of ", p]
...     
Traceback (most recent call last):
  File "<input>", line 3, in <module>
NameError: name 'list_of_cards' is not defined
>>> list_of_cards=()
>>> for p in list_of_suites:
...     for q in list_of_values:
...         list_of_cards.append[q, " of ", p]
...     
Traceback (most recent call last):
  File "<input>", line 3, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> list_of_cards=[]
>>> for p in list_of_suites:
...     for q in list_of_values:
...         list_of_cards.append(q, " of ", p)
...     
Traceback (most recent call last):
  File "<input>", line 3, in <module>
TypeError: append() takes exactly one argument (3 given)
>>> for p in list_of_suites:
...     for q in list_of_values:
...         list_of_cards.append(q+"_of_"+p)
...     
>>> list_of_cards
['ace_of_hearts', 'two_of_hearts', 'three_of_hearts', 'four_of_hearts', 'five_of_hearts', 'six_of_hearts', 'seven_of_hearts', 'eight_of_hearts', 'nine_of_hearts', 'ten_of_hearts', 'jack_of_hearts', 'queen_of_hearts', 'king_of_hearts', 'ace_of_spades', 'two_of_spades', 'three_of_spades', 'four_of_spades', 'five_of_spades', 'six_of_spades', 'seven_of_spades', 'eight_of_spades', 'nine_of_spades', 'ten_of_spades', 'jack_of_spades', 'queen_of_spades', 'king_of_spades', 'ace_of_diamonds', 'two_of_diamonds', 'three_of_diamonds', 'four_of_diamonds', 'five_of_diamonds', 'six_of_diamonds', 'seven_of_diamonds', 'eight_of_diamonds', 'nine_of_diamonds', 'ten_of_diamonds', 'jack_of_diamonds', 'queen_of_diamonds', 'king_of_diamonds', 'ace_of_clubs', 'two_of_clubs', 'three_of_clubs', 'four_of_clubs', 'five_of_clubs', 'six_of_clubs', 'seven_of_clubs', 'eight_of_clubs', 'nine_of_clubs', 'ten_of_clubs', 'jack_of_clubs', 'queen_of_clubs', 'king_of_clubs']
>>> for k in list_of_cards:
...     print k
...     
ace_of_hearts
two_of_hearts
three_of_hearts
four_of_hearts
five_of_hearts
six_of_hearts
seven_of_hearts
eight_of_hearts
nine_of_hearts
ten_of_hearts
jack_of_hearts
queen_of_hearts
king_of_hearts
ace_of_spades
two_of_spades
three_of_spades
four_of_spades
five_of_spades
six_of_spades
seven_of_spades
eight_of_spades
nine_of_spades
ten_of_spades
jack_of_spades
queen_of_spades
king_of_spades
ace_of_diamonds
two_of_diamonds
three_of_diamonds
four_of_diamonds
five_of_diamonds
six_of_diamonds
seven_of_diamonds
eight_of_diamonds
nine_of_diamonds
ten_of_diamonds
jack_of_diamonds
queen_of_diamonds
king_of_diamonds
ace_of_clubs
two_of_clubs
three_of_clubs
four_of_clubs
five_of_clubs
six_of_clubs
seven_of_clubs
eight_of_clubs
nine_of_clubs
ten_of_clubs
jack_of_clubs
queen_of_clubs
king_of_clubs
>>> 