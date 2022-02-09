# You need to install curses => pip install windows-curses
import curses

def start_menu(stdscr) -> str:
    """draws the start screen

    Args:
        stdscr curses: look at curses doc for further details

    Returns:
        str: Return the choice of the user (quit / options / enter)
    """
    k = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while True:

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Declaration of strings
        title = "Four in a row"
        subtitle = "Made by KrishenK and Atalata"
        statusbarstr = "Press 'q' to exit | Press 'e' to access options"
        consignstr = "Press 'Enter' to start the game."
        
        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_consign = int((width // 2) - (len(consignstr) // 2) - len(consignstr) % 2)
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
        stdscr.addstr(start_y-1, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Turning on attributes for consign
        stdscr.attron(curses.color_pair(1))

        stdscr.addstr(start_y + 5, start_x_consign, consignstr)

        # Turning off attributes for consign
        stdscr.attroff(curses.color_pair(1))

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 5)
        
        stdscr.move(height - 1, width - 1)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()
        
        if k == ord('q') or k == curses.KEY_HOME : return "quit"
        if k == curses.KEY_ENTER: return "enter"
        if k == ord('e'): return "option"

def main():
    print(curses.wrapper(start_menu))

if __name__ == "__main__":
    main()