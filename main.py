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
        # todo
        # self.__root.protocol("WM_DELETE_WINDOW", self.on_exit_button_pressed)

        # Setting MainFrame
        self.__menu_frame = game_env_interface.MenuFrame(self)
        self.__arrange_frame = None
        self.__game_frame = None
        self.__menu_frame.place_frame()
        self.__bot = ai.Obj()

        # Setting HelpFrame
        # todo
        # self.__help_frame = game_env_interface.HelpFrame(self)

    def start(self):
        """
        Starts the mainloop
        :return: None
        """
        self.__root.mainloop()

    def get_root(self):
        """
        :return: BaseWidget tkinter root (master)
        """
        return self.__root