#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-02-05 22:51:46
# @Last Modified 2015-02-05
# @Last Modified time: 2015-02-05 22:57:15

sample_array = ["a", "b", "c", "d", "e", "f"]

sample_array.each do |sstop|
	next if sstop == "b"
	puts sstop
	break if sstop == "c"
end