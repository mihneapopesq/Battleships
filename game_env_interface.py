from tkinter import *
from tkinter import messagebox as msg
from constants import Strings as String
from constants import Colors as Color
from constants import BOT_SHOOT_TIME
import utils
import board


class MapBuilder(object):

    def __init__(self, context, master, width_and_height):
        self.__context = context
        self.__frame_map = Frame(master)
        self.__buttons = self.__create_frame(self.__frame_map, width_and_height)
        self.__player = None

    def __create_frame(self, root, width_and_height):
        # MapBuilder: map created
        print("MapBuilder: map created")
        buttons = [None]
        letter_coordinates = "ABCDEFGHIJ"

        for y in range(1, 11):
            Label(root, text=str(y)).grid(row=y, column=0)
            Label(root, text=letter_coordinates[y-1]).grid(row=0, column=y)

            row_buttons = [None]
            for x in range(1, 11):
                bt = Button(root,
                            text="",
                            width=width_and_height,
                            height=width_and_height,
                            bg=Color.MAP_COLOR,
                            activebackground=Color.MAP_COLOR,
                            command=lambda cx=x, cy=y: self.__on_button_clicked(cx, cy))

                bt.grid(row=y, column=x)
                bt.bind("<Enter>", lambda e, cx=x, cy=y: self.__on_mouse_entered(e, cx, cy))
                bt.bind("<Leave>", lambda e, cx=x, cy=y: self.__on_mouse_leaved(e, cx, cy))
                bt.bind("<Button-3>", lambda e, cx=x, cy=y: self.__on_mouse_right_clicked(e, cx, cy))

                row_buttons.append(bt)
            buttons.append(row_buttons)
        return buttons

    def __on_button_clicked(self, x, y):
        self.__context.on_point_clicked(x, y)

    def __on_mouse_entered(self, event, x, y):
        """ When the cursor enters a button, let the context handle the highlight. """
        try:
            self.__context.on_mouse_entered(event, x, y)
        except AttributeError:
            pass

    def __on_mouse_leaved(self, event, x, y):
        """ When the cursor leaves a button, let the context revert it to normal. """
        try:
            self.__context.on_mouse_leaved(event, x, y)
        except AttributeError:
            pass

    def __on_mouse_right_clicked(self, event, x, y):
        """ Rotate the ship on right click. """
        try:
            self.__context.on_mouse_right_clicked(event, x, y)
        except AttributeError:
            pass

    def get_button(self, x, y):
        return self.__buttons[y][x]

    def refresh(self):
        for yy in range(1, 11):
            for xx in range(1, 11):
                self.__buttons[yy][xx].config(bg=Color.MAP_COLOR)

    def clickable(self, state: bool):
        bt_state = NORMAL if state else DISABLED
        for yy in range(1, 11):
            for xx in range(1, 11):
                self.__buttons[yy][xx].config(state=bt_state)

    def set_player(self, player: utils.Player):
        self.__player = player

    def connect_maps(self):
        """
        We only iterate up to 5, because we have 5 ships:
         1 ship (5 blocks),
         1 ship (4 blocks),
         2 ships (3 blocks),
         1 ship (2 blocks).
        """
        for i in range(1, 6):  # only 5 ships
            ship = self.__player.get_ship(i)
            if ship is not None:
                for j in range(ship.get_type()):
                    self.get_button(ship.get_x_at(j), ship.get_y_at(j)).config(bg=Color.SHIP_COLOR)

    def get_frame(self):
        return self.__frame_map


