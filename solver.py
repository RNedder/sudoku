def find_next_empty(grid):
    # finds the next row, col on the grid that's not filled yet --> rep with 0
    # return row, col tuple (or (None, None) if there is none)

    #keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c

    return None, None #if no spaces in the grid are left

def is_valid(grid, guess, row, col):
    #figures out whether the guess at the row/col of the grid is a valid guess
    #returns True if is valid, False otherwise

    #let's start with the row:
    row_vals = grid[row]
    if guess in row_vals:
        return False
    
    #now the column
    col_vals = []
    for i in range(9):
        col_vals.append(grid[i][col])
    if guess in col_vals:
        return False
    # col_vals = [grid[i][col]] for i in range(9) ALTERNATIVE CODE

    #and then the 3x3 Square
    #this is tricky, but we want to get where the 3x3 square starts
    #and iterate over the 3 values in the row/column 
    #gets which of the 9 3x3 squares you are in
    row_start = (row // 3) * 3  #1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3 

    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start):
            if grid[r][c] == guess:
                return False
            
    #if we get here, these checks pass
    return True

def solve_sudoku(grid):
    # solve sudoku using backtracking
    # our grid is a list of lists, where each inner list is a row in our sudoku grid
    # return whether a solution exists
    # mutates puzzl;e to be the solution (if solution exists)

    #step 1: choose a spot on the grid to make a guess
    row, col = find_next_empty(grid)

    #step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    #step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): #range(1,10) is 1, 2, 3, ... 9
        #step 3: check if this is a valid guess
        if is_valid(grid, guess, row, col):
            #step 3.1: if this is valid, then place that guess on the grid!
            grid[row][col] = guess
            #now recurse using this grid!
            #step 4: recursively call our function
            if solve_sudoku(grid):
                return True
            
        #step 5: if not valid OR if our guess does not solve the grid, then we need to backtrack and try a new number
        grid[row][col] = 0 #reset the guess

    #step 6: if none of the numbers that we try work, then the grid is unsolveable 
    return False