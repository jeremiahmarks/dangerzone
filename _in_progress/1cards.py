#cards
list_of_values= ["ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king"]
list_of_suites=["hearts","spades","diamonds","clubs"]
k=len(list_of_values)
s=len(list_of_suites)
list_of_cards = []
for p in list_of_suites:
    for q in list_of_values:
        list_of_cards.append((q + " of "+ p))

    							
