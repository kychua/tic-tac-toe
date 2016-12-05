import pickle
import random


class QLearning:
    """ Stores data relevant to Q-learning (Q table and parameters)
    and provides relevant methods.  """

    def __init__(self, qtable_pickle_file, alpha=0.1, gamma=0.9, delta=0.0, epsilon=0.9):
        self.qtable_pickle_file = qtable_pickle_file
        try:
            self.qtable = self._load_qtable()
        except (OSError, IOError) as e:
            self.qtable = {}
            self._save_qtable()

        self.discount = gamma
        self.learning_rate = alpha
        self.epsilon = epsilon
        self.increase_in_epsilon = delta

    def _load_qtable(self):
        return pickle.load(open(self.qtable_pickle_file, "rb"))

    def _save_qtable(self):
        pickle.dump(self.qtable, open(self.qtable_pickle_file, "wb"))

    def update_parameters(self, total_games, games_left):
        """ Updates parameters after fixed number of games
        and saves qtable periodically.
        """
        rounds = total_games - games_left
        if rounds % 5000 == 0:
            self.epsilon += self.increase_in_epsilon
        if rounds % 1000 == 0:
            self._save_qtable()

    def get_state(self, board, player):
        """ Convert board and player into a string represent state.  """
        return ''.join(x for x in board.cells) + player.symbol

    def update_qvalues(self, cell, original_player, original_state, action_reward, new_board):
        """ Update Q-table values for original state using value for new state
         resulting from move (cell) chosen and reward for choosing said move.
        """
        if new_board.is_game_over:
            expected = action_reward
        else:
            qvalues = self.get_or_create_qvalues(new_board, original_player.opponent)
            if original_player.is_maximising:
                # opponent min_player will pick lowest value action
                future_outcome = min(qvalues.values())
            else:
                # opponent max_player will pick highest value action
                future_outcome = max(qvalues.values())
            expected = action_reward + (self.discount * future_outcome)
        change = self.learning_rate * (expected - self.qtable[original_state][cell])
        self.qtable[original_state][cell] += change

    def get_or_create_qvalues(self, board, player):
        """ Get dictionary of possible moves (cells) and their values from 
        Q-table, given state (board, player). Creates dictionary of moves 
        and their values (values follow uniform random distribution 
        with values in [-0.15, 0.15]) if no such dictionary exists.
        """
        state = self.get_state(board, player)
        if state not in self.qtable:
            available_cells = board.get_available_cells()
            qvalues = {}
            for cell in available_cells:
                qvalues[str(cell)] = random.uniform(-0.15, 0.15)
            self.qtable[state] = qvalues
        return self.qtable[state]
