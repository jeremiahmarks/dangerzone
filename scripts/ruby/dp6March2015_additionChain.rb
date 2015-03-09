#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-03-08 18:16:46
# @Last Modified 2015-03-08>
# @Last Modified time: 2015-03-08 18:23:24


class numChain

    def initialize(val1, chainLength)
        @firstValue=val1
        @chainLength = chainLength
        @numberChain = Array.new(chainLength) { iii }
