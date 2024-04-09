# Displays the grid
def display_game(grid):
    for row in grid:
        clean_print = '  '.join(str(col) for col in row)
        print(clean_print)

#checks whether the number already appears in the row or col
def is_valid(grid, number, row, col):
    row_vals = grid[row]
    col_vals = []
    for i in range(9):
        col_vals.append(grid[i][col])
    if number not in row_vals and number not in col_vals:
        return True
    else:
        return False
    
# Generates a puzzle by randomly selecting integers 1-9 for each square
def generate_puzzle(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                while True:
                    #generates number 1-9
                    number = random.randint(1,9)
                    #runs the is_valid function to check if the number is valid
                    if is_valid(grid, number, row, col):
                        grid[row][col] = number
                    #repeats the while loop if the number is not valid
                    else:
                        continue