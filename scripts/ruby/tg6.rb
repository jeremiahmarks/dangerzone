#!/usr/bin/ruby
# @Author: jeremiah.marks
# @Date:   2015-02-10 14:40:29
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-02-10 14:41:08


def foo(str: "foo", num: 424242)
  [str, num]
end

foo(num: 123)