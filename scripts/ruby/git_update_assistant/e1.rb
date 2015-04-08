#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-03-16 22:50:24
# @Last Modified 2015-04-07
# @Last Modified time: 2015-04-07 19:39:32


gitsFinder = %x( find ~/ -name ".git" 2>/dev/null )
# gitsFinder = %x[ #{cmd} ]

# value = %x( echo 'hi' )
# value = %x[ #{cmd} ]

gits=gitsFinder.split("\n")


gits.each do |changeDir|
    cmd = "cd " + changeDir + " 2>/dev/null && pwd"
    puts %x[ #{cmd} ]
end

