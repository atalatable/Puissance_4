from save import load_grid, show_grid


def verify_grid(grid: list) -> str:
    """Check if there is any winners in the given grid

    Args:
        grid (list): the four in a row grid

    Returns:
        str: return "red" if red wins "yellow" if yellow wins and "" if no one wins
    """
    # checking columns
    for i in range(7):
        result = vertical_check(grid, i)
        if result: return result
    
    # checking lines
    for i in range(6):
        result = horizontal_check(grid, i)
        if result: return result

    # descending diagonals 
    for i in range(3):
        result = descending_diagonal_check(grid, i)
        if result: return result

    # ascending diagonals
    for i in range(3):
        result = ascending_diagonal_check(grid, i)
        if result: return result
    
    return ""


def vertical_check(grid: list, column: int) -> str:
    """Check if there is any winners in the given column of the given grid

    Args:
        grid (list): the four in a row grid
        column (int) : the column you want to check

    Returns:
        str: return "red" if red wins "yellow" if yellow wins and "" if no one wins
    """
    for i in range(3):
        if grid[i][column] != 0:
            if grid[i][column] == grid[i+1][column] and grid[i][column] == grid[i+2][column] and grid[i][column] == grid[i+3][column]:
                if grid[i][column] == -1:
                    return "yellow"
                else:
                    return "red"
    return ""


def horizontal_check(grid: list, line: int) -> str:
    """Check if there is any winners in the given line of the given grid

    Args:
        grid (list): the four in a row grid
        line (int) : the line you want to check

    Returns:
        str: return "red" if red wins "yellow" if yellow wins and "" if no one wins
    """
    for i in range(4):
        if grid[line][i] != 0:
            if grid[line][i] == grid[line][i+1] and grid[line][i] == grid[line][i+2] and grid[line][i] == grid[line][i+3]:
                if grid[line][i] == -1:
                    return "yellow"
                else:
                    return "red"
    return ""


def descending_diagonal_check(grid: list, column: int) -> str:
    """Check the diagonals (going down and right) of the given column (start of the diagonal) of the given grid

    Args:
        grid (list): the four in a row grid
        column (int): the start column of the diagonals (to the right) you want to check

    Returns:
        str: return "red" if red wins "yellow" if yellow wins and "" if no one wins
    """
    for i in range(3):
        if grid[i][column] != 0:
            if grid[i][column] == grid[i+1][column+1] and grid[i][column] == grid[i+2][column+2] and grid[i][column] == grid[i+3][column+3]:
                if grid[i][column] == -1:
                    return "yellow"
                else:
                    return "red"
    return ""


def ascending_diagonal_check(grid: list, column: int) -> str:
    """Check the diagonals (going up and right) of the given column (start of the diagonal) of the given grid

    Args:
        grid (list): the four in a row grid
        column (int): the start column of the diagonals (to the right) you want to check

    Returns:
        str: return "red" if red wins "yellow" if yellow wins and "" if no one wins
    """
    for i in range(3, 6):
        if grid[i][column] != 0:
            if grid[i][column] == grid[i-1][column+1] and grid[i][column] == grid[i-2][column+2] and grid[i][column] == grid[i-3][column+3]:
                if grid[i][column] == -1:
                    return "yellow"
                else:
                    return "red"
    return ""


def main():
    grid = load_grid("./grids/game1.txt")
    show_grid()
    winner = verify_grid(grid)
    if winner: print(f'\nThe winner is {winner} !\n')
    else: print(f'\nThe game is not finnished yet !\n')

if __name__ == "__main__":
    main()
