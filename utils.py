from exceptions import ShipException
from constants import MyExceptions as Errors
import constants

BATTLESHIP = 4
CRUISER = 3
DESTROYER = 2
SUBMARINE = 1
HORIZONTAL = 1
VERTICAL = 2


def get_list_of_ships():
    """
    return: All names of ships that must be created
    """
    return constants.LIST_OF_SHIPS


class Ship(object):

    def __init__(self, tp: int, orientation: int, init_x: int, init_y: int) -> None:
        """
        :param tp: int (1-4) - which type is a ship(BATTLESHIP, CRUISER, DESTROYER, SUBMARINE)
        :param orientation: int (1 or 2) - orientation of a ship (VERTICAL, HORIZONTAL)
        :param init_y: int (1-10): X upper right coordinate of a ship
        :param init_y: int (1-10): Y upper right coordinate of a ship
        """
        self.__type = tp
        self.__orientation = orientation
        self.__coordinate_x = []
        self.__coordinate_y = []
        self.__destroyed = []
        self.__health = tp

        # Check weather given ship is not out of the map
        if 1 <= init_x <= 10 and 1 <= init_y <= 10 and \
                (orientation == HORIZONTAL and init_x + tp <= 11 or orientation == VERTICAL and init_y + tp <= 11):

            for i in range(self.__type):                    # Init coordinates Id and Destroyed param

                if orientation == HORIZONTAL:               # Sets coordinates depending on orientation
                    self.__coordinate_x.append(init_x + i)
                    self.__coordinate_y.append(init_y)
                else:
                    self.__coordinate_x.append(init_x)
                    self.__coordinate_y.append(init_y + i)

                self.__destroyed.append(False)              # Setting coordinateIds and destroyed bool list
        else:
            # Raises an Error
            raise ShipException("Ship is out of map", Errors.MAP_ERROR)

    def __str__(self):
        """
        :return: type, orientation, coordinates, destroyed sells
        """
        coors = "Coordinates: "
        destroyed_sells = "Destroyed sells: "
        for i in range(self.__type):
            coors += "(" + str(self.__coordinate_x[i]) + ", " + str(self.__coordinate_y[i]) + ") "
            destroyed_sells += str(self.__destroyed[i]) + ", "

        string = "Type: " + str(self.__type) + "\nOrientation: " \
                 + str(self.__orientation) + "\n" + coors + "\n" + destroyed_sells

        return string

    def get_type(self):
        """
        :return: int [1, 4] - type of the ship
        """
        return self.__type

    def hit(self, x, y):
        """
        Hit the part of the ship on the given coors
        :param x: int (1-10) - X coordinate to check
        :param y: int (1-10) - Y coordinate to check
        :return: True if some part of the ship is destroyed, False otherwise
        """
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
        """
        Marks the ship to the given map
        :param map_to_mark_on: map 10x10 list
        :param ship_id: int - id of the ship
        :return: None
        """
        x = self.__coordinate_x
        y = self.__coordinate_y
        for i in range(self.__type):
            map_to_mark_on[x[i]][y[i]] = ship_id

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
        """
        :param map_to_mark_on: Player map 10x10 list
        :return: True if it is possible to put onto the given map, False otherwise
        """
        x = self.__coordinate_x
        y = self.__coordinate_y
        for i in range(self.__type):
            if map_to_mark_on[x[i]][y[i]] != 0:
                return False
        return True

    def get_status(self):
        """
        :return: True if this ship is not destroyed, else False
        """
        for i in range(self.__type):
            if not self.__destroyed[i]:
                return True
        return False

    def get_x_at(self, index: int):
        """
        :param index: int - the index
        :return: return coordinate X at the given index
        """
        return self.__coordinate_x[index]

    def get_y_at(self, index: int):
        """
        :param index: int - the index
        :return: return coordinate Y at the given index
        """
        return self.__coordinate_y[index]