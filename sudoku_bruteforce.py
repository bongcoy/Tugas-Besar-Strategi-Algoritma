from general_function import *
 
# Program utama
def sudoku_bruteforce(grid, row, col):
   
    # Rekursif berhenti jika mencapai batas maks
    if (row == NMAX - 1 and col == NMAX):
        return True
       
    # Jika kolom bernilai 9, 
    # maka lanjut baris selanjutnya
    # dan kolom bernilai 0
    if col == NMAX:
        row += 1
        col = 0
 
    # Cek jika num tidak 0,
    # maka lanjut ke kolom selanjutnya
    if grid[row][col] != 0:
        return sudoku_bruteforce(grid, row, col + 1)

    # Cek angka 1 sampai 9 pada masing2 sel
    for num in range(1, NMAX+1): # NMAX+1 karena exclude
       
        # Jika angka safe, maka masukkan ke dalam sel
        if (is_safe(grid, row, col, num)):
           
            # Masukkan angka ke dalam sel
            grid[row][col] = num
 
            # Rekursif untuk cek kembali pada 
            # kolom selanjutnya
            if (sudoku_bruteforce(grid, row, col + 1)):
                return True
 
        # Jika belum true, maka sel menjadi 0 kembali
        grid[row][col] = 0

    # Jika loop tidak menghasilkan true, maka backtrack
    return False