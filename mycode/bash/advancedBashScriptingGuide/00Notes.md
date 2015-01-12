# ######################################### #
# #File by Jeremiah Marks#

#Notes from Advanced Bash Scripting Guide

##Ch 3
    * Special Chars
        - #
            + Comments
        - ;
            + Command separator
            + Requires no space before and one space after
                * echo hello; echo there
        - ;;
            + Terminator in a case option
                * example:                 
                    case "$variable" in
                        abc) echo "\$variable = abc" ;;
                        xyz) echo "\$variable = xyz" ;;
                    esac
        - .
            + Source
                * example: 
                    #!/bin/bash
                    #  Note that this example must be invoked with bash, i.e., bash ex38.sh
                    #+ not  sh ex38.sh !
                    . data-file    # Load a data file.
            + Component of a file name 
                * hidden files and folders
                * relative path/cwd
                * regular expressions (regex) matches a single character
        - "
            + Partial quoting - preserves most special characters
        - '
            + Full quoting - preserves all special characters
        - ,
            + Comma Operator
                * links together a series of arithmetic operations. 
                    - All evaluated, only last returned
                        + example:
                            let "t2=((a=9, 15 / 3))"
                            # Set a=9 amd t2=15/3
                * concat strings
                    - example:
                        for file in /{,usr/}bin/*calc
                        # checks in /bin and /usr/bin
        - ,, ,
            + Lowercase conversion
                * in searches , is one lowercase character [first char], ,, is all letters lowercase
        - \
            + Escape
        - `
            + Command substution
        - :
            + null command
                * synonomis with 'true' 
            + Provide a placeholder where a binary operation is expected
            + Provide a placeholder where a command is expected in a here document.