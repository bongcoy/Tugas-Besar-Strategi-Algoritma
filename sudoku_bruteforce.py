# Ukuran matriks N * N
N = 9
 
# Cek safe atau tidak
# Safe = Num tidak terpakai di row, column, dan box 3x3
def is_safe(grid, row, col, num):
   
    # Cek sudah terpakai di baris ke-row atau tidak
    # Jika sudah, maka return False
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # Cek sudah terpakai di kolom ke-col atau tidak
    # Jika sudah, maka return False
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # Cek sudah terpakai di box 3x3 atau tidak
    # Jika sudah, maka return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSudoku(grid, row, col):
   
    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
        return True
       
    # Check if column value  becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0
 
    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):
       
        # Check if it is safe to place
        # the num (1-9)  in the
        # given row ,col  ->we
        # move to next column
        if is_safe(grid, row, col, num):
           
            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            grid[row][col] = num
 
            # Checking for next possibility with next
            # column
            if solveSudoku(grid, row, col + 1):
                return True
 
        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        grid[row][col] = 0
    return False
 
if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("no solution  exists ")