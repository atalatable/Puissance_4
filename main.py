from graphics import start_menu,multiplayer_menu, multiplayer_address_menu
from local import local
from init import grid
from curses import wrapper

def main():
    choice = 0
    
    while choice != 3:
        choice = wrapper(start_menu)
        if choice == 1: local(grid)
        elif choice == 2: 
            multichoice = -1
            while multichoice != 3:
                multichoice = wrapper(multiplayer_menu)
                if multichoice == 1: wrapper(multiplayer_address_menu, 0, "127.0.0.1", "25565")
                if multichoice == 2: wrapper(multiplayer_address_menu, 1)
        
if __name__ == "__main__":
    main()