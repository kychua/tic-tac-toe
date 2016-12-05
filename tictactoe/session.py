import game

class Session:

    """ Represent a user session.  """

    def __init__(self, player1, player2, board_update_handler, new_game_handler, invalid_move_handler):
        player1.opponent = player2
        self.player_1 = player2  # players are swapped when new game starts
        self.player_2 = player1

        self.board_update_handler = board_update_handler
        self.new_game_handler = new_game_handler
        self.invalid_move_handler = invalid_move_handler

    def start_new_game(self):
        """ Start a new game of tic tac toe. Players take turns to start.  """
        self._swap_players()
        self.game = game.Game(self.player_1, self.player_2, self.board_update_handler, self.new_game_handler, self.invalid_move_handler)
        self.trigger_next_turn()

    def execute_next_move(self, cell):
        """ Mark provided cell as next move.  """
        self.game.execute_move(cell)
        self.trigger_next_turn()
   
    def trigger_next_turn(self):
        """ Start next turn (for cases where input must be requested). 
        If input is user-initiated, do nothing. (wait for callback) 
        """
        if not self.game.is_over:
            cell = self.game.get_player_input()
            if cell is not None:
                self.execute_next_move(cell)
        
    def _swap_players(self):
        player = self.player_1
        self.player_1 = self.player_2
        self.player_2 = player

    def start(self, rounds=1):
        """ Start a game of tic-tac-toe.  """
        while rounds > 0:
            self.start_new_game()
            rounds -= 1

    def run(self, rounds):
        """ Automatically run multiple games of tic-tac-toe.  """
        total_games = rounds
        p1 = self.player_1.symbol
        p2 = self.player_2.symbol
        wins = { p1 : 0, p2 : 0 }

        while (rounds > 0):
            self.start_new_game()
            winner = self.game.winner
            
            if winner is not None:
                wins[winner.symbol] += 1
            rounds -= 1
            self.player_1.qlearning.update_parameters(total_games, rounds)
            if rounds % 100 == 0:
                percentage_wins = wins[p2]/(wins[p2] + wins[p1] + 1) * 100
                print(p2 + " has won " +  str(percentage_wins) + " games" )
        print(wins)