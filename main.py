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
        self.__root.protocol("WM_DELETE_WINDOW", self.on_exit_button_pressed)

        # Setting MainFrame
        self.__menu_frame = game_env_interface.MenuFrame(self)
        self.__arrange_frame = None
        self.__game_frame = None
        self.__menu_frame.place_frame()
        self.__bot = ai.Obj()

        # Setting HelpFrame
        self.__help_frame = game_env_interface.HelpFrame(self)

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

    # Menu frame
    def on_start_arrange_button_pressed(self):
        """
        Calls when the start button of the MainFram is clicked
        :return: None
        """
        print("Main: OnStartButtonPressed")
        self.__menu_frame.displace_frame()
        self.__arrange_frame = game_env_interface.ArrangeFrame(self)
        self.__arrange_frame.place_frame()

    def on_help_button_pressed(self):
        """
        Callback: MenuFrame
        :return:
        """
        self.__menu_frame.displace_frame()
        self.__help_frame.place_frame()

    def on_exit_button_pressed(self):
        """
        Callback: MenuFrame
        :return:
        """
        print("Main: onExitButtonPressed")
        dialog = msb.askokcancel(constants.Strings.APP_NAME, constants.Strings.MenuFrame.EXIT_DIALOG_MSG)

        if dialog:
            self.__root.destroy()

    # Arrange frame
    def on_start_game_button_pressed(self, player: utils.Player):
        """
        Calls when the start button of the ArrangeFrame is clicked
        :param player: Player - a player that was created
        :return: None
        """
        print("Main: Game started!")
        self.__arrange_frame.displace_frame()
        self.__game_frame = game_env_interface.GameFrame(self, player, board.get_random_player())
        self.__game_frame.place_frame()

    def on_arrange_back_button_pressed(self):
        """
        Calls when the start button of the ArrangeFrame is clicked
        :return:
        """
        self.__arrange_frame.displace_frame()
        self.__menu_frame.place_frame()

    # Help frame
    def on_help_back_button_pressed(self):
        """
        Calls when the start button of the ArrangeFrame is clicked
        :return:
        """
        self.__help_frame.displace_frame()
        self.__menu_frame.place_frame()

    # Game frame
    def on_game_back_button_pressed(self):
        """
        Calls when the start button of the ArrangeFrame is clicked
        :return:
        """
        self.__game_frame.displace_frame()
        self.__menu_frame.place_frame()
        self.__bot = None
        self.__bot = ai.Obj()

    def get_shoot(self, sms: str):
        """
        Callback to get shot coordinates from the opponent
        :param sms: str - command to the opponent
        :return: tuple of two ints - (0: X coordinate, 1: Y coordinate)
        """
        return self.__bot.say(sms)


master = Main()

master.start()