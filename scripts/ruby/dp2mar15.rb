#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-03-08 16:23:57
# @Last Modified 2015-03-08
# @Last Modified time: 2015-03-08 17:14:33

############################################################
##
##  From http://redd.it/2xoxum
##
##  find the given subsctring in the full play of macbeth
##
############################################################

# puts File.read('macbeth.txt').split(/[A-Z]\.\n|\n\n/).find { |x| x.include? "Eye of newt" }

def findLine(words)
    # This is the cheating way of doing it, I totally stole this soluction 
    puts File.read('macbeth.txt').split(/[A-Z]\.\n|\n\n/).find { |x| x.include? words }
end
# findLine("Eye of newt")

def evalAndReturn(thisString, soliSoFar)
    startVal=''
    unless soliSoFar==''
        startVal << soliSoFar
    end
    if thisString[0,4]=='    '
        soliSoFar << thisString
    else
        soliSoFar=''
    end
    return soliSoFar, startVal
end

def myAttempt(words)
    these_words=''
    found=false
    macText = File.read('macbeth.txt')
    macText.each_line do |line|
        if line.include? words
            found=true
        end
        these_words, oldphrase = evalAndReturn(line, these_words)
        if these_words=='' && found
            puts oldphrase
            break
        end
    end
end
myAttempt("Eye of newt")
puts "\n"*3
myAttempt("tied me to a stake")