
def apple()
    puts "can access"
end

def splat_params(*things_to_say)
    puts things_to_say
end

def do_the_thing()
	splat_params("This will be said", 'so will this', 'and this as well')
end

def block_method
	yield
end

def bm2
	yield
	puts "apple \n\n"
	yield
end

def block_test
	block_method { puts "red" }
end

def bt2
	bm2 { puts "red" }
end