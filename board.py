import numpy as np
import random
import datetime
import pyautogui
from time import sleep

import utils

# Define the characters for display
chars = {'unknown': '■', 'hit': 'X', 'miss': '□', 'sea': '■', 'destroyed': '*'}


def get_random_player():
    """
    Creates a Player object with a random map
    :return: Player
    """
    player = utils.Player()
    ships = utils.get_list_of_ships()

    j = 0
    for ship in ships:
        i = 0
        j += 1
        while not __is_added(player, ship):
            i += 1

    return player



def __is_added(player, ship):
    """
    :param player: Player - an object Player
    :param ship: Ship - a ship that has to be tried to put on the map of Player
    :return: True if the given ship has been put successfully
    """
    random.seed(datetime.datetime.now().microsecond)

    orientation = random.randint(1, 2)
    if orientation == utils.HORIZONTAL:
        x = random.randint(1, 11 - ship)
        y = random.randint(1, 10)
    else:
        x = random.randint(1, 10)
        y = random.randint(1, 11 - ship)

    return player.add_ship(utils.Ship(ship, orientation, x, y))



class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size), dtype=np.int8)

    def get_board(self, copy=False):
        if copy:
            return self.board.copy()
        else:
            return self.board

    def print_board(self, text):
        pyautogui.hotkey('ctrl', 'l')
        print(text)
        sleep(1)

        print("   ", end='')
        for i in range(self.size):
            pyautogui.write(str(i + 1) + ' ', interval=0.05)
        pyautogui.press('enter')

        for i, row in enumerate(self.get_board()):
            pyautogui.write(chr(i + 65) + '  ', interval=0.05)
            for cell in row:
                pyautogui.write(chars[self.square_states[cell]] + ' ', interval=0.05)
            pyautogui.press('enter')
        sleep(1)

class DefenseBoard(Board):
    def __init__(self, size, ships_array):
        super().__init__(size)
        self.attack_board = None
        self.square_states = {0: 'sea', 1: 'ship'}
        self.inv_square_states = {v: k for k, v in self.square_states.items()}
        self.ships = []
        self.available_ships = ships_array
        self.init_from_array()

class AttackBoard(Board):
    def __init__(self, defense_board):
        super().__init__(defense_board.size)
        self.defense_board = defense_board
        self.square_states = {0: 'unknown', 1: 'hit', 2: 'destroyed', 3: 'miss'}
        self.inv_square_states = {v: k for k, v in self.square_states.items()}

    def send_hit(self, x, y):
        if not self.legal_hit(x, y):
            raise ValueError("Invalid attack square")

        target = self.defense_board.get_board()[x][y]
        if target == self.defense_board.inv_square_states['ship']:
            self.get_board()[x][y] = self.inv_square_states['hit']
            # Additional logic to handle hit
            return 'hit', self.check_game_over()
        else:
            self.get_board()[x][y] = self.inv_square_states['miss']
            return 'miss', False

    def legal_hit(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.get_board()[x][y] == self.inv_square_states['unknown']

    def check_game_over(self):
        # Add your game over logic here
        return np.all(self.get_board() != self.inv_square_states['unknown'])