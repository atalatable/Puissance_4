from curses import wrapper
from graphics import local_play_screen, winning_screen
from check import verify_grid
from save import add_piece, load_grid


def local(grid: list) -> None:
    """manages the local playing logic

    Args:
        grid (list): the four in a row grid
    """
    winner, quit, turn = "", False, 1
    column, line = 0, 0

    while winner == "" and not quit:
        column = wrapper(local_play_screen, turn, grid)
        if column == -1: break
        check = add_piece(grid, turn, column)
        if check:
            winner = verify_grid(grid)
            if turn == 0: turn = 1
            else: turn = 0

    if winner == "red": wrapper(winning_screen, 1, False)
    else: wrapper(winning_screen, -1, False)

if __name__ == "__main__":
    local()