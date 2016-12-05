import ui

class Cli(ui.Ui):
    
    """ Represent command line user interface. """

    def __init__(self, qtable_pickle_file, alpha=0.1, gamma=0.9, delta=0.0, epsilon=0.9):
        self.alpha = alpha
        self.gamma = gamma
        self.delta = delta
        self.epsilon = epsilon
        super().__init__(qtable_pickle_file, True)
        
    def update_invalid_move(self, display_text):
        print(display_text)
