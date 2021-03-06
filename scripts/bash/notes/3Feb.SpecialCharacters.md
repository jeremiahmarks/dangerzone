

##Notes

" vs '
	Basically double quotes will allow you to replace special characters.  Single quotes will preserve every special char.

, 
	The comma operator links together a series of arithmetic operations. All are evaluated, but only the last one is returned.
	EXAMPLE
		let "t2 = ((a = 9, 15 / 3))"
		# Set "a = 9" and "t2 = 15 / 3"
	The comma operator can also concatenate strings.
	EXAMPLE
		for file in /{,usr/}bin/*calc
		#             ^    Find all executable files ending in "calc"
		#+                 in /bin and /usr/bin directories.
`
	command substitution. The `command` construct makes available the output of command for assignment to a variable. This is also known as backquotes or backticks.
:
	null command [colon]. This is the shell equivalent of a "NOP" (no op, a do-nothing operation). It may be considered a synonym for the shell builtin true.
:>
	truncates a file to zero length, without changing its permissions. If the file did not previously exist, creates it.
		: > data.xxx   # File "data.xxx" now empty.
		# Same effect as   cat /dev/null >data.xxx
		# However, this does not fork a new process, since ":" is a builtin.
?
	test operator. Within certain expressions, the ? indicates a test for a condition.
	In a double-parentheses construct, the ? can serve as an element of a C-style trinary operator.
	EXAMPLE
		(( var0 = var1<98?9:21 ))
		#                ^ ^

		# if [ "$var1" -lt 98 ]
		# then
		#   var0=9
		# else
		#   var0=21
		# fi
? 
	single character wild card
${parameter}
	Same as $parameter, i.e., value of the variable parameter. In certain contexts, only the less ambiguous ${parameter} form works.
	EXAMPLE
		your_id=${USER}-on-${HOSTNAME}
		echo "$your_id"
		#
		echo "Old \$PATH = $PATH"
		PATH=${PATH}:/opt/bin  # Add /opt/bin to $PATH for duration of script.
		echo "New \$PATH = $PATH"

$?
        exit status variable. The $? variable holds the exit status of a command, a function, or of the script itself.

$$
    process ID variable. The $$ variable holds the process ID [4] of the script in which it appears.

()
    command group A listing of commands within parentheses starts a subshell.
E   EXAMPLE
        a=123
        ( a=321; )        
        echo "a = $a"   # a = 123
        # "a" within parentheses acts like a local variable.
    
    array initialization
E   EXAMPLE
        Array=(element1 element2 element3)

{}
    Brace expansion
    No spaces allowed within the braces unless the spaces are quoted or escaped.
E   EXAMPLE
        echo \"{These,words,are,quoted}\"   # " prefix and suffix
        # "These" "words" "are" "quoted"

        cat {file1,file2,file3} > combined_file
        # Concatenates the files file1, file2, and file3 into combined_file.

        cp file22.{txt,backup}
        # Copies "file22.txt" to "file22.backup"
    Block of code [curly brackets]. 
        Also referred to as an inline group, this construct, in effect, creates an anonymous 
        function (a function without a name). 
        However, unlike in a "standard" function, the variables inside a code block remain visible to 
        the remainder of the script.

(( ))
    integer expansion.
    Expand and evaluate integer expression between (( )).


{a..z}
    Extended Brace expansion.
        
        echo {a..z} # a b c d e f g h i j k l m n o p q r s t u v w x y z
        # Echoes characters between a and z.
        echo {0..3} # 0 1 2 3
        # Echoes characters between 0 and 3.