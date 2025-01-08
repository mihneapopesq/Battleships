from tkinter import *
from tkinter import messagebox as msb

import game_env_interface
import constants
import utils
import board
import ai
import pygame


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

        # Initialize pygame mixer
        pygame.init()
        pygame.mixer.init()

        # Load and play background music
        self.play_background_music(constants.Strings.APP_MUSIC)

        # Load background image
        self.background_image = PhotoImage(file='resources/battleships.png')
        self.background_label = Label(self.__root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)  # Make the image fill the entire window

        # Setting MainFrame
        self.__menu_frame = game_env_interface.MenuFrame(self)
        self.__arrange_frame = None
        self.__game_frame = None
        self.__menu_frame.place_frame()
        self.__bot = ai.Obj()

        # Setting HelpFrame
        self.__help_frame = game_env_interface.HelpFrame(self)

        # Center the window on the screen
        self.center_window()

    def play_background_music(self, filename):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)  # Play the music indefinitely


    def center_window(self):
        self.__root.update_idletasks()  # Update "requested size" from geometry manager
        width = self.__root.winfo_width()
        height = self.__root.winfo_height()
        x = (self.__root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.__root.winfo_screenheight() // 2) - (height // 2)
        self.__root.geometry('+{}+{}'.format(x, y))

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
    # Other methods remain unchanged


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