#cards
list_of_values= ('ace',"two","three","four","five","six","seven","eight","nine","ten","jack","queen","king")
list_of_suites=("hearts","spades","diamonds","clubs")
num_of_val=len(list_of_values)
num_of_suites=len(list_of_suites)
list_of_cards = []
for p in list_of_suites:
    for q in list_of_values:
        cardd=(q+" of "+p)
        list_of_cards.extend(cardd)

    							
