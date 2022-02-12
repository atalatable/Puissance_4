from graphics import start_menu
from local import local
from init import grid
from curses import wrapper

def main():
    choice = 0
    
    while choice != 3:
        choice = wrapper(start_menu)
        if choice == 1: local(grid)
        
if __name__ == "__main__":
    main()