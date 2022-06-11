from sudo_backtrack import *

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