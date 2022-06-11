import time

# Print array 2D untuk membentuk sebuah Grid
def print_grid(grid):
    # for row in range(9):
    #     for col in range(9):
    #         print(grid[row][col], end=" ")
    #     print("n")

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

# Mencari elemen array yang bisa direplace (saat elemen bernilai 0)
def is_empty_exist(arr, l):
    # TODO: Ini bisa diganti pake return 2 values, kalo ga ketemu maka return -1, -1
    #       return row, column kalo ketemu
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

# Cek sudah terpakai di baris ke-row atau tidak
def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

# Cek sudah terpakai di kolom ke-col atau tidak
def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

# Cek sudah terpakai di box 3x3 atau tidak
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False

# Cek safe atau tidak
# Safe = Num tidak terpakai di row, column, dan box 3x3
def is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)

# Program utama
def solve_sudoku(arr):

    # List untuk menyimpan angka yang dapat diisi (saat num = 0)
    l = [0, 0]

    # Iterasi untuk mencari elemen yang kosong,
    # Jika tidak ada, maka return True
    if(not is_empty_exist(arr, l)):
        return True

    # Jika ada elemen kosong, maka masukkan ke variable row & col
    row = l[0]
    col = l[1]
    
    # Cek angka 1 sampai 9 pada masing2 sel
    for num in range(1, 10):
        
        # Jika angka safe, maka masukkan ke dalam sel
        if(is_safe(arr, row, col, num)):

            # Masukkan angka ke dalam sel
            arr[row][col]= num

            # Rekursif untuk cek kembali pada 
            # elemen kosong selanjutnya
            if(solve_sudoku(arr)):
                return True

            # Jika tidak safe, maka sel menjadi 0 kembali
            arr[row][col] = 0

    # Jika loop tidak menghasilkan true, maka backtrack
    return False 

if __name__=="__main__":
    start_time = time.time()
        
    # Array 2D atau Grid yang akan dipakai
    grid =[[0 for x in range(9)]for y in range(9)]
    
    # Nilai awal Grid
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    print("Grid awal kamu :")
    print_grid(grid)
    print()

    # Jika sukses, maka print Grid
    print("Hasilnya adalah :")
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print("No solution exists")

    print("\nProgram berjalan selama: %.4f seconds" %(time.time() - start_time))
