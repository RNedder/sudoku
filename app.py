import copy, random
from sudoku_pkg.puzzle import display_game, is_valid, generate_puzzle

#Use Dictionary - each key is a row and each value is a list of 1-9
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


#Randomize each row by iterating through each number and checking that it does not duplicate on the column or row
#Final check for the row
#If there are no duplications, move on to the next row, if there are, change the duplicate in the row, repeat


generate_puzzle(grid)
display_game(grid)