####################################################################################################
##                                                                                                ##
##                                                                                                ##
##                         Applicant Name:    Jeremiah Marks                                      ##
##                  Position Applying for:    Jr. Systems Administrator                           ##
## Stated Requirements for script success:    Given a test file containing lines of words such as ##
##   (abc, abb, abd, abb, etc), write a script that prints, in order of frequency, how many times ##
##   each word appears in the file                                                                ##
##                                                                                                ##
##                                                                                                ##
####################################################################################################



####################################################################################################
##                                                                                                ##
##                                                                                                ##
##              Important Note:                                                                   ##
##                                                                                                ##
##    In case it does not become painfully obvious through the course of this series of scripts   ##
##      most of my experience is either hacking with Python or school programs with Java. I am    ##
##      approaching this series of scripts with the idea that you are seeking someone with the    ##
##      core skills and are willing to help train them.                                           ##
##                                                                                                ##
##    What I am saying is I intend to provide a fair representation of my skills rather than only ##
##      presenting my most production ready code. I feel that it is only fair that you and I both ##
##      are firmly aware of my strengths and my weaknesses.                                       ##
##                                                                                                ##
##    That coupled with the fact that I have no idea what production ready code would even look   ##
##      like will probably become pretty obvious, but I wanted to warn you anyways. Thank you!    ##
##                                                                                                ##
####################################################################################################       

WORDFILE = '/home/jeremiah/Desktop/words.txt'


def firstAttack():
  """
  The firstAttack method is my first, naive walkthrough of the looping required.
  I am probably going a little overboard with since I will be attempting to cover a couple of
  different scenarios regarding the way the file is set up, but better safe than sorry, esp
  when applying for a job.
  
  """
  
  # I have always been told to start with an algorithm, so here it is: 
  
  # open file on my desktop
  # load each line into a list
  # parse each line for words. for each word:
  #     Check if the word is in the dictionary
  #     If not, add the word and the number 1 as an entry
  #     If it is simply add one to the number of occurences  
  #         (I remember having a bad time with this approach before, but that was when I was first 
  #          learning about dictionaries and I hope that I won't do some silly thing I did then)
  #     Export the dictionary and sort it using the fruit bowl method
  #       mention knowledge on sorting
  #     display all of the items sorted
  
  
  #   If I can get this, I will only be details away from adding the parts of the application that 
  #     new to me
  
  
  listOfLines=[]
  rankings=[]
  #I am including two data structures because I want to cover the possability that the words will 
  #be on lines as stated or whether they will be delimited by comas as appears in my inbox
  #if this where anything EXCEPT a interview type question, though, please know that I would 
  #ask that question directly before starting to write. 
  
  wordFile=open(WORDFILE,'r+')
  
  for line in wordFile:
    for word in line.split(',')
      listOfLines.append([word.strip(),])
    #This for loop ensures that all of the lines in the file are removed. That means that I will need
    #to check for delimiters and build my dictionary. 
    #
    #Basically this combination of for loops treats the file as a two dimensional array. 
    #It is not very pythonic, but it is the fastest method I can think of right now
    #
    # I just changed line 76 from .append(word.strip()) to ([word.strip(),]) to set up to
    # len each words list
    
    
  listOfLines.sort()
  
  for word in listOfLines:
    rankings.append[listOfLines.count(word), word]
    
    while word in listOfLines:
      listOfLines.remove(word)
      
  #This for while loop set takes the zeroth word in the list, counts how many times it is in the list, 
  #Then updates the rankings, currently unsorted.
  #After that it removes all traces of the word from the list and moves on to the next word
  
  rankings.sort()
  
  for item in rankings:
    print(item[0],item[1])
    
  
