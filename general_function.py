# Ukuran matriks N * N
NMAX = 9

# Cek sudah terpakai di baris ke-row atau tidak
def used_in_row(grid, row, num):
    for i in range(9):
        if(grid[row][i] == num):
            return True
    return False

# Cek sudah terpakai di kolom ke-col atau tidak
def used_in_col(grid, col, num):
    for i in range(9):
        if(grid[i][col] == num):
            return True
    return False

# Cek sudah terpakai di box 3x3 atau tidak
def used_in_box(grid, row, col, num):
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if(grid[i + startRow][j + startCol] == num):
                return True
    return False

# Cek safe atau tidak
# Safe = Num tidak terpakai di row, column, dan box 3x3
def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row, col, num)

    # Print array 2D untuk membentuk sebuah Grid
def print_grid(grid):
    for row in range(len(grid)):
        if row == 0 or row == 3 or row == 6:
            print("-------------------------")
        for col in range(len(grid[row])):
            if col == 0 or col == 3 or col ==6:
                print("| ", end = "")
            if grid[row][col] != 0:
                print(grid[row][col], end = " ")
            else:
                print(end = "  ")
            if col == 8:
                print("|")
    print("-------------------------")