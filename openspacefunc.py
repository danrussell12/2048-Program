#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:08:02 2017

@author: danrussell
"""

## Function: find open spaces, print out matrix with list of indices of open
#spaces, and choose one at random

#input: 4x4 matrix of board with values in each location - 'board'
#output: the indices in 1x2 mat of the space in board to put the
# next number - 'newnum'

M = 4                               #x length for loop 
N = 4                               #y length for loop
count = 0                           #initialize counter
open = np.zeros((16,2))             #initialize open spaces mat
for i in range(M):                  #iterate through x
    for j in range(N):              #iterate through y
        if (board[i,j] == 0):       #check if space is empty
            open[count,0] = i       #assign col 0 to x index #can I put these together somehow?
            open[count,1] = j       #assign col 1 to y index
            count = count + 1       #iterate through spaces in open mat
open = open[0:count,:]              #ditch leftover 0,0 vals at end of mat

randnum = rand.randint(0,count-1)   #generate random number to choose indices

newnum = open[randnum,:]            #put indices in a matrix

