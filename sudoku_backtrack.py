from general_function import *

# Mencari elemen grid yang bisa direplace (saat elemen bernilai 0)
def is_empty_exist(grid, l):
    for row in range(9):
        for col in range(9):
            if(grid[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

# Program utama
def sudoku_backtrack(grid):

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
            if(sudoku_backtrack(grid)):
                return True

            # Jika belum true, maka sel menjadi 0 kembali
            grid[row][col] = 0

    # Jika loop tidak menghasilkan true, maka backtrack
    return False 
