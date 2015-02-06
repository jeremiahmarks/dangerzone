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