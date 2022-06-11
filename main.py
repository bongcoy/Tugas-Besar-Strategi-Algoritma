from sudo_backtrack import *

import time

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

def solve(grid_variant):
    # Jika sukses, maka print Grid
    print("Hasilnya adalah :")

    start_time = time.time()
    
    if(solve_sudoku(grid_variant)):
        print_grid(grid_variant)
    else:
        print("No solution exists")

    print("\nProgram berjalan selama: %.4f seconds" %(time.time() - start_time))

def main():    
    # Macam-macam jumlah clue dalam Grid
    grid32 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # grid20 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #         [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #         [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #         [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #         [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #         [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # grid17 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #         [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #         [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #         [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #         [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #         [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # Set nilai awal Grid
    grid = grid32

    print("Grid awal kamu :")
    print_grid(grid)
    print()

    solve(grid)

if __name__=="__main__":
    main()