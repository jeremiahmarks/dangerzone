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

###how to convert a hash that uses strings as keys to a hash that uses symbols as keys

EXAMPLE
    hash_with_strings.each do |key|
        hash_with_symbols[key.to_sym] = hash_with_strings.delete(key)
    end

###Access a nested hashs elements
Assume that you have a hash this_hash[:keyname] = { thiskey: "val1", thatkey: "val2" }
you could access val1 with
    this_hash[:keyname][:thiskey]


###Remove an element from array by value
    >a=[1,2,4,5,6,7,3,9]
    => [1, 2, 4, 5, 3, 7]
    >a.delete(3)
    => 3
    >a
    => [1, 2, 4, 5, 7]