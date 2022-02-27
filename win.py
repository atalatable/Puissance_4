# You need to install curses => pip install windows-curses
import curses
import math

from init import KEY_ENTER, KEY_ESC, KEY_RETURN, KEY_NUM, KEY_DOT, grid

title = "======= Four in a row ======="
subtitle = "Made by KrishenK and Atalata."
statusbarstr = "Press 'esc' to exit"


class Piece:
    def __init__(self, height, y0, dt):
        self.G = 9.81
        self.K = math.sqrt(2*height/self.G)
        self.Y = [height-60*y0]
        self.V = [math.sin(2*self.G*height)]
        self.H = [height]
        self.TM = [self.K]
        self.S = 2*self.K
        self.height = height
        self.bounce = 0
        self.dt = dt
        self.t = 0
        self.T = 0

        for i in range(1, 20):
            self.S *= self.E
            self.V[i] = self.E*self.V[i-1]
            self.H[i] = self.E*self.E*self.H[i-1]
            self.TM[i] = self.TM[i-1]+self.S

    def calc(self, t):
        if self.bounce == 0:
            self.y = self.height-0.5*self.G*self.t*self.t
        else:
            self.y = self.V[self.bounce]*self.t-0.5*self.G*self.t*self.t
        if self.y < 0:
            t -= self.dt
            tau=self.TM[self.bounce]-self.T
            self.t+=tau
            self.T+= self.tau
            if self.bounce == 0:
                self.y = self.height-0.5*self.G*self.t*self.t
            else:
                self.y = self.V[self.bounce]*self.t-0.5*self.G*self.t*self.t
            self.y = 0
            self.bounce += 1
            t = 0
        if self.H[self.bounce]<0.005: return False
        self.t+=self.dt
        self.T+=self.dt
        return True
    
    def setHeight(self, height): 
        self.height = height

def winning_screen(stdscr, winner: int) -> None:
    """Draws the for in a row grid and the opponent choice position

    Args:
        stdsrcr (curses): look at curses doc for further details
        winner (int): 0 if it is red's win and 1 if it's yellow's win
    """
    import random
    k = n = x = 0

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

    row = [random.randint(1, 5) for i in range(6)]

    Y = []
    V = []
    

    # Loop where k is the last character pressed
    while True:


        if k == KEY_ESC: return -1

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        winstr = ["Red won!", "Yellow won!"]
        losestr = ["Red lost :(", "Yellow lost :("]
        win_start = [int((width // 2) - (len(winstr[0]) // 2) - len(winstr[0]) % 2), 
                      int((width // 2) - (len(winstr[1]) // 2) - len(winstr[1]) % 2)]
        lose_start = [int((width // 2) - (len(losestr[0]) // 2) - len(losestr[0]) % 2), 
                      int((width // 2) - (len(losestr[1]) // 2) - len(losestr[1]) % 2)]
        
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x = int((width // 2)-1)

        if (n+1) % 10 == 0: x += 0.1

        stdscr.addstr(0, 0, str(n))        
        stdscr.addstr(1, 0, str(x))        

        # start_y = int((height // 2)- (5-(x % 5))+1)

        v = 1*math.sin(math.pi/2) - 9.81*x

        start_y = int(int((height // 3)) + 9.81*x**2*1/2)

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
        
        # for i in range(len(row)):
        #     print(row[i])
        #     for j in range(row[i]):
        #         if winner == 1: stdscr.addstr(start_y - (j + 2), start_x + 1 * (i * 2), "  ", curses.color_pair(1))
        #         elif winner == -1: stdscr.addstr(start_y - (j + 2), start_x + 1 * (i * 2), "  ", curses.color_pair(2))

        stdscr.addstr(start_y, start_x, "  ", curses.color_pair(1))

        stdscr.move(height - 1, width - 1)
        
        stdscr.refresh()

        n+=1
        k = stdscr.getch()



def main():
    choice = curses.wrapper(winning_screen, 1)


if __name__ == "__main__":
    main()
