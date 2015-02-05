wordss=open('words.txt')
matching_words={}
do_matching_words={}
words_without_letters={}
do_words_without_letters={}
alphabet=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


def no_e(word):
    for letter in word:
        if letter == 'e':
            return
    return word

def check_dict():
    #matching_words=[]
    for i in range (100):
        line=wordss.readline()
        cword=line.strip()
        passer=no_e(cword)
        if passer==None:
            pass
        else:
            matching_words.append(passer)

    print matching_words

def nolet(word,outcast):
    for letter in word:
        for char in outcast:
            if letter == char:
                return
    return word

def dolet(word,outcast):
    for letter in word:
        for char in outcast:
            if letter == char:
                return word
    return None



def heck_dict(): #this is the function that builds the list
    #matching_words=[]
    #bad=raw_input('please input undesired letters')
    for line in wordss:
        for bad in alphabet:
            cword=line.strip()
            passer=nolet(cword,bad)
            if passer==None:
                pass
            else:
                if passer not in matching_words:
                    matching_words[passer]=bad
                else:
                    matching_words[passer]+=bad
                if bad not in words_without_letters:
                    words_without_letters[bad]=[(passer)]
                else:
                     words_without_letters[bad]+=[(passer)]
    #print matching_words

def listoletters(word):
    listed=matching_words[word]
    for letter in listed:
        print (letter+" is not in "+word) 

def wordswithout(letter):
    listed=words_without_letters[letter]
    for word in listed:
        print (word+" does not have "+letter)

def wordswith(letters):
    for line in wordss:
        for bad in alphabet:
            cword=line.strip()
            passer=dolet(cword,bad)###
            if passer==None:
                pass
            else:
                if passer not in do_matching_words:###do_
                    do_matching_words[passer]=bad###do_
                else:
                    do_matching_words[passer]+=bad###do_
                if bad not in do_words_without_letters:###
                    do_words_without_letters[bad]=[(passer)]
                else:
                     do_words_without_letters[bad]+=[(passer)]


#def timesave():
#def timeload():
