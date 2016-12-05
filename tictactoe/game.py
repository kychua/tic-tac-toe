import board
import event
import util


class Game:

    """ Represent a game of tic tac toe. Keeps track of board
    and current player. Uses events to update board when moves are
    carried out in a game.

    """

    MSG_NEXT_TURN = "{name}, it's your turn!"
    MSG_TIE = "Game over. You have tied!"
    MSG_WIN = "{name} wins!"
    MSG_INVALID_MOVE = "That cell cannot be selected. Pls try again, {name}!"

    new_move_event = event.Event()
    new_game_event = event.Event()
    invalid_move_event = event.Event()
    
    def __init__(self, player1, player2, new_move_handler, new_board_handler, invalid_move_handler):
        self.player1 = player1
        self.player2 = player2
        self.board = board.Board()
        self._setup_handlers(new_move_handler, new_board_handler, invalid_move_handler)
        self.current_player = self.player1
        Game.new_game_event(Game.MSG_NEXT_TURN.format(name=self.current_player.name), self.board)
        
    @util.run_once
    def _setup_handlers(self, new_move_handler, new_board_handler, invalid_move_handler):
        Game.new_move_event.append(new_move_handler)
        Game.new_game_event.append(new_board_handler)
        Game.invalid_move_event.append(invalid_move_handler)

    def get_player_input(self):
        """ Get next move from current player if available.  """
        return self.current_player.get_next_move(self.board)
    
    def execute_move(self, cell):
        """ Mark given cell using current player's symbol.  """
        is_valid = self.current_player.make_move(self.board, cell)
        if is_valid:
            player = self.current_player
            self.current_player = self.current_player.opponent
            display_text = self._get_display_text(player)
            Game.new_move_event(cell, display_text, player, self.board.is_game_over, self.board)
        else:
            Game.invalid_move_event(Game.MSG_INVALID_MOVE.format(name=self.current_player.name))

    def _get_display_text(self, player):
        if self.board.is_game_over:
            if self.board.winner is not None:     
                display_text = Game.MSG_WIN.format(name=player.name)
            else:
                display_text = Game.MSG_TIE
        else:
            display_text = Game.MSG_NEXT_TURN.format(name=player.opponent.name)

        return display_text

    @property
    def is_over(self):
        return self.board.is_game_over

    @property
    def winner(self):
        if self.board.winner is None:
            return None
        elif self.player1.symbol == self.board.winner:
            return self.player1
        elif self.player2.symbol == self.board.winner:
            return self.player2
        else:
            return self.board.winner
