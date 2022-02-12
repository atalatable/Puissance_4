# You need to install curses => pip install windows-curses
import curses
from tracemalloc import start

from init import KEY_ENTER, KEY_ESC

def start_menu(stdscr) -> int:
    """draws the start screen

    Args:
        stdscr (curses): look at curses doc for further details

    Returns:
        int: Return the choice of the user either 1 (play locally) 2 (multiplayer) 3 (leave)
    """
    k = 0
    choice = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while True:

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == ord('1'): return 1                  # Local play
        elif k == ord('2'): return 2                # multiplayer
        elif k in [ord('3'), KEY_ESC]: return 3     # quit
        elif k == curses.KEY_UP: choice -= 1
        elif k == curses.KEY_DOWN: choice += 1
        elif k == KEY_ENTER: return choice%3 + 1

        # Declaration of strings
        title =    "======= Four in a row ======="
        subtitle = "Made by KrishenK and Atalata."
        statusbarstr = "Press 'esc' to exit"
        optionstr = ["1. Play local ", "2. Multiplayer", "3.   Leave    "]
        
        # Centering calculations
        start_x_option = int((width // 2) - (len(optionstr[0]) // 2) - len(optionstr[0]) % 2)
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_y = int((height // 2) - 2)

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(1, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Turning off attributes for consign
        stdscr.attroff(curses.color_pair(1))

        # Print rest of text
        stdscr.addstr(3, start_x_subtitle, subtitle)
        stdscr.addstr(2, (width // 2) - 3, '-' * 6)

        # Print choices
        for i in range(len(optionstr)):
            if i == choice%3:
                stdscr.addstr(start_y + i*2, start_x_option - 2, f'> {optionstr[i]}', curses.A_BOLD)
            else: stdscr.addstr(start_y + i*2, start_x_option, optionstr[i])

        stdscr.move(height - 1, width - 1)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()
        
def local_play_screen(stdscr, yellow_turn: bool) -> int:
    """Draws and handle player input for local play

    Args:
        stdsrcr (curses): look at curses doc for further details
        yellow_turn (bool): true if it is yellow's turn and false if it is red's turn

    Returns:
        int: return the column in which the player wants to play
    """
    k = 0
    choice = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while True:

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        if k == KEY_ESC: return -1
        
        linestr_1 = "+---"*7 + "+"
        linestr_2 = "|   "*7 + "|"
        statusbarstr = "Press 'esc' to exit"
        
        start_x_grid = int((width // 2) - (len(linestr_1) // 2) - len(linestr_1) % 2)
        start_y = int((height // 2)-4)
        
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        
        for i in range(0, 10, 2):
            stdscr.addstr(start_y + i, start_x_grid, linestr_1)
            stdscr.addstr(start_y + i + 1, start_x_grid, linestr_2)
        stdscr.addstr(start_y + 10, start_x_grid,  "+---"*7 + "+")

        stdscr.refresh()
        
        k = stdscr.getch()

def main():
    choice = -1
    while choice != 3:
        choice = curses.wrapper(start_menu)
        if choice == 1: curses.wrapper(local_play_screen, True)
        elif choice == 2: pass

if __name__ == "__main__":
    main()