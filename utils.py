from exceptions import ShipException
from constants import MyExceptions as Errors
import constants

BATTLESHIP = 4
CRUISER = 3
DESTROYER = 2
SUBMARINE = 1
HORIZONTAL = 1
VERTICAL = 2

# Dictionary for how many ships of each length we need
#  length : number_of_ships
SHIPS_NEEDED = {
    5: 1,  # one ship of 5 blocks
    4: 1,  # one ship of 4 blocks
    3: 2,  # two ships of 3 blocks
    2: 1,  # one ship of 2 blocks
    1: 0   # zero ships of 1 block (we no longer want submarines)
}


def get_list_of_ships():
    """
    return: the list of ship lengths that must be created
    """
    return constants.LIST_OF_SHIPS  # (5,4,3,3,2)


class Ship(object):

    def __init__(self, tp: int, orientation: int, init_x: int, init_y: int) -> None:
        """
        :param tp: int - the length of the ship (e.g. 5,4,3,2,1)
        :param orientation: int - (HORIZONTAL=1 / VERTICAL=2)
        :param init_x: int (1-10) - the X coordinate for the top part of the ship
        :param init_y: int (1-10) - the Y coordinate
        """
        self.__type = tp
        self.__orientation = orientation
        self.__coordinate_x = []
        self.__coordinate_y = []
        self.__destroyed = []
        self.__health = tp

        # We check that it doesn't go off the 10x10 map:
        if 1 <= init_x <= 10 and 1 <= init_y <= 10 and \
           ((orientation == HORIZONTAL and init_x + tp - 1 <= 10) or
            (orientation == VERTICAL and init_y + tp - 1 <= 10)):

            for i in range(self.__type):
                if orientation == HORIZONTAL:
                    self.__coordinate_x.append(init_x + i)
                    self.__coordinate_y.append(init_y)
                else:
                    self.__coordinate_x.append(init_x)
                    self.__coordinate_y.append(init_y + i)

                self.__destroyed.append(False)
        else:
            raise ShipException("Ship is out of map", Errors.MAP_ERROR)

    def __str__(self):
        coors = "Coordinates: "
        destroyed_cells = "Destroyed cells: "
        for i in range(self.__type):
            coors += f"({self.__coordinate_x[i]}, {self.__coordinate_y[i]}) "
            destroyed_cells += str(self.__destroyed[i]) + ", "

        return f"Type(length): {self.__type}\nOrientation: {self.__orientation}\n" \
               f"{coors}\n{destroyed_cells}"

    def get_type(self):
        return self.__type

    def hit(self, x, y):
        result = -1
        for i in range(self.__type):
            if x == self.__coordinate_x[i] and y == self.__coordinate_y[i]:
                result = i
                break
        if result != -1 and not self.__destroyed[result]:
            self.__destroyed[result] = True
            return True
        return False

    def mark_on_map(self, map_to_mark_on: list, ship_id: int):
        x = self.__coordinate_x
        y = self.__coordinate_y
        for i in range(self.__type):
            map_to_mark_on[x[i]][y[i]] = ship_id

            # Mark surrounding zones with '.' so that we can't place other ships right next to it
            if map_to_mark_on[x[i] - 1][y[i]] == 0:
                map_to_mark_on[x[i] - 1][y[i]] = '.'
            if map_to_mark_on[x[i] + 1][y[i]] == 0:
                map_to_mark_on[x[i] + 1][y[i]] = '.'
            if map_to_mark_on[x[i]][y[i] - 1] == 0:
                map_to_mark_on[x[i]][y[i] - 1] = '.'
            if map_to_mark_on[x[i]][y[i] + 1] == 0:
                map_to_mark_on[x[i]][y[i] + 1] = '.'
            if map_to_mark_on[x[i] - 1][y[i] - 1] == 0:
                map_to_mark_on[x[i] - 1][y[i] - 1] = '.'
            if map_to_mark_on[x[i] + 1][y[i] + 1] == 0:
                map_to_mark_on[x[i] + 1][y[i] + 1] = '.'
            if map_to_mark_on[x[i] + 1][y[i] - 1] == 0:
                map_to_mark_on[x[i] + 1][y[i] - 1] = '.'
            if map_to_mark_on[x[i] - 1][y[i] + 1] == 0:
                map_to_mark_on[x[i] - 1][y[i] + 1] = '.'

    def is_possible_put_onto_map(self, map_to_mark_on: list):
        x = self.__coordinate_x
        y = self.__coordinate_y
        for i in range(self.__type):
            if map_to_mark_on[x[i]][y[i]] != 0:
                return False
        return True

    def get_status(self):
        # True = still floating, False = completely destroyed
        return any(not destroyed for destroyed in self.__destroyed)

    def get_x_at(self, index: int):
        return self.__coordinate_x[index]

    def get_y_at(self, index: int):
        return self.__coordinate_y[index]


