from tkinter import *
from constants import Colors as Color
import utils

class MapBuilder(object):

    def __init__(self, context, master, width_and_height):
        """
        init the map
        :param context: Main - context
        :param: tkinter master - container
        :param width_and_height: int - width of a single grid (default(1))
        """
        self.__context = context
        self.__frame_map = Frame(master)
        self.__buttons = self.__create_frame(self.__frame_map, width_and_height)
        self.__player = None

    def __str__(self):
        return str(self.__buttons)

    def __on_mouse_entered(self, event, x, y):
        """
        Calls when the mouse has entered to the buttons
        :param event: tkinter event
        :return: None
        """
        try:
            self.__context.on_mouse_entered(event, x, y)
        except AttributeError:
            pass

    def __on_mouse_leaved(self, event, x, y):
        """
        Calls when the mouse has leaved to the buttons
        :param event: tkinter event
        :return: None
        """
        try:
            self.__context.on_mouse_leaved(event, x, y)
        except AttributeError:
            pass

    def __on_mouse_right_clicked(self, event, x, y):
        """
        Calls when right button of the mouse is clicked
        :param event: tkinter event
        :return: None
        """
        try:
            self.__context.on_mouse_right_clicked(event, x, y)
        except AttributeError:
            print()

    def __create_frame(self, root, width_and_height):  # Creating MapFrame getting
        """
        Creates a map (10x10), private
        :param root: tkinter object (master, Frame) - container
        :param width_and_height: int - width end height of a single grid
        :return: list of tkinter Buttons
        """
        print("MapBuilder: map created")
        buttons = [None]
        letter_coordinates = "ABCDEFGHIJ"

        for y in range(1, 11):

            Label(root,
                  text=str(y)).grid(row=y, column=0)
            Label(root,
                  text=letter_coordinates[y-1]).grid(row=0, column=y)

            row_buttons = [None]
            for x in range(1, 11):
                bt = Button(root,
                            text="",
                            width=width_and_height,
                            height=width_and_height,
                            bg=Color.MAP_COLOR,
                            activebackground=Color.MAP_COLOR,
                            command=lambda coord_x=x, coord_y=y: self.__on_button_clicked(coord_x, coord_y))

                bt.grid(row=y, column=x)
                bt.bind("<Enter>", lambda e, coord_x=x, coord_y=y: self.__on_mouse_entered(e, coord_x, coord_y))
                bt.bind("<Leave>", lambda e, coord_x=x, coord_y=y: self.__on_mouse_leaved(e, coord_x, coord_y))
                bt.bind("<Button-3>", lambda e, coord_x=x, coord_y=y:
                        self.__on_mouse_right_clicked(e, coord_x, coord_y))

                row_buttons.append(bt)
            buttons.append(row_buttons)

        return buttons

    def __on_button_clicked(self, x, y):
        """
        Map click listener, private
        :param x: int - X coordinate of the clicked grid
        :param y: int - Y coordinate of the clicked grid
        :return: None
        """
        #  print(x, y)
        self.__context.on_point_clicked(x, y)

    def set_player(self, player: utils.Player):
        """
        Sets player object ot this map
        :param player: Player - the player
        :return: None
        """
        self.__player = player

    def connect_maps(self):
        """
        Shows player's map on this map
        :return: None
        """
        for i in range(1, 11):
            ship = self.__player.get_ship(i)
            if ship is not None:
                for j in range(ship.get_type()):
                    self.get_button(ship.get_x_at(j), ship.get_y_at(j)).config(bg=Color.SHIP_COLOR)

    def get_button(self, x, y):
        """
        Gets the button at the fixed coordinate
        :param x: int - X coordinate
        :param y: int - Y coordinate
        :return: tkinter object Button
        """
        return self.__buttons[y][x]

    def refresh(self):
        """
        Makes a map as normal
        :return: None
        """
        for y in range(1, 11):
            for x in range(1, 11):
                self.__buttons[y][x].config(bg=Color.MAP_COLOR)

    def clickable(self, state: bool):
        """
        Makes the map impossible to click
        :return: None
        """
        if state is True:
            bt_state = NORMAL
        else:
            bt_state = DISABLED
        for y in range(1, 11):
            for x in range(1, 11):
                self.__buttons[y][x].config(state=bt_state)

    def get_frame(self):
        """
        :return: tkinter object Frame - the created MapFrame
        """
        return self.__frame_map