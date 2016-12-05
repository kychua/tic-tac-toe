import abc

import computer_player
import human_player
import qlearning
import session


class Ui:
    __metaclass__ = abc.ABCMeta

    def __init__(self, qtable_pickle_file, is_cli):
        self._is_cli = is_cli
        self.qtable_pickle_file = qtable_pickle_file
        self._start()

    def _start(self):
        player1, player2 = self._get_players()
        self._start_session(player1, player2)

    def _get_players(self):
        p1_name, p2_name, is_against_ai = self._request_user_data()
        player1, player2 = self._create_players(p1_name, p2_name, is_against_ai)
        return player1, player2

    def _start_session(self, player1, player2):
        self.session = session.Session(player1, player2, self.update_new_move, self.update_new_game, self.update_invalid_move)
        self.session.start()

    def _create_players(self, p1_name, p2_name, is_against_ai):
        player1 = human_player.HumanPlayer(p1_name, "O", self._is_cli)
        if is_against_ai:
            q = qlearning.QLearning(self.qtable_pickle_file)
            player2 = computer_player.ComputerPlayer("Computer", "X", True, q)
        else:
            player2 = human_player.HumanPlayer(p2_name, "X", self._is_cli)
        return player1, player2

    @abc.abstractmethod
    def update_new_move(self, cell, display_text, player, is_game_over, board):
        """ Update display when a cell is marked.
            Mark provided cell with player's symbol and display output message.
        """
        return

    @abc.abstractmethod
    def update_new_game(self, text, board):
        """ Update display when new game is started.  """
        return

    @abc.abstractmethod
    def update_invalid_move(self, display_text):
        """ Update display when invalid move is submitted.  """
        return
