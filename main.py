import numpy as np

grid = [[3, 0, 0, 0, 6, 0, 9, 2, 0],
        [0, 1, 0, 0, 0, 3, 4, 0, 0],
        [4, 0, 9, 0, 8, 5, 0, 1, 6],
        [0, 0, 0, 0, 0, 0, 1, 5, 0],
        [0, 0, 4, 5, 9, 2, 7, 0, 0],
        [0, 9, 3, 0, 0, 0, 0, 0, 0],
        [9, 6, 0, 8, 3, 0, 5, 0, 2],
        [0, 0, 8, 2, 0, 0, 0, 9, 0],
        [0, 4, 5, 0, 1, 0, 0, 0, 7]]


def possible(x, y, n):
    # Check row
    for i in range(9):
        if grid[x][i] == n:
            return False

    # Check column
    for i in range(9):
        if grid[i][y] == n:
            return False

    x_grid = (x // 3) * 3
    y_grid = (y // 3) * 3

    # Check small square grid
    for i in range(3):
        for j in range(0, 3):
            if grid[x_grid + i][y_grid + j] == n:
                return False

    return True


def solve():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return
    print(np.matrix(grid))

solve()
