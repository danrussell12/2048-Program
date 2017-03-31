
#import stuff, libraries etc. functions?
import numpy as np
import random as rand


#set-up board for gameplay 
board = np.zeros((4,4)) # set initial board matrix of zeros

row = rand.randint(0,3) #generate random number for row
col = rand.randint(0,3) #generate random num for column

val = rand.randint(1,10) #rand num to put in
if (val == 10): #10% chance of getting a 4
    val = 4
else:
    val = 2

board[row,col] = val #set the random board space to the random value
     

#find empty spaces and store in matrix     
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

