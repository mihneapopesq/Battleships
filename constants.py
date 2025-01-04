LIST_OF_SHIPS = (1, 1, 2, 1)
BOT_SHOOT_TIME = {"shoot": 1000, "hit": 1500, "destroyed": 1500}


class Strings:
    APP_NAME = "BattleShip"

    class MenuFrame:
        TITLE = "Menu:"
        BUTTON_START = "GAME"
        BUTTON_HELP = "HELP"
        BUTTON_EXIT = "EXIT"
        EXIT_DIALOG_MSG = "Do you really want to exit?"

    class StatusFrame:
        MSG_CHOSE = "Ships:"
        MSG_CHOSEN = "Ship:"
        MSG_MAP = "MAP"
        HEADER_TYPE = "Type:"
        HEADER_AMOUNT = "Amount:"
        HEADER_ORIENTATION = "Orientation:"
        BUTTON_CHANGE = "Change orientation"

        DIALOG_BACK_MENU = "Do you really want to go back to menu?"
        DIALOG_CLEAR_ALL = "Do you really want to clear all ships from the map?"

        SHIPS = [(1, "BATTLESHIP"),
                 (1, "CRUISER"),
                 (2, "DESTROYER"),
                 (1, "SUBMARINE")]

    class GameFrame:
        TITLE_VICTORY = "Victory"
        TITLE_DEFEAT = "Defeat"
        MSG_VICTORY = "Congratulations!\nYou won the battle."
        MSG_DEFEAT = "Unfortunately.\nYou lost the battle."
        PLAYER_SHIPS = "You:"
        ENEMY_SHIPS = "Enemy:"

        BOT_SHOOT = "shoot"
        BOT_HIT = "hit"
        BOT_DESTROYED = "destroyed"
        BOT_ERROR = "error"

    class HelpFrame:
        MSG_HELP = """
        Players:
•   2

        Goal:
•   Sink all of your opponent’s ships

        Setup:
•   Each player places ships on the bottom grid

        Rules:
•   Take turns firing shots by calling out grid coordinates
•   Mark shots you fire on the vertical target grid
        """


class MyExceptions:
    MAP_ERROR = "MapError"


class Dimensions:
    APP_MAX_WIDTH = 1000
    APP_MAX_HEIGHT = 600

    APP_MIN_WIDTH = 1000
    APP_MIN_HEIGHT = 600



class Colors:

    MAP_COLOR = "white"
    SHIP_COLOR = "green"
    ERROR_COLOR = "red"
    BACK_BUTTON = "blue"
    DESTROYED_SHIP = "#7c0d0f"
    DESTROYED_PART = "red"
    BROKEN_POINT = "yellow"
    HELP_MSG = "#079b5b"

    class MenuFrame:
        BACKGROUND_BUTTONS = "#000"

    class PreStartFrame:
        BUTTON_BACK = "#000"
        BUTTON_ARRANGE = "#000"
        BUTTON_RANDOM = "#000"