class StatusBuilder(object):
    """
    A class that shows how many ships of each type have been placed, on the side.
    """

    def __init__(self, context, master, title: str, player: utils.Player):
        self.__context = context
        self.__player = player

        self.__label_battleship = None
        self.__label_cruiser = None
        self.__label_destroyer = None
        self.__label_submarine = None

        self.__frame = Frame(master)
        self.__create_frame(self.__frame, title)

    def __create_frame(self, root, title: str):
        root.config(padx=35, pady=10, highlightthickness=1, highlightbackgroun=Color.MenuFrame.BACKGROUND_BUTTONS)
        Label(root, text=title, padx=14, pady=7, font="time 14 bold").pack(anchor=W)

        # BATTLESHIP => index 0 (length 5)
        self.__label_battleship = Label(root, text=String.StatusFrame.SHIPS[0][1] + ": ", padx=7, pady=3,
                                        font="time 10 italic")
        self.__label_battleship.pack(anchor=W)

        # CRUISER => index 1 (length 4)
        self.__label_cruiser = Label(root, text=String.StatusFrame.SHIPS[1][1] + ": ", padx=7, pady=3,
                                     font="time 10 italic")
        self.__label_cruiser.pack(anchor=W)

        # DESTROYER => index 2 (length 3)
        self.__label_destroyer = Label(root, text=String.StatusFrame.SHIPS[2][1] + ": ", padx=7, pady=3,
                                       font="time 10 italic")
        self.__label_destroyer.pack(anchor=W)

        # SUBMARINE => index 3 (length 2)
        self.__label_submarine = Label(root, text=String.StatusFrame.SHIPS[3][1] + ": ", padx=7, pady=3,
                                       font="time 10 italic")
        self.__label_submarine.pack(anchor=W)

    def refresh(self):
        """
        Shows how many ships of type (5,4,3,2) have been placed so far.
        """
        self.__label_battleship.config(
            text=String.StatusFrame.SHIPS[0][1] + ": " +
                 str(1 - self.__player.get_non_placed_amount(5))
        )
        self.__label_cruiser.config(
            text=String.StatusFrame.SHIPS[1][1] + ": " +
                 str(1 - self.__player.get_non_placed_amount(4))
        )
        self.__label_destroyer.config(
            text=String.StatusFrame.SHIPS[2][1] + ": " +
                 str(2 - self.__player.get_non_placed_amount(3))
        )
        self.__label_submarine.config(
            text=String.StatusFrame.SHIPS[3][1] + ": " +
                 str(1 - self.__player.get_non_placed_amount(2))
        )

    def get_frame(self):
        return self.__frame


class MenuFrame(object):
    """
    Frame with the main buttons: Start, Help, Exit
    """

    def __init__(self, context):
        self.__context = context
        self.__frame = self.__create_frame(self.__context.get_root())

    def __on_start_button_pressed(self):
        self.__context.on_start_arrange_button_pressed()

    def __on_help_button_pressed(self):
        self.__context.on_help_button_pressed()

    def __on_exit_button_pressed(self):
        self.__context.on_exit_button_pressed()

    def __create_frame(self, root):
        frame = Frame(root, padx=10, pady=10, highlightthickness=1,
                      highlightbackgroun=Color.MenuFrame.BACKGROUND_BUTTONS)

        Label(frame,
              text=String.MenuFrame.TITLE,
              pady=5,
              font="time 14 bold").pack()

        bt_start_game = Button(frame,
                               text=String.MenuFrame.BUTTON_START,
                               width=20,
                               padx=4,
                               takefocus="tab",
                               command=self.__on_start_button_pressed)
        bt_help = Button(frame,
                         text=String.MenuFrame.BUTTON_HELP,
                         width=20,
                         padx=4,
                         command=self.__on_help_button_pressed)
        bt_exit = Button(frame,
                         text=String.MenuFrame.BUTTON_EXIT,
                         width=20,
                         padx=4,
                         command=self.__on_exit_button_pressed)

        bt_start_game.pack()
        bt_help.pack()
        bt_exit.pack()

        return frame

    def place_frame(self):
        self.__frame.place(relx=0.17, rely=0.3, anchor=CENTER)

    def displace_frame(self):
        self.__frame.place_forget()

    def get_frame(self):
        return self.__frame


class ArrangeFrame(object):
    """
    Frame where the player arranges their ships on the map.
    """

    def __init__(self, context):
        self.__context = context

        # Default: 5 (BATTLESHIP)
        self.__chosen_ship = IntVar()
        self.__chosen_ship.set(5)

        self.__frame_choose = Frame(self.__context.get_root())
        self.__create_choose_frame(self.__frame_choose)

        self.__frame_status = Frame(self.__context.get_root())
        self.__label_type = None
        self.__label_amount = None
        self.__frame_of_orientation = None
        self.__orientation = True  # True => horizontal
        self.__create_status_frame(self.__frame_status)

        # Initial drawing: ship of 5 blocks
        self.__frame_of_orientation = self.__draw_ship(self.__frame_status, 5, self.__orientation)
        self.__frame_of_orientation.pack()

        self.__frame_map = Frame(self.__context.get_root())
        self.__map = MapBuilder(self, self.__frame_map, 2)
        self.__map.get_frame().pack()

        self.__frame_message = Frame(self.__context.get_root())
        self.__label_warnings = None
        self.__create_message_frame(self.__frame_message)

        self.__frame_special = Frame(self.__context.get_root())
        self.__create_special_frame(self.__frame_special)

        self.__player = utils.Player()
        self.__can_ship_be_put = True

    def __get_ship_name_by_size(self, size: int) -> str:
        for val, name in String.StatusFrame.SHIPS:
            if val == size:
                return name
        return "Unknown"

    def __on_ship_chosen(self):
        size = self.__chosen_ship.get()
        ship_name = self.__get_ship_name_by_size(size)
        text = String.StatusFrame.HEADER_TYPE + " " + ship_name
        self.__label_type.config(text=text)

        text2 = String.StatusFrame.HEADER_AMOUNT + " " + str(self.__player.get_non_placed_amount(size))
        self.__label_amount.config(text=text2)

        if self.__frame_of_orientation is not None:
            self.__frame_of_orientation.pack_forget()

        self.__orientation = True
        self.__frame_of_orientation = self.__draw_ship(self.__frame_status, size, self.__orientation)
        self.__frame_of_orientation.pack()

    def on_point_clicked(self, x, y):
        size = self.__chosen_ship.get()
        if self.__player.get_non_placed_amount(size) > 0:
            orientation = 1 if self.__orientation else 2
            ship_is_added = False
            if self.__can_ship_be_put:
                try:
                    ship = utils.Ship(size, orientation, x, y)
                    ship_is_added = self.__player.add_ship(ship)
                    if ship_is_added:
                        print("StatusFrame: this ship is added\n", ship)
                except Exception:
                    ship_is_added = False

            if not ship_is_added:
                self.__show_warning(
                    String.StatusFrame.WARNING_CANNOT_PUT %
                    self.__get_ship_name_by_size(size),
                    "red"
                )
            else:
                # Automatically switch to the next type if you've finished placing the current one
                if self.__chosen_ship.get() > 1 and \
                   self.__player.get_non_placed_amount(self.__chosen_ship.get()) == 0:
                    self.__chosen_ship.set(self.__chosen_ship.get() - 1)

            self.__on_ship_chosen()
            self.__orientation = not self.__orientation
            self.__on_change_button_pressed()

            if self.__player.is_completed():
                self.__show_warning(String.StatusFrame.WARNING_CAN_START, "green")
        else:
            self.__show_warning(
                String.StatusFrame.WARNING_ALL_SHIPS_PUT %
                self.__get_ship_name_by_size(size),
                "red"
            )

    def on_mouse_entered(self, event, x, y):
        """
        When the cursor enters a button, color the sequence of buttons that would
        represent the ship, up to the boundary (10) if it exceeds.
        """
        size = self.__chosen_ship.get()
        if self.__player.get_non_placed_amount(size) > 0:
            if self.__orientation:
                # HORIZONTAL
                end_x = x + size - 1
                if end_x > 10:
                    end_x = 10
                    self.__can_ship_be_put = False
                    color = Color.ERROR_COLOR
                else:
                    self.__can_ship_be_put = True
                    color = Color.SHIP_COLOR

                # Active background only for the button under the cursor
                if self.__player.get_point_on_map(x, y) != 0:
                    event.widget.config(activebackground=Color.ERROR_COLOR)
                else:
                    event.widget.config(activebackground=color)

                # Color the interval [x..end_x]
                for i in range(x, end_x + 1):
                    point = self.__player.get_point_on_map(i, y)
                    if point != 0:
                        self.__map.get_button(i, y).config(bg=Color.ERROR_COLOR)
                    else:
                        self.__map.get_button(i, y).config(bg=color)

            else:
                # VERTICAL
                end_y = y + size - 1
                if end_y > 10:
                    end_y = 10
                    self.__can_ship_be_put = False
                    color = Color.ERROR_COLOR
                else:
                    self.__can_ship_be_put = True
                    color = Color.SHIP_COLOR

                if self.__player.get_point_on_map(x, y) != 0:
                    event.widget.config(activebackground=Color.ERROR_COLOR)
                else:
                    event.widget.config(activebackground=color)

                # Color the interval [y..end_y]
                for i in range(y, end_y + 1):
                    point = self.__player.get_point_on_map(x, i)
                    if point != 0:
                        self.__map.get_button(x, i).config(bg=Color.ERROR_COLOR)
                    else:
                        self.__map.get_button(x, i).config(bg=color)
        else:
            # The current type has already been fully placed
            if self.__player.get_point_on_map(x, y) not in ('.', 0):
                event.widget.config(activebackground=Color.SHIP_COLOR)

    def on_mouse_leaved(self, event, x, y):
        """
        When the cursor leaves a button, revert to normal coloring (MAP_COLOR).
        """
        event.widget.config(activebackground=Color.MAP_COLOR)
        size = self.__chosen_ship.get()

        if self.__orientation:
            end_x = x + size - 1
            if end_x > 10:
                end_x = 10

            for i in range(x, end_x + 1):
                point = self.__player.get_point_on_map(i, y)
                if point in ('.', 0):
                    self.__map.get_button(i, y).config(bg=Color.MAP_COLOR)
                else:
                    # If it was ERROR_COLOR, set back SHIP_COLOR
                    if self.__map.get_button(i, y).cget("bg") == Color.ERROR_COLOR:
                        self.__map.get_button(i, y).config(bg=Color.SHIP_COLOR)
        else:
            end_y = y + size - 1
            if end_y > 10:
                end_y = 10

            for i in range(y, end_y + 1):
                point = self.__player.get_point_on_map(x, i)
                if point in ('.', 0):
                    self.__map.get_button(x, i).config(bg=Color.MAP_COLOR)
                else:
                    if self.__map.get_button(x, i).cget("bg") == Color.ERROR_COLOR:
                        self.__map.get_button(x, i).config(bg=Color.SHIP_COLOR)

    def on_mouse_right_clicked(self, event, x, y):
        # Rotate the ship on right click
        self.on_mouse_leaved(event, x, y)
        self.__on_change_button_pressed()
        self.on_mouse_entered(event, x, y)

    def __on_change_button_pressed(self):
        if self.__frame_of_orientation is not None:
            self.__frame_of_orientation.pack_forget()
        self.__orientation = not self.__orientation

        size = self.__chosen_ship.get()
        self.__frame_of_orientation = self.__draw_ship(self.__frame_status, size, self.__orientation)
        self.__frame_of_orientation.pack()

    def __on_random_button_pressed(self):
        self.__player = board.get_random_player()
        self.__map.refresh()
        for yy in range(1, 11):
            for xx in range(1, 11):
                point = self.__player.get_point_on_map(xx, yy)
                if point not in (0, '.'):
                    self.__map.get_button(xx, yy).config(bg=Color.SHIP_COLOR)
        self.__orientation = not self.__orientation
        self.__on_change_button_pressed()

    def __on_back_menu_button_pressed(self):
        is_agree = msg.askyesno(String.APP_NAME, String.StatusFrame.DIALOG_BACK_MENU)
        if is_agree:
            self.__context.on_arrange_back_button_pressed()

    def __on_start_button_pressed(self):
        if self.__player.is_completed():
            self.__context.on_start_game_button_pressed(self.__player)
        else:
            self.__show_warning(String.StatusFrame.WARNING_PUT_ALL_SHIPS, "red")

    def __on_clear_button_pressed(self):
        if self.__player.is_some_ships_placed():
            is_agree = msg.askyesno(String.APP_NAME, String.StatusFrame.DIALOG_CLEAR_ALL)
            if is_agree:
                self.__player = utils.Player()
                self.__map.refresh()
                self.__show_warning(String.StatusFrame.WARNING_SHIPS_CLEARED, "green")
                self.__on_ship_chosen()  # refresh status
        else:
            self.__show_warning(String.StatusFrame.WARNING_EMPTY_MAP, "red")

    def __show_warning(self, warning: str, color: str):
        self.__label_warnings.config(text=warning, fg=color)
        self.__label_warnings.after(4000, lambda: self.__label_warnings.config(text=""))

    @staticmethod
    def __draw_ship(root, tp: int, orientation: bool):
        frame = Frame(root, pady=25)
        for i in range(tp):
            bt = Button(frame, width=1, height=1, bg=Color.SHIP_COLOR, state=DISABLED)
            if orientation:
                bt.grid(row=0, column=i)
            else:
                bt.grid(row=i, column=0)
        return frame

    def __create_choose_frame(self, root):
        root.config(padx=10, pady=10)
        Label(root, pady=3, padx=15, text=String.StatusFrame.MSG_CHOSE, font="time 14 bold").pack(anchor=W)
        for value, ship_name in String.StatusFrame.SHIPS:
            Radiobutton(root,
                        text=ship_name,
                        padx=10,
                        pady=4,
                        width=16,
                        anchor=W,
                        indicatoron=0,
                        variable=self.__chosen_ship,
                        value=value,
                        command=self.__on_ship_chosen).pack(anchor=W)

    def __create_status_frame(self, root):
        root.config(padx=11, pady=10)
        Label(root, pady=3, padx=15, text=String.StatusFrame.MSG_CHOSEN, font="time 14 bold").pack(anchor="w")

        self.__label_type = Label(root, text="Type: BATTLESHIP", padx=10, pady=3)
        self.__label_type.pack(anchor=W)

        self.__label_amount = Label(root, text="Amount: 1", padx=10, pady=2)
        self.__label_amount.pack(anchor=W)

        Label(root, text=String.StatusFrame.HEADER_ORIENTATION, padx=10, pady=2).pack(anchor=W)

    def __create_message_frame(self, root):
        self.__label_warnings = Label(root, fg=Color.ERROR_COLOR, bg=Color.MAP_COLOR,
                                      width=43, height=1, font="time 12 italic")
        self.__label_warnings.pack(anchor=W)

    def __create_special_frame(self, root):
        Button(root,
               text=String.StatusFrame.BUTTON_CLEAR_ALL,
               width=18,
               anchor=W,
               bg=Color.ERROR_COLOR, fg="white",
               command=self.__on_clear_button_pressed).pack()

        Button(root,
               text=String.StatusFrame.BUTTON_RANDOM,
               width=18,
               anchor=W,
               bg=Color.SHIP_COLOR, fg="white",
               command=self.__on_random_button_pressed).pack()

        Button(root,
               text=String.StatusFrame.BUTTON_BACK_MENU,
               width=18,
               anchor=W,
               bg=Color.BACK_BUTTON, fg="white",
               command=self.__on_back_menu_button_pressed).pack()

        Button(root,
               text=String.StatusFrame.BUTTON_START,
               anchor=W,
               width=18,
               command=self.__on_start_button_pressed).pack()

    def place_frame(self):
        self.__frame_choose.place(relx=0.03, rely=0.1, anchor=NW)
        self.__frame_status.place(relx=0.03, rely=0.45, anchor=NW)
        self.__frame_map.place(relx=0.5, rely=0.08, anchor=N)
        self.__frame_message.place(relx=0.5, rely=0.95, anchor=CENTER)
        self.__frame_special.place(relx=0.97, rely=0.9, anchor=SE)

    def displace_frame(self):
        self.__frame_choose.place_forget()
        self.__frame_status.place_forget()
        self.__frame_map.place_forget()
        self.__frame_message.place_forget()
        self.__frame_special.place_forget()

    def get_root(self):
        return self.__frame_map


