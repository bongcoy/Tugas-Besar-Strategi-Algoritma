# Mencari elemen grid yang bisa direplace (saat elemen bernilai 0)
def is_empty_exist(grid, l):
    for row in range(9):
        for col in range(9):
            if(grid[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

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
    for i in range(3):
        for j in range(3):
            if(grid[i + row][j + col] == num):
                return True
    return False

# Cek safe atau tidak
# Safe = Num tidak terpakai di row, column, dan box 3x3
def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row - row % 3, col - col % 3, num)

# Program utama
def solve_sudoku(grid):

    # List untuk menyimpan angka yang dapat diisi (saat num = 0)
    l = [0, 0]

    # Iterasi untuk mencari elemen yang kosong,
    # Jika tidak ada, maka return True
    if(not is_empty_exist(grid, l)):
        return True

    # Jika ada elemen kosong, maka masukkan ke variable row & col
    row = l[0]
    col = l[1]
    
    # Cek angka 1 sampai 9 pada masing2 sel
    for num in range(1, 10):
        
        # Jika angka safe, maka masukkan ke dalam sel
        if(is_safe(grid, row, col, num)):

            # Masukkan angka ke dalam sel
            grid[row][col]= num

            # Rekursif untuk cek kembali pada 
            # elemen kosong selanjutnya
            if(solve_sudoku(grid)):
                return True

            # Jika tidak safe, maka sel menjadi 0 kembali
            grid[row][col] = 0

    # Jika loop tidak menghasilkan true, maka backtrack
    return False 
