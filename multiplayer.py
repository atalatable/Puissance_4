from curses import wrapper
from typing import Tuple
from graphics import multiplayer_play_screen, multiplayer_waiting_screen
from check import verify_grid
from save import add_piece
import socket
import json
import time
from requests import get

from save import load_grid

def multiplayer(s: socket, turn: int, grid: list) -> None:
    """manages the multiplayer playing logic

    Args:
        grid (list): the four in a row grid
    """
    winner, quit = ("", False)
    column = 0
    
    while winner == "" and not quit:
        column = wrapper(multiplayer_play_screen, s, turn, grid)
        if column == -1: break
        check = add_piece(grid, turn, column)
        if check:
            winner = verify_grid(grid)
            return (winner, grid)


def host(address : Tuple[str, int], grid: list) -> str:
    """Host the game (server side)

    Args:
        address (Tuple[str, int]): (str) is the IP address of the hoster and the (int) is the port where the client will listen
        grid (list): the four in a row grid

    Returns:
        str: return "red" if red wins "yellow" if yellow wins, "full" if the grid is full
    """
    backlog = 5
    size = 1024

    # Create the server (see the socket doc for further information)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(address)
    except Exception as e:
        print(e)
        return None

    # print(f'Your IP addresses :\n\nIPV4 : {get("https://api.ipify.org").text}\nIPV6 : {get("https://api64.ipify.org").text}')

    s.listen(backlog)

    # Waiting for client connection
    client, address = s.accept()

    # Send the grid to the opponent
    client.send(json.dumps(grid).encode())

    winner = ""

    while not winner:
        waiting = wrapper(multiplayer_waiting_screen, client, 0, grid)
        # Get back to a socket blocking mode
        client.setblocking(True) 

        try:
            # Waiting for the grid or information if he won
            data = client.recv(size) 
        except Exception as e:
            print(e)
            break

        # Check if the game is full or enemy has won else play
        if "full" in [waiting, data.decode()]: winner = "full"
        elif "win" in [waiting, data.decode()]: winner = "red"
        else:
            # Display the game and get the results (the grid and the winner if he has won)
            (winner, grid) = multiplayer(client, 1, json.loads(data.decode()))

            # If he wins send to the opponent that he loses
            # first send -> close the waiting screen
            # second send -> inform the lose
            if winner == "yellow": client.send(b'win'); time.sleep(0.1); client.send(b'win')
            else: 
                # Send that he can play and send the new grid
                client.send(b'play')
                time.sleep(0.1)
                client.send(json.dumps(grid).encode())
        

    client.close()
    return winner

def join(address: Tuple[str, int]) -> str:
    """Join the game (client side)

    Args:
        address (Tuple[str, int]): (str) is the IP address of the hoster and the (int) is the port where we will listen
    
    Returns:
        str: return "red" if red wins "yellow" if yellow wins, "full" if the grid is full
    """
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Trying to connect to the server
    try:
        s.connect(address)
    except Exception as e:
        print(e)
        return None

    winner = ""

    while not winner:
        # Get back to a socket blocking mode (useless for the first loop)
        s.setblocking(True) 

        # Same process as the host
        try:
            data = s.recv(size)
        except Exception as e:
            print(e)
            break
    
        if data.decode() == 'full': winner = 'full'
        elif data.decode() == 'win': winner = "yellow"
        else:
            (winner, grid) = multiplayer(s, 0, json.loads(data.decode()))

            if winner == "red": s.send(b'win'); time.sleep(0.1); s.send(b'win')
            elif winner == "full": s.send(b'full'); time.sleep(0.1); s.send(b'full')
            else: 
                s.send(b'play')
                time.sleep(0.1)
                s.send(json.dumps(grid).encode())
                wrapper(multiplayer_waiting_screen, s, 1, grid)
        

    s.close()
    return winner

if __name__ == "__main__":
    # print(get("https://api.ipify.org").text)

    t = input('(host | join) >>')
    grid = load_grid('./grids/game1.txt')
    if t == 'join': join(('127.0.0.1', 25565))
    elif t == 'host': host(('127.0.0.1', 25565), grid)