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