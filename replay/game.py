from enum import Enum


class PlayerTurn(Enum):
    Ghost = "fantome"
    Inspector = "inspecteur"


class Turn:
    def __init__(self, turn, score, shadow, block):
        self.turn = turn
        self.score = score
        self.shadow = shadow
        self.block = block
        self.players = []
        self.steps = []

    def __str__(self):
        return "turn [{}] score [{}] shadow [{}] block [{}]".format(self.turn, self.score, self.shadow, self.block)


class Step:
    def __init__(self):
        self.question = ""
        self.answer = 0
        self.interpretation = ""
        self.extra_information = ""


class StepPiece(Step):
    def __init__(self):
        super().__init__()


class StepPower(Step):
    def __init__(self):
        super().__init__()


class StepMove(Step):
    def __init__(self):
        super().__init__()
