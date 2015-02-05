from grams import getwords, checkLetters

def grams(originalstring, listofwords, starterphrase=''):
    
    listofphrases = []
    
    for word in listofwords:
        thisphrase=starterphrase+word+' '
        templist=[]
        tempstring=originalstring
        for letter in word:
            tempstring=tempstring.replace(letter, '',1)
        for eachword in listofwords:
            if checkLetters(tempstring, eachword):
                templist.append(eachword)
        if len(templist)==0:
            listofphrases.append(thisphrase)
            continue
        else:
            listofphrases.extend(grams(tempstring, templist, thisphrase))
            
    return listofphrases
    

object deruzzle():

    def __init__(ruzzlestring):
        """ The ruzzlestring is the 16 letters that are on a ruzzleboard
            with color modifiers in the style of a_red_. and example ruzzleboard
            board would be entered as such: pn_yellow_reei_blue_ama_red_e_green_i_yellow_seslt
            
            p    n_y_ r    e
            e    i_b_ a    m
            a_r_ e_g_ i_y_ s
            e    s    l    t
        """
        while not(len(ruzzlestring)==0):
             
