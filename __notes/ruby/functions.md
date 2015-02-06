##functions

###Basic creation
* functions are created with def
* functions are ended with end

###Splat parameters
In the parameters function of the method you can tell it that you may pass it more than just the listed variables.
EXAMPLE

    def splat_params(*things_to_say)
        puts things_to_say
    end

    splat_params("This will be said", 'so will this', 'and this as well')

###Returns
Since the last thing that appears in your method body is likely what you want to return, unless otherwise specified it will return the last part of the method body
EXAMPLE

    def add(a,b)
        return a+b
    end

is the exact same as

    def add(a,b)
        a+b
    end

