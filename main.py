from sudoku_bruteforce import *
from sudoku_backtrack import *

import timeit
import matplotlib.pyplot as plt

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
    y_backtrack.append(round(result,5))
    # print("[Backtrack]   execution time is %.5f seconds" %(result))
    
    result = timeit.timeit(lambda: solve_bruteforce(grid_bf),number=n_run)
    y_bruteforce.append(round(result,5))
    # print("[Brute Force] execution time is %.5f seconds\n" %(result))

def draw_graph(x,y1,y2):
    # plotting the points 
    plt.plot(x, y1, color='green', linestyle='dashed', linewidth = 3,
             marker='o', markerfacecolor='blue', markersize=8, label='Backtrack')
    plt.plot(x, y2, color='red', linestyle='dashed', linewidth = 3,
             marker='o', markerfacecolor='orange', markersize=8, label='Brute Force')

    plt.xlabel('x - Jumlah n kali Run')
    plt.ylabel('y - Waktu eksekusi')

    plt.legend()
    plt.show()

def main():
    use_grid = grid17

    print("Grid awal kamu :")
    print_grid(use_grid)
    print()

    n_run = [100, 500, 1000, 2000]

    # Macam-macam ukuran jumlah run
    for i in n_run:
        try_one_sudoku(use_grid, i)

    print("Backtrack   =",y_backtrack)
    print("Brute Force =",y_bruteforce)

    draw_graph(n_run,y_backtrack,y_bruteforce)

if __name__=="__main__":
    main()