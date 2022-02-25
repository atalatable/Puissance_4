from init import grid

def load_grid(filename: str) -> list:
    with open(filename, 'r') as file:
        i = 0
        for line in file:
            row = list(line[:-1])
            j = 0
            for value in row:
                grid[i][j] = -1 if (int(value) == 2) else int(value)
                j += 1
            i += 1

    return grid


def save_grid(filename: str) -> None:
    with open(filename, 'w') as file:
        for i in range(6):
            for j in range(7):
                file.write(str(2 if (grid[i][j] == -1) else grid[i][j]))
            file.write('\n')

# for debug only
def show_grid() -> None:
    for i in range(6):
        print('   +'+ f'{"-"*3}+'*7)
        print(f"   |", end="")
        for j in range(7):
            if grid[i][j] == 1:
                print(" \033[91m■\033[0m ", end="")
            elif grid[i][j] == -1:
                print(" \033[93m■\033[0m ", end="")
            else:
                print("   ", end="")

            
            print("|", end="")
        print()
    print('   +'+ f'{"-"*3}+'*7)

def add_piece(grid: list, color: int, column: int) -> bool:
    """Add a piece of the given color inside the grid (at the given column)

    Args:
        grid (list): the current four in a row grid
        color (int): 1 if it's yellow and 0 if it is red
        column (int): the column in which you want to add the piece
        
    Returns:
        bool: False if the column is full, True if everything is fine
    """
    if grid[0][column] != 0: return False
    
    for i in range(5):
        if grid[i+1][column] != 0: 
            if color == 0: grid[i][column] = 1
            else: grid[i][column] = -1
            return True

    if color == 0: grid[5][column] = 1
    else: grid[5][column] = -1

    return True

if __name__ == "__main__":
    grid = load_grid("./grids/game.txt")
    show_grid()