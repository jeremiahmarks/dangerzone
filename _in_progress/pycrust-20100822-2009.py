PyCrust 0.9.5 - The Flakiest Python Shell
Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56) 
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import cardgen
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "cardgen.py", line 5
    def get_card()
                 ^
SyntaxError: invalid syntax
>>> import cardgen
>>> cardgen.get_card
<function get_card at 0xb56dc72c>
>>> cardgen.get_card()
nine of diamonds
>>> cardgen.get_card()
jack of hearts
>>> cardgen.get_card()
five of diamonds
>>> cardgen.get_card()
two of spades
>>> cardgen.get_card()
ace of diamonds
>>> cardgen.get_card()
ace of hearts
>>> cardgen.get_card()
king of hearts
>>> cardgen.get_card()
four of clubs
>>> cardgen.get_card()
ace of spades
>>> cardgen.get_card()
seven of spades
>>> cardgen.get_card()
three of diamonds
>>> cardgen.get_card()
king of spades
>>> cardgen.get_card()
king of clubs
>>> cardgen.get_card()
king of clubs
>>> cardgen.get_card()
king of diamonds
>>> 