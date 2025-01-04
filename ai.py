from constants import Strings as String

class Obj(object):

    def __init__(self):

        self.__x = 0
        self.__y = 0
        self.__last_ship = []
        self.__time = 0

        # Setting up an empty array
        self.__mp = []  # True if the field is hit else False
        for y in range(12):
            row = []
            for x in range (12):
                row.append(False)
            self.__mp.append(row)

    def say(self, sms: str):
        """
        :param sms: str - the command, what should do the bot
        :return: tuple of two int - (x, y) coordinates
        """
        result = None
        if sms == String.GameFrame.BOT_SHOOT:
            result = self.__shoot()

        elif sms == String.GameFrame.BOT_HIT:
            if self.__time != 0:
                self.__last_ship.append((self.__x, self.__y))
            result = self.__hit()

        elif sms == String.GameFrame.BOT_DESTROYED:
            self.__last_ship.append((self.__x, self.__y))
            result = self.__destroyed()

        self.__time += 1
        print(">>> Bot1: shoot #%d - (%d, %d)" % (self.__time, result[0], result[1]))
        return result