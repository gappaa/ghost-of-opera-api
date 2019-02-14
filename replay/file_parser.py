from enum import Enum
import re
from player import Player
from game import Turn


class ParserEnum(Enum):
    StartParser = ""
    BeforeInformationTurn = "!!!"
    InformationTurn = "**************************"
    AfterInformationTurn = "****"


class Parser:
    def __init__(self, logger):
        self.turn = []
        self._parser_state = ParserEnum.StartParser
        self._logger = logger
        self._cpt = 0

    def parse(self, file):
        with open(file, 'r') as fd:
            for line in iter(lambda: fd.readline(), ''):
                line = line.rstrip()

                if line == ParserEnum.InformationTurn.value:
                    self._logger.info('begin turn')
                    self._parser_state = ParserEnum.InformationTurn
                    self._cpt = 0
                    continue
                elif line == ParserEnum.AfterInformationTurn.value:
                    self._logger.info('end turn\n')
                    self._parser_state = ParserEnum.AfterInformationTurn
                    self._cpt = 0
                    continue

                if self._parser_state == ParserEnum.InformationTurn:
                    if self._cpt == 0:
                        i = self._store_turn_information(line)
                        self._logger.info(i)
                    elif self._cpt == 1:
                        i = self._store_players_information(line)
                        self._logger.info('\n'.join([_.__str__() for _ in i]))
                    self._cpt += 1

    @staticmethod
    def _store_turn_information(line):
        p = list(filter(lambda k: k != '', re.split(r'^Tour:(.*), Score:(.*), Ombre:(.*), Bloque:(.*)$', line)))
        return Turn(p[0], p[1], p[2], p[3])

    @staticmethod
    def _store_players_information(line):
        try:
            p = list(map(Player, filter(lambda k: k != '', re.split(r'\s+', line))))
        except ValueError as e:
            return []
        return p


class StateParser:
    def __init__(self):
        self._state = 0


class StepParser:
    def __init__(self):
        pass


class TurnParser:
    def __init__(self):
        pass
