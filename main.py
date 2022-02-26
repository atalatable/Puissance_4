from graphics import start_menu,multiplayer_menu, multiplayer_address_menu
from local import local
from multiplayer import host, join
from init import grid
from save import load_grid
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
                if multichoice == 1: host(wrapper(multiplayer_address_menu, 0, "", "25565"), grid)
                if multichoice == 2: join(wrapper(multiplayer_address_menu, 1))
        
if __name__ == "__main__":
    main()