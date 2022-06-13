from sudoku_bruteforce import *
from sudoku_backtrack import *

import time

def solve_backtrack(grid_variant):
    # Jika sukses, maka print Grid
    print("Hasilnya adalah :")

    start_time = time.time()
    
    if(sudoku_backtrack(grid_variant)):
        print_grid(grid_variant)
    else:
        print("No solution exists")

    print("\nProgram berjalan selama: %.5f seconds" %(time.time() - start_time))

def solve_bruteforce(grid_variant):
    # Jika sukses, maka print Grid
    print("Hasilnya adalah :")

    start_time = time.time()

    if (sudoku_bruteforce(grid_variant, 0, 0)):
        print_grid(grid_variant)
    else:
        print("No solution  exists")

    print("\nProgram berjalan selama: %.5f seconds" %(time.time() - start_time))


def main():
    # Macam-macam jumlah clue dalam Grid
    grid76 = [[6, 3, 0, 1, 4, 5, 7, 9, 8],
            [1, 7, 5, 2, 8, 9, 0, 6, 4],
            [0, 4, 9, 6, 7, 3, 1, 5, 2],
            [2, 1, 4, 7, 5, 8, 9, 3, 6],
            [9, 6, 8, 3, 1, 4, 0, 2, 7],
            [3, 5, 7, 0, 6, 2, 4, 8, 1],
            [7, 2, 3, 4, 9, 6, 8, 1, 5],
            [5, 9, 1, 8, 2, 7, 6, 4, 3],
            [4, 8, 6, 5, 3, 1, 2, 7, 9]]

    grid60 = [[1, 0, 8, 0, 7, 4, 0, 9, 5],
            [0, 9, 0, 1, 8, 2, 3, 0, 4],
            [0, 7, 3, 5, 9, 0, 1, 8, 2],
            [0, 5, 0, 7, 4, 3, 8, 1, 6],
            [3, 0, 4, 2, 6, 1, 9, 0, 7],
            [7, 6, 1, 9, 0, 8, 4, 2, 3],
            [0, 0, 7, 8, 2, 9, 0, 0, 1],
            [8, 0, 5, 4, 3, 7, 2, 0, 9],
            [9, 3, 2, 6, 0, 0, 7, 4, 8]]

    grid44 = [[0, 7, 3, 4, 0, 0, 6, 0, 8],
            [6, 8, 2, 3, 7, 9, 0, 0, 1],
            [0, 5, 4, 8, 0, 1, 2, 0, 3],
            [0, 1, 6, 2, 9, 0, 0, 0, 7],
            [0, 3, 0, 0, 4, 0, 9, 0, 2],
            [0, 0, 9, 0, 5, 7, 0, 4, 6],
            [0, 0, 5, 0, 1, 0, 8, 0, 9],
            [3, 4, 1, 0, 0, 2, 7, 0, 5],
            [0, 0, 0, 0, 3, 0, 0, 0, 4]]

    grid28 = [[0, 0, 9, 0, 0, 0, 0, 0, 7],
            [0, 4, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 4, 0, 0, 0, 0, 9],
            [0, 5, 0, 9, 0, 0, 0, 0, 4],
            [0, 0, 3, 0, 0, 0, 7, 2, 1],
            [0, 0, 0, 0, 0, 3, 0, 0, 5],
            [0, 0, 0, 0, 4, 1, 9, 0, 3],
            [4, 1, 0, 0, 3, 9, 0, 0, 8],
            [0, 0, 7, 8, 0, 2, 0, 0, 6]]

    grid17 = [[0, 0, 0, 0, 0, 0, 0, 7, 9],
            [0, 0, 0, 0, 0, 0, 3, 0, 6],
            [0, 0, 0, 0, 6, 0, 1, 0, 2],
            [0, 0, 0, 5, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 1, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 9, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 0, 0, 7, 0, 4]]

    # Set nilai awal Grid
    grid = grid76

    print("Grid awal kamu :")
    print_grid(grid)
    print()

    solve_backtrack(grid)

if __name__=="__main__":
    main()