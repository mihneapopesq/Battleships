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

    def __shoot(self):
        """
        Calls when the bot receives "shoot" command
        :return: tuple of two ints - x and y, coordinate of the bot's chose
        """
        if not self.__last_ship:
            x = self.__random(1, 10)
            y = self.__random(1, 10)

            if not self.__mp[y][x]:
                self.__x = x
                self.__y = y

                self.__mp[y][x] = True
                self.__print_map()
                return x, y

            return self.__shoot()
        else:
            return self.__hit()

    def __hit(self):
        """
        Calls when the bot receives "hit" command
        :return: tuple of two ints - x and y, coordinate of the bot's chose
        """
        print("Bot's hit last ship: ", self.__last_ship)
        result = ()

        if len(self.__last_ship) == 1:
            result = self.__get_one_of_four()

        elif len(self.__last_ship) > 1:
            if self.__last_ship[0][0] != self.__last_ship[1][0]:  # is horizontal
                result = self.__get_right_or_left()
            else:
                result = self.__get_top_or_bottom()

        self.__x = result[0]
        self.__y = result[1]

        self.__mp[result[1]][result[0]] = True
        return result