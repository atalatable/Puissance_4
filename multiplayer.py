from curses import wrapper
from pydoc import cli
from graphics import local_play_screen
from check import verify_grid
from save import add_piece
import socket
import json

from requests import get
from save import load_grid
# from init import grid


def multiplayer(s: socket, turn: int, grid: list) -> None:
    """manages the local playing logic

    Args:
        grid (list): the four in a row grid
    """
    winner, quit = ("", False)
    column = 0
    
    while winner == "" and not quit:
        column = wrapper(local_play_screen, turn, grid)
        if column == -1: break
        add_piece(grid, turn, column)
        winner = verify_grid(grid)
        return (winner, grid)


def host(host: str, port: int, grid: list):
    backlog = 5
    size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(backlog)
    print("Serveur allumé")
    client, address = s.accept() # Waiting for client connection

    client.send(json.dumps(grid).encode())

    winner = ""

    while not winner:
        try:
            data = client.recv(size)
        except ConnectionResetError:
            break

        print(data)
        if data.decode() != "win":
            (winner, grid) = multiplayer(client, 1, json.loads(data.decode()))
            client.send(json.dumps(grid).encode())

            print(winner)

            if winner == "yellow": client.send("win".encode())
            else: client.send(json.dumps(grid).encode())
        else:
            winner = "red"


    client.close()

def join(host: str, port: int) -> None:
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        print("Connecté sur {}:{}".format(host, port))
    except Exception as e:
        print(e)

    winner = ""

    while not winner:
        try:
            data = s.recv(size)
        except ConnectionResetError:
            break

        print(data)

        if data.decode() != "win":
            (winner, grid) = multiplayer(s, 0, json.loads(data.decode()))

            if winner == "red": s.send("win".encode())
            else: s.send(json.dumps(grid).encode())
        else:
            winner = "yellow"
    s.close()



if __name__ == "__main__":
    # print(get("https://api.ipify.org").text)

    t = input('>>')
    grid = load_grid('./grids/game1.txt')
    if(t == 'join'): join('127.0.0.1', 25565)
    else: host('127.0.0.1', 25565, grid)