def is_valid(gird, number, row, col):

    row_vals = grid[row]
    if number in row_vals:
        return False
    
    col_vals = []
    for i in range(9):
        col_vals.append(grid[i][col])
    if number in col_vals:
        return False
    
    