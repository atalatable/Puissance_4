from curses import wrapper
from graphics import local_play_screen
from check import verify_grid
from save import add_piece


def multiplayer(grid: list) -> None:
    """manages the local playing logic

    Args:
        grid (list): the four in a row grid
    """
    winner, quit, turn = "", False, 1
    column = 0
    
    while winner == "" and not quit:
        column = wrapper(local_play_screen, turn, grid)
        if column == -1: break
        add_piece(grid, turn, column)
        winner = verify_grid(grid)
        if turn == 0: turn = 1
        else: turn = 0

if __name__ == "__main__":
    multiplayer()