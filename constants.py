LIST_OF_SHIPS = (5, 4, 3, 3, 2)

BOT_SHOOT_TIME = {"shoot": 1000, "hit": 1500, "destroyed": 1500}


class Strings:
    APP_NAME = "BattleShip"
    APP_MUSIC = "resources/sound.wav"

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
        BUTTON_RANDOM = "Arrange randomly".upper()
        BUTTON_START = "Start >>".upper()
        BUTTON_CLEAR_ALL = "Clear all".upper()
        BUTTON_BACK_MENU = "Back to menu".upper()
        WARNING_ALL_SHIPS_PUT = "All %s ships have been placed!"
        WARNING_SHIPS_CLEARED = "The map has been cleared!"
        WARNING_PUT_ALL_SHIPS = "Place all ships before start game!"
        WARNING_CAN_START = "All ships have been arranged. You can start game."
        WARNING_CANNOT_PUT = "%s cannot be placed here!"
        WARNING_EMPTY_MAP = "The map is empty to clear!"

        DIALOG_BACK_MENU = "Do you really want to go back to menu?"
        DIALOG_CLEAR_ALL = "Do you really want to clear all ships from the map?"

        SHIPS = [
            (5, "BATTLESHIP"),
            (4, "CRUISER"),
            (3, "DESTROYER"),
            (2, "SUBMARINE")
        ]

    class GameFrame:
        TITLE_VICTORY = "Victory"
        TITLE_DEFEAT = "Defeat"
        MSG_VICTORY = "Congratulations!\nYou won the battle."
        MSG_DEFEAT = "Unfortunately.\nYou lost the battle."
        PLAYER_SHIPS = "You:"
        ENEMY_SHIPS = "Enemy:"
        TURN_OF_PLAYER = "Your turn.".upper()
        TURN_OF_ENEMY = "The enemy's turn.".upper()
        WARNING_MISS = "miss!".upper()
        WARNING_HIT = "hit!".upper()
        WARNING_SHIP_DESTROYED = "Destroyed a ship!"
        WARNING_TURN_OF_ENEMY = "Now is the enemy's turn"
        WARNING_LAST_SHOT = "Last hit field: %s.  "

        BOT_SHOOT = "shoot"
        BOT_HIT = "hit"
        BOT_DESTROYED = "destroyed"
        BOT_ERROR = "error"

    class HelpFrame:
        MSG_HELP = """
Players:
•   2

Objective:
•   Sink all the opponent's ships.

Setup:
•   Each player arranges their ships on a hidden grid.

Gameplay:
•   Players take turns guessing grid coordinates to locate and hit the opponent's ships.
•   A ship is sunk when all its sections have been hit.
•   The first player to sink all enemy ships wins.

Tips:
•   Plan strategically based on your hits and misses.
•   Keep track of your attempts to increase hit accuracy.

Enjoy the game!

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
    HELP_MSG = "#000080"

    class MenuFrame:
        BACKGROUND_BUTTONS = "#000"

    class PreStartFrame:
        BUTTON_BACK = "#000"
        BUTTON_ARRANGE = "#000"
        BUTTON_RANDOM = "#000"