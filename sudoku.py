# pylint: disable=missing-docstring

def is_valid_block(block):
    return sorted(block) == list(range(1, 10))

def sudoku_validator(grid):
    for i in range(9):
        row = [grid[i][j] for j in range(9)]
        column = [grid[j][i] for j in range(9)]

        if not is_valid_block(row) or not is_valid_block(column):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]

            if not is_valid_block(block):
                return False

    return True
