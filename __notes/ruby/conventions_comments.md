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

###global variables

$this_is_a_global_var

###class variables

@@this_variable_can_be_accessed_in_the_class

###instance variables

@this_is_an_instance_var

###class methods

Inside of a class if you define a method like this

	def self.awesome_method
		puts "something"
	end

that method is accessable from the class, not from individual instances of that class.