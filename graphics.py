# You need to install curses => pip install windows-curses
import curses

from init import KEY_ENTER, KEY_ESC, KEY_RETURN, KEY_NUM, KEY_DOT, grid
from piece import Piece

title =    "======= Four in a row ======="
subtitle = "Made by KrishenK and Atalata."
statusbarstr = "Press 'esc' to exit"

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
        
def local_play_screen(stdscr, turn: int, grid: list) -> int:
    """Draws and handle player input for local play

    Args:
        stdsrcr (curses): look at curses doc for further details
        turn (int): 0 if it is red's turn and 1 if it's yellow's turn
        grid (list): the four in a row grid

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
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    # Loop where k is the last character pressed
    while True:

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        if k == KEY_ESC: return -1
        if k == curses.KEY_RIGHT: choice += 1
        if k == curses.KEY_LEFT: choice -= 1
        if k == KEY_ENTER: return choice % 7
        
        
        turnstr = [f"It is Red's turn !", f"It is Yellow's turn !"]
        turn_start = [int((width // 2) - (len(turnstr[0]) // 2) - len(turnstr[0]) % 2), 
                      int((width // 2) - (len(turnstr[1]) // 2) - len(turnstr[1]) % 2)]
        linestr_1 = "+----"*7 + "+"
        linestr_2 = "|    "*7 + "|"
        
        start_x_grid = int((width // 2) - (len(linestr_1) // 2) - len(linestr_1) % 2)
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_y = int((height // 2)-5)
        
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        
        # Turning on attributes for title
        stdscr.attron(curses.color_pair(4))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(1, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(4))
        stdscr.attroff(curses.A_BOLD)
        
        stdscr.addstr(3, start_x_subtitle, subtitle)
        
        for i in range(0, 12, 2):
            stdscr.addstr(start_y + i, start_x_grid, linestr_1)
            stdscr.addstr(start_y + i + 1, start_x_grid, linestr_2)
        stdscr.addstr(start_y + 12, start_x_grid, linestr_1)
        
        stdscr.addstr(start_y + 13, start_x_grid + 2 + (choice%7)* 5, "^")
        
        for i in range(6):
            for j in range(7):
                if grid[i][j] == 1: stdscr.addstr(start_y + 1 + (i * 2), start_x_grid + 2 + (j*5), "  ", curses.color_pair(1))
                elif grid[i][j] == -1: stdscr.addstr(start_y + 1 + (i * 2), start_x_grid + 2 + (j*5), "  ", curses.color_pair(2))
                
        stdscr.addstr(height - 3, turn_start[turn], turnstr[turn])

        stdscr.move(height - 1, width - 1)

        stdscr.refresh()
        
        k = stdscr.getch()

def multiplayer_menu(stdscr) -> int:
    """draws the multiplayer screen

    Args:
        stdscr (curses): look at curses doc for further details

    Returns:
        int: Return the choice of the user either 1 (create a party) 2 (join a party) 3 (return to the main menu)
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

        if k == ord('1'): return 1                  # Create
        elif k == ord('2'): return 2                # Join
        elif k in [ord('3'), KEY_ESC]: return 3     # Return
        elif k == curses.KEY_UP: choice -= 1
        elif k == curses.KEY_DOWN: choice += 1
        elif k == KEY_ENTER: return choice%3 + 1

        # Declaration of strings
        optionstr = ["1. Create ", "2. Join", "3. Menu   "]
        
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

def multiplayer_address_menu(stdscr, type: int, host: str = '', port: int = 0) -> int:
    """draws the address screen, where the hoster or joiner will specify the address and the port for play together

    Args:
        stdscr (curses): look at curses doc for further details
        host (str): the IP address of the hoster (default '')
        port (int): the port of the hoster (default 0)
        type (int): 0: create a party and 1: join a party

    Returns:
        int: Return -1 to cancel
        (str, int): Return a tuple (address, port) for the socket connection
    """
    k = 0
    choice = 0
    ipstr = host
    portstr = str(port) if port != 0 else ''

    # Number of choice
    dc = 3 if type == 1 else 2

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

        if k == KEY_ESC: return -1     # Return
        elif k == KEY_ENTER: 
            if (type == 1 and choice%dc != 2) or (type == 0 and choice%dc != 1): choice += 1
            else: return (ipstr, int(portstr))
        elif k == curses.KEY_UP: choice -= 1
        elif k == curses.KEY_DOWN: choice += 1
        elif k == KEY_RETURN: 
            if choice%dc == 0 and type == 1: ipstr = ipstr[:-1]
            if (type == 1 and choice%dc == 1) or (type == 0 and choice%dc == 0): portstr = portstr[:-1]
        elif k in KEY_NUM or k == KEY_DOT: 
            if choice%dc == 0 and type == 1: ipstr += chr(k)
            if (type == 1 and choice%dc == 1) or (type == 0 and choice%dc == 0): portstr += chr(k)

        # Declaration of strings
        iplabelstr = "Address : " if type == 1 else ""
        portlabelstr = "Port : "
        connectstr = "Connect" if type == 1 else "Create"

        stdscr.addstr(0, 0, str(choice%dc))
        
        # Centering calculations
        start_x_port = int((width // 2) - (len(portlabelstr) // 2) - len(portlabelstr) % 2)
        start_x_ip = int((width // 2) - (len(iplabelstr) // 2) - len(iplabelstr) % 2) if type == 1 else start_x_port - 2
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

        # Print rest of text
        stdscr.addstr(3, start_x_subtitle, subtitle)
        stdscr.addstr(2, (width // 2) - 3, '-' * 6)

        # Print port and join input
        if type == 1: inputs = [iplabelstr+ipstr, portlabelstr+portstr, connectstr]
        else: inputs = [portlabelstr+portstr, connectstr]

        for i in range(len(inputs)):
            if i == choice%dc: 
                stdscr.addstr(start_y + i*2, start_x_ip, f'> {inputs[i]}', curses.A_BOLD)
            else:
                stdscr.addstr(start_y + i*2, start_x_port, inputs[i])

        stdscr.move(height - 1, width - 1)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def multiplayer_play_screen(stdscr, s, turn: int, grid: list) -> int:
    """Draws and handle player input for multiplayer play

    Args:
        stdsrcr (curses): look at curses doc for further details
        s (socket) : the instance of the s channel
        turn (int): 0 if it is red's turn and 1 if it's yellow's turn
        grid (list): the four in a row grid

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
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    # Set the socket in 'non-blocking' mode
    s.setblocking(True)

    # Loop where k is the last character pressed
    while True:
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        if k == KEY_ESC: return -1
        if k == curses.KEY_RIGHT: choice += 1
        if k == curses.KEY_LEFT: choice -= 1
        if k == KEY_ENTER: return choice % 7        
        
        turnstr = "It's your turn"
        turn_start = int((width // 2) - (len(turnstr) // 2) - len(turnstr) % 2)
        linestr_1 = "+----"*7 + "+"
        linestr_2 = "|    "*7 + "|"
        
        start_x_grid = int((width // 2) - (len(linestr_1) // 2) - len(linestr_1) % 2)
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_y = int((height // 2)-5)
        
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        
        # Turning on attributes for title
        stdscr.attron(curses.color_pair(4))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(1, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(4))
        stdscr.attroff(curses.A_BOLD)
        
        stdscr.addstr(3, start_x_subtitle, subtitle)
        
        for i in range(0, 12, 2):
            stdscr.addstr(start_y + i, start_x_grid, linestr_1)
            stdscr.addstr(start_y + i + 1, start_x_grid, linestr_2)
        stdscr.addstr(start_y + 12, start_x_grid, linestr_1)
        
        stdscr.addstr(start_y + 13, start_x_grid + 2 + (choice%7)* 5, "^")
        
        for i in range(6):
            for j in range(7):
                if grid[i][j] == 1: stdscr.addstr(start_y + 1 + (i * 2), start_x_grid + 2 + (j*5), "  ", curses.color_pair(1))
                elif grid[i][j] == -1: stdscr.addstr(start_y + 1 + (i * 2), start_x_grid + 2 + (j*5), "  ", curses.color_pair(2))
                
        stdscr.addstr(height - 3, turn_start, turnstr)

        stdscr.move(height - 1, width - 1)

        stdscr.refresh()

        stdscr.addstr(1, 0, str(choice))

        choice %= 7

        s.send(str(choice).encode())
        k = stdscr.getch()
        
        curses.napms(10)

def multiplayer_waiting_screen(stdscr, s, turn: int, grid: list) -> None:
    """Draws the for in a row grid and the opponent choice position

    Args:
        stdsrcr (curses): look at curses doc for further details
        s (s) : the instance of the s channel
        turn (int): 0 if it is red's turn and 1 if it's yellow's turn
        grid (list): the four in a row grid
    """
    choice = k = 0
    data = '0'

    # nodelay permits to set the getch() in non-blocking mode
    stdscr.nodelay(1)
    stdscr.notimeout(1)

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    s.setblocking(False)

    # Set the socket to a non-blocking mode
    # Loop where k is the last character pressed
    while True:
        
        # Read the data in background

        try:
            data = s.recv(1).decode()
            s.setblocking(False)
        except:
            pass


        if data == 'p': return
        else: choice = int(data)

        if k == KEY_ESC: return -1

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        stdscr.addstr(0, 0, str(data))
        stdscr.addstr(1, 0, str(choice))
        
        turnstr = "It is Your opponent's turn !"
        turn_start = int((width // 2) - (len(turnstr) // 2) - len(turnstr) % 2)
        linestr_1 = "+----"*7 + "+"
        linestr_2 = "|    "*7 + "|"
        
        start_x_grid = int((width // 2) - (len(linestr_1) // 2) - len(linestr_1) % 2)
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_y = int((height // 2)-5)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        
        # Turning on attributes for title
        stdscr.attron(curses.color_pair(4))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(1, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(4))
        stdscr.attroff(curses.A_BOLD)

        stdscr.addstr(3, start_x_subtitle, subtitle)
        
        for i in range(0, 12, 2):
            stdscr.addstr(start_y + i, start_x_grid, linestr_1)
            stdscr.addstr(start_y + i + 1, start_x_grid, linestr_2)
        stdscr.addstr(start_y + 12, start_x_grid, linestr_1)

        stdscr.addstr(start_y + 13, start_x_grid + 2 + (choice%7)* 5, "^")
        
        for i in range(6):
            for j in range(7):
                if grid[i][j] == 1: stdscr.addstr(start_y + 1 + (i * 2), start_x_grid + 2 + (j*5), "  ", curses.color_pair(1))
                elif grid[i][j] == -1: stdscr.addstr(start_y + 1 + (i * 2), start_x_grid + 2 + (j*5), "  ", curses.color_pair(2))
                
        stdscr.addstr(height - 3, turn_start, turnstr)

        stdscr.move(height - 1, width - 1)
        
        stdscr.refresh()

        k = stdscr.getch()
    
        curses.napms(10)


def winning_screen(stdscr, winner: int, online: bool) -> None:
    """Draws the for in a row grid and the opponent choice position

    Args:
        stdsrcr (curses): look at curses doc for further details
        winner (int): 1 if it is red's win and -1 if it's yellow's win
        online (bool): True if from an online game
    """
    import random

    k = 0

    if online: w = 0
    else: w = 1 if winner == -1 else 2

    stdscr.nodelay(1)
    
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)


    height, width = stdscr.getmaxyx()
    piece = Piece(16, 0.05)

    row = [random.randint(1, 5) for i in range(1, 7)]
    pieces = [[Piece(height//4, 0.05)]*i for i in row]

    # Loop where k is the last character pressed
    while True:
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == KEY_ESC: return -1
        if k == curses.KEY_RESIZE: piece.setHeight(height)

        
        winstr = ["You won :)", "Yellow won!", "Red won!"]
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_pieces = int((width // 2) - len(row))
        start_x_win = int((width // 2) - (len(winstr[w]) // 2) - len(winstr[w]) % 2)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        
        # Turning on attributes for title
        stdscr.attron(curses.color_pair(4))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(1, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(4))
        stdscr.attroff(curses.A_BOLD)

        stdscr.addstr(3, start_x_subtitle, subtitle)                   
        
        for i in range(len(row)):
            for j in range(row[i]):
                if(pieces[i][j].isMoving()): pieces[i][j].calc()
                if winner == 1: stdscr.addstr(int(height//2 - pieces[i][j].y) - (j + 2), start_x_pieces + (i * 2), "  ", curses.color_pair(1))
                elif winner == -1: stdscr.addstr(int(height//2 - pieces[i][j].y) - (j + 2), start_x_pieces + (i * 2), "  ", curses.color_pair(2))
        
        # Winner 
        stdscr.addstr(int((height // 2)), start_x_win, winstr[w])

        stdscr.move(height - 1, width - 1)
        
        stdscr.refresh()

        k = stdscr.getch()

        curses.napms(20)

def losing_screen(stdscr, loser: int, online: bool) -> None:
    """Draws the for in a row grid and the opponent choice position

    Args:
        stdsrcr (curses): look at curses doc for further details
        loser (int): 1 if it is red's win and -1 if it's yellow's win
        online (bool): True if from an online game
    """

    k = 0

    if online: l = 0

    stdscr.nodelay(1)
    
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)


    height, width = stdscr.getmaxyx()

    piece = Piece(height//4, 0.05, 0.4)

    # Loop where k is the last character pressed
    while True:
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == KEY_ESC: return -1
        if k == curses.KEY_RESIZE: piece.setHeight(height)

        losestr = "You lost :("
        
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_pieces = int((width // 2) - 1)
        start_x_lose = int((width // 2) - (len(losestr) // 2) - len(losestr) % 2)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))
        
        # Turning on attributes for title
        stdscr.attron(curses.color_pair(4))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(1, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(4))
        stdscr.attroff(curses.A_BOLD)

        stdscr.addstr(3, start_x_subtitle, subtitle)                   
        
        
        if(piece.isMoving()): piece.calc()
        if loser == 1: stdscr.addstr(int(height//2 - piece.y - 2), start_x_pieces, "  ", curses.color_pair(1))
        elif loser == -1: stdscr.addstr(int(height//2 - piece.y - 2), start_x_pieces, "  ", curses.color_pair(2))
        
        # Loser 
        stdscr.addstr(int((height // 2)), start_x_lose, losestr)

        stdscr.move(height - 1, width - 1)
        
        stdscr.refresh()

        k = stdscr.getch()

        curses.napms(20)

        
def main():
    choice = -1
    while choice != 3:
        choice = curses.wrapper(start_menu)
        if choice == 1: curses.wrapper(local_play_screen, 0, grid)
        elif choice == 2: 
            multichoice = -1
            while multichoice != 3:
                multichoice = curses.wrapper(multiplayer_menu)
                if multichoice == 1: curses.wrapper(multiplayer_address_menu, 0, "127.0.0.1", "25565")
                if multichoice == 2: curses.wrapper(multiplayer_address_menu, 1)

if __name__ == "__main__":
    main()