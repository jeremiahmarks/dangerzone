
#Basic commands - Common Functions - how tos - other conventions and notes


##Commands
###puts 
displays to screen and inserts a new line
###gets
gets the most recent input the user typed in
###print 
displays to screen and does not put new line
###false
you know, not true
###if/elsif/else/end
I already miss elif, and I am not sure how I feel about end either.
EXAMPLE

    if brackets == 0 && colons == 0
        puts "IsRuby"
        variable_naming_convention = "_"
    elsif multiline_comments == "=begin" && "=end"
        =begin
        when the else function evaluates before it's variables
         can be set in every case, I hope that it errors when 
         loading it in irb
        The guards of the multiline comment may not be mentioned
         by name when you are between them, or anarchy will reign.
        =end
        puts "StillRuby"
        variable_naming_convention = "_"
    else
        puts "You guessed it, still ruby!"
        variable_naming_convention = "_"
    end

    if wants_another_round
        puts "Never gonna give you up!"
        puts "Yep, still ruby!"
        variable_naming_convention = "_"
seriously, I should have probably just written a section about comments.
###Comments
* single line
    - #
        + # This would be a comment
* multiline
    - =start && =end
        + =start
        + All three of these lines would be comments
        + =end

###break
exit the parent loop

###arrays
* creation
    - variableName = ["apple", apple_color, "pie"]
    - variableName = Array.new(7, 'seven of these in one array')

###next
moves to next item in iterable






##Common Functions
* string.length
    - interger value
* string.reverse
    - esrever.gnirts
* "string" *2
    - "stringstring"
* Int.next
    - Int + 1
* Int.pred
    - Int - 1
* gets.chomp
    - gets the users most recnet input and cleans it up by removing generally unwanted trash in the stream
* array.each
    - iterates through the values of the array. often times used with do to make for/each loop.
* array.include?
    - returns bool whether the value is stored in the array.
* array.first
    - whatever element is at position 0
* array.last
    - last element of an array
* array.empty?
    - returns if there are no values in the array
* array.length
    - number of elements in array
* array.shift
    - returns and removes the first element of the array
* array.pop
    - returns and removes the last element of an array
* array.push(object)
    - appends object to the last item of the array
* array.unshift(object)
    - appends object to first spot in array
* array.insert(location, object)
    - inserts objenct to the locationth place in the array
    - 

###loop control
####while
    while sum_function_that_returns_bool?
        do something cool
    end

####until
the example in the book is actually really good, it if from the perspective of a control method from a train dont use `while !at_stop?` because it is ugly and takes a moment to process, use `until at_stop?`

####for in

    for item in array_of_values
        puts item
    end
Can also be done by

    array_of_values.each do |item|
        puts item
    end
Since it is a one line thing, it can also be done like this:

    array_of_values.each{ |item| puts item }








##How-Tos
###how to insert variable value into screen
* must use double quotes
* must also have some funny @{varname} part
    - Heck yeah, it was @{varname}

###how to access files from InteractiveRuBy
1. open command prompt
2. navigate to folder where file is located
    a. I know that there is a better way, I just haven't seen it yet
3. run irb
4. """load 'filename.rb'"""

###how to stop a loop
1. break



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



