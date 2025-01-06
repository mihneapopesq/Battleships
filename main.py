from tkinter import *
from tkinter import messagebox as msb

import game_env_interface
import constants
import utils
import board
import ai


class Main(object):
    time = 0

    def __init__(self):

        self.__root = Tk()
        self.__root.title(constants.Strings.APP_NAME)
        self.__root.minsize(constants.Dimensions.APP_MIN_WIDTH,
                            constants.Dimensions.APP_MIN_HEIGHT)
        self.__root.maxsize(constants.Dimensions.APP_MAX_WIDTH,
                            constants.Dimensions.APP_MAX_HEIGHT)