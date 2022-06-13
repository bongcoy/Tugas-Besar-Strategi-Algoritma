from sudoku_bruteforce import *
from sudoku_backtrack import *

import timeit

def solve_backtrack(grid_variant):
    if(sudoku_backtrack(grid_variant)):
        pass
        # print_grid(grid_variant)
    else:
        print("No solution exists")

def solve_bruteforce(grid_variant):
    if (sudoku_bruteforce(grid_variant, 0, 0)):
        pass
        # print_grid(grid_variant)
    else:
        print("No solution  exists")

def try_one_sudoku(grid_default, n_run):
    # n_run adalah Jumlah run perfunction

    # Set nilai awal Grid
    grid_bf = grid_default
    grid_bt = grid_default

    result = timeit.timeit(lambda: solve_backtrack(grid_bt),number=n_run)
    print("[Backtrack]   execution time is %.5f seconds" %(result))
    result = timeit.timeit(lambda: solve_bruteforce(grid_bf),number=n_run)
    print("[Brute Force] execution time is %.5f seconds\n" %(result))


def main():
    use_grid = grid17

    print("Grid awal kamu :")
    print_grid(use_grid)
    print()

    # Macam-macam ukuran jumlah run
    try_one_sudoku(use_grid, 100)
    try_one_sudoku(use_grid, 500)
    try_one_sudoku(use_grid, 1000)
    try_one_sudoku(use_grid, 2000)

if __name__=="__main__":
    main()