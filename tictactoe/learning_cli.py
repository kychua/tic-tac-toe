import cli
import qlearning
import session
import computer_player


class LearningCli(cli.Cli):

    """ Represent command line user interface for machine learning.
    Displays statistics instead of player interactions.  

    """

    def _start(self):
        q = qlearning.QLearning(self.qtable_pickle_file, self.alpha, self.gamma, self.delta, self.epsilon)
        player1, player2 = self.create_computer_players(q)
        self.rounds = int(input('Enter no. of rounds: '))
        self.session = session.Session(player1, player2, self.update_new_move, self.update_new_game, self.update_invalid_move)
        self.session.run(self.rounds)
    
    def update_new_game(self, text, board):
        pass

    def update_new_move(self, cell, display_text, player, is_game_over, board):
        pass

    def create_computer_players(self, qlearning):
        player1 = computer_player.ComputerPlayer("MAX", "X", True, qlearning)
        player2 = computer_player.ComputerPlayer("min", "O", False, qlearning)
        return player1, player2

