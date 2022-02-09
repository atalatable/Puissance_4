from init import grid

def load_grid(file: str) -> int[int]:
    with open(file, 'r') as f:
        for i in range(6):
            line = list(f.readline())

            for j in range(7):
                grid[i][j] = -1 if int(line[j] == 2) else int(line[j]) 
                
    return grid


def save_grid(file: str) -> None:
    with open(file, 'w') as f:
        for i in range(7):
            for j in range(6):
                f.write(2 if (grid[i][j] == -1) else grid[i][j])
            f.write('\n')