class Player(object):

    def __init__(self):
        """
        We initialize a 12x12 map (protective borders),
        plus an array of ships (only 5, according to new requirements).
        """
        # we have indexing up to 5, so 6 elements, index 0 unused
        self.__ships = [None] * 6
        # stores how many ships of each length we've already placed
        # indexing: 0..5 => for type (length) = 5,4,3,2,1
        # e.g.: self.__shipsAmount[3] tells how many ships of length 3 we have placed
        self.__shipsAmount = [0, 0, 0, 0, 0, 0]

        # 12x12 with zero
        self.__map = []
        for i in range(12):
            row = []
            for j in range(12):
                row.append(0)
            self.__map.append(row)

    def __str__(self):
        string = ""
        # we have a maximum of 5 ships => indices 1..5
        for i in range(1, 6):
            string += f"\nShip #{i} >>>>>>>>>>>>>>>>>>\n{self.__ships[i]}\n"
        return string

    def get_point_on_map(self, x: int, y: int):
        return self.__map[x][y]

    def get_non_placed_amount(self, tp: int):
        """
        Returns how many ships of type (length) `tp` we can still place.
        """
        # For instance, SHIPS_NEEDED[3] = 2 (we want two 3-block ships),
        # and self.__shipsAmount[3] is how many we have already placed.
        return SHIPS_NEEDED[tp] - self.__shipsAmount[tp]

    def is_some_ships_placed(self):
        """
        True if at least one ship is placed.
        """
        for i in range(1, 6):
            if self.__ships[i] is not None:
                return True
        return False

    def is_completed(self):
        """
        True if all 5 ships are placed.
        """
        for i in range(1, 6):
            if self.__ships[i] is None:
                return False
        return True

    def show_map(self):
        """
        Prints the 10x10 map (without the 0 and 11 borders)
        """
        for i in range(1, 11):
            for j in range(1, 11):
                print(self.__map[i][j], end=" ")
            print()

    def remove_ship(self, index: int):
        """
        Removes the ship at the given `index`.
        WARNING: here the index is 1..5, not the ship type.
        """
        ship = self.__ships[index]
        if ship is not None:
            tp = ship.get_type()
            self.__ships[index] = None
            self.__shipsAmount[tp] -= 1
            # WARNING: if you actually want to remove it from the map,
            # you should reinitialize the map and place all the other ships again.
            # For now, we just remove it from the array and decrement the counter.

    def add_ship(self, ship: Ship):
        """
        Tries to add the `ship`.
        Returns True if successful, False otherwise.
        """
        tp = ship.get_type()
        amount = self.__shipsAmount[tp]
        needed = SHIPS_NEEDED.get(tp, 0)  # default 0 if unrecognized

        if amount >= needed:
            raise ShipException(
                f"All {tp}-block ships have already been placed",
                Errors.MAP_ERROR
            )

        if ship.is_possible_put_onto_map(self.__map):
            # We compute a free ID in the ships array.
            # Example: we put the ship at the index found free in self.__ships (from 1..5).

            index_to_place = None
            for idx in range(1, 6):
                if self.__ships[idx] is None:
                    index_to_place = idx
                    break

            if index_to_place is None:
                return False  # no more space (should not happen)

            self.__ships[index_to_place] = ship
            self.__shipsAmount[tp] += 1

            # Mark on map
            ship.mark_on_map(self.__map, index_to_place)
            return True

        return False

    def get_ship(self, index: int):
        return self.__ships[index]
