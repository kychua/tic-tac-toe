class Player:
    """ Represents a player.  """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    @property
    def opponent(self):
        return self.__opponent

    @opponent.setter
    def opponent(self, opponent):
        self.__opponent = opponent
        opponent.__opponent = self

    def make_move(self, board, cell):
        return board.mark(cell, self.symbol)
