import random
import datetime

import utils


def get_random_player():
    """
    Creates a Player object with a random map.
    """
    player = utils.Player()
    ships = utils.get_list_of_ships()  # (5,4,3,3,2)

    for ship_length in ships:
        placed = False
        # we keep generating random coordinates until we manage to place it
        while not placed:
            orientation = random.randint(1, 2)  # 1 = HORIZONTAL, 2 = VERTICAL

            if orientation == utils.HORIZONTAL:
                x = random.randint(1, 11 - ship_length)  # so it fits
                y = random.randint(1, 10)
            else:
                x = random.randint(1, 10)
                y = random.randint(1, 11 - ship_length)

            new_ship = utils.Ship(ship_length, orientation, x, y)
            try:
                placed = player.add_ship(new_ship)
            except:
                placed = False

    return player
