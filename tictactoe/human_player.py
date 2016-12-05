import player

class HumanPlayer(player.Player):
    MSG_REQUEST_USER_INPUT = "Pls enter the cell (from 0 to 8) you'd like to mark: "

    def __init__(self, name, symbol, is_cli=False):
        super().__init__(name, symbol)
        self.is_cli = is_cli

    def get_next_move(self, board):
        if self.is_cli:
            cell = int(input(HumanPlayer.MSG_REQUEST_USER_INPUT))
        else:  # wait for user callback
            cell = None
        return cell
