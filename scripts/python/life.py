#!/usr/bin/env python
from numpy import *
import sys
import math

# compute next generation of conway's game of life
def next_generation( current, next ) :
    next[:,:] = 0 # zero out next board
    # bound examination area
    bend0 = (current.shape[0]-3)+1
    bend1 = (current.shape[1]-3)+1
    for i in xrange( bend0 ) :
        for j in xrange( bend1 ) :
            neighbours = sum( current[i:i+3, j:j+3] )
            if current[i+1, j+1] == 1 :
                neighbours -= 1 # do not count yourself
                if 2 <= neighbours <= 3 :
                    next[i+1, j+1] = 1
            else:
                if neighbours == 3 :
                    next[i+1,j+1] = 1

if len(sys.argv) != 3 :
    print "usage:", sys.argv[0], "init-board generations"
    sys.exit( 1 )

init = sys.argv[1]
generations = int( sys.argv[2] )

board_sz = math.ceil( math.sqrt(len(init)) ) 

# board_sz+2 includes the border of zeros
board = zeros( (board_sz+2,board_sz+2), uint8)
next_board = zeros_like( board ) # same shape

# fill the board
i = 0
j = 0
for index,ch in enumerate(init) :
    if ch == '1' :
        board[i+1,j+1] = 1
    j = (j+1) % board_sz
    if ((index+1) % board_sz) == 0 : i += 1

for gen in xrange(generations) :
    next_generation( board, next_board )
    board, next_board = next_board, board # swap boards
    print board[1:-1,1:-1] # do not print the border

