import numpy as np

import player
import random


class ComputerPlayer(player.Player):

    def __init__(self, name, symbol, is_maximising, qlearning):
        super().__init__(name, symbol)
        self.is_maximising = is_maximising
        self.qlearning = qlearning

    def get_next_move(self, board):
        """ Get cell to mark.  """
        qvalues = self.qlearning.get_or_create_qvalues(board, self)
        return self._pick_move(qvalues)

    def _pick_move(self, qvalues):
        """ Pick cell according to Q-learning algorithm.
        Picks best cell with probability self.qlearning.epsilon.
        Otherwise picks cell randomly with cells with higher values having 
        higher probability of being picked.  
        """
        unif = random.random()
        if unif < self.qlearning.epsilon: # greedy
            cell = self._greedy_pick_cell(qvalues)
        else: # random
            cell = self._random_pick_cell(qvalues)
        return cell

    def _greedy_pick_cell(self, qvalues):
        if self.is_maximising:
            return int(max(qvalues, key=qvalues.get))
        else:
            return int(min(qvalues, key=qvalues.get))

    def _random_pick_cell(self, qvalues):
        if not self.is_maximising:
            # picking min(x) is equivalent to picking max(-x)
            self._change_to_negative_values(qvalues)
        return self._pick_weighted_random_move(qvalues)

    def _change_to_negative_values(self, qvalues):
        for i, v in qvalues.items():
                qvalues[i] = -qvalues[i]
                
    def _pick_weighted_random_move(self, qvalues):
        """ Randomly pick cell (from qvalues' keys), weighted by value (qvalue).  
        Cells with higher values have a higher probability of being picked.
        Cells with negative values are handled by adding a constant to every
        value such that all values are positive.
        """

        probabilities = [0] * 9
        
        min_val = min(qvalues.values())
        if min_val <= 0:  # handle negative values
            constant = abs(min_val) + 0.1
        else: 
            constant = 0
        for x in qvalues.keys():
            probabilities[int(x)] = qvalues[x] + constant  
        
        probabilities = np.cumsum(probabilities)
        rand = random.uniform(0, probabilities[8])
        cell = next(i for i, v in enumerate(probabilities) if v >= rand)
        return cell

    def make_move(self, board, cell):
        """ Mark provided cell with own symbol and update Q-table accordingly.  """
        state = self.qlearning.get_state(board, self)
        is_valid_move = board.mark(cell, self.symbol)

        if not is_valid_move:
            return False

        reward = self._get_reward(board)

        self.qlearning.update_qvalues(str(cell), self, state, reward, board)
        return is_valid_move

    def _get_reward(self, board):
        reward = 0
        if board.is_game_over and board.winner is not None:
            if self.is_maximising:
                reward = 1
            else:
                reward = -1
        return reward
