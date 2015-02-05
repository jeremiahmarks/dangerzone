#!/bin/bash

#from
    # http://stackoverflow.com/questions/11279423/bash-getopts-with-multiple-and-mandatory-options

# You can concatenate the options you provide and getopts will separate them. 
# In your case statement you will handle each option individually.

# You can set a flag when options are seen and check to make sure mandatory 
# "options" (!) are present after the getopts loop has completed.

# Here is an example:



rflag=false
small_r=false
big_r=false

usage () { echo "How to use"; }

options=':ij:rRvh'
while getopts $options option
do
    case $option in
        i  ) i_func;;
        j  ) j_arg=$OPTARG;;
        r  ) rflag=true; small_r=true;;
        R  ) rflag=true; big_r=true;;
        v  ) v_func; other_func;;
        h  ) usage; exit;;
        \? ) echo "Unknown option: -$OPTARG" >&2; exit 1;;
        :  ) echo "Missing option argument for -$OPTARG" >&2; exit 1;;
        *  ) echo "Unimplemented option: -$OPTARG" >&2; exit 1;;
    esac
done

shift $(($OPTIND - 1))

if ! $rflag && [[ -d $1 ]]
then
    echo "-r or -R must be included when a directory is specified" >&2
    exit 1
fi

# from http://rsalveti.wordpress.com/2007/04/03/bash-parsing-arguments-with-getopts/

# This is an import point of getopts. You can use ":" in two cases, one when you
#  want getopts to deal with argument's errors, and another to tell getopts which 
#  argument needs a value.

# First, the error checking. When you pass the arguments to getopts in the 
# optstring, getopts will only check what's there, so if you pass an argument 
# that's not listed at optstring getopts will give an error (because it's not a 
# valid argument). When you put ":" at the beginning of the optstring, 
# ":ht:r:p:v" for example, getopts sets the OPTION var with "?" and the $OPTARG 
# with the wrong character, but no output will be written to standard error; 
# otherwise, the shell variable $OPTARG will be unset and a diagnostic message 
# will be written to standard error (./test_script.sh: illegal option -- l, if 
# you pass the argument -l, for example).

# Second, how to tell getopts which argument needs a value. When you need an 
# argument that needs a value, "-t test1" for example, you put the ":" right 
# after the argument in the optstring. If your var is just a flag, withou any 
# additional argument, just leave the var, without the ":" following it.