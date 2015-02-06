##Conventions and comments
(because there are tons of things... I am still not sure about spaces vs tabs!)

###?
indicates that a method returns a boolean value. [Source](http://stackoverflow.com/questions/1345843/ruby-question-mark-usage)

###next if
when iterating through an array, if the condition evaluates as true it iterates.
EXAMPLE:  
    
    test = [1, 2, 3, 4]
    for value in test
        next if value%2 == 0
        puts value
    end

OUTPUT    

    1
    3
    => true



