import cli


class GameCli(cli.Cli):

    """ Represent command line user interface for interactive play. """

    MSG_REQUEST_NAME = 'Enter your name: '
    MSG_ASK_IF_AGAINST_COMPUTER = "Would you like to play against the computer? "
    MSG_GREET_PLAYER = 'Hello, {name}'

    def update_new_game(self, text, board):
        print('====================NEW GAME===================')
        print(text)
        print(board)

    def update_new_move(self, cell, display_text, player, is_game_over, board):
        print(display_text)
        print(board)

    def _request_user_data(self):
        p1_name = input(GameCli.MSG_REQUEST_NAME)
        print(GameCli.MSG_GREET_PLAYER.format(name=p1_name))

        is_playing_with_computer = input(GameCli.MSG_ASK_IF_AGAINST_COMPUTER)

        if is_playing_with_computer == "n":
            p2_name = input(GameCli.MSG_REQUEST_NAME)
            print(GameCli.MSG_GREET_PLAYER.format(name=p2_name))
            is_playing_with_computer = False
        else:
            p2_name = None
            is_playing_with_computer = True

        return p1_name, p2_name, is_playing_with_computer
