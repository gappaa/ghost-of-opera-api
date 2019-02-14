from enum import Enum


class PlayerState(Enum):
    Suspect = 'suspect'
    Clean = 'clean'


class Player:
    def __init__(self, player):
        self._color, self._number, self._state = player.split('-')

    @property
    def color(self):
        return self._color

    @property
    def number(self):
        return self._number

    @property
    def state(self):
        return PlayerState(self._state)

    def __str__(self):
        return "color [{}] number [{}] state [{}]".format(self._color, self._number, self._state)
