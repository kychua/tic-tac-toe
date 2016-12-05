class Board:
    """Represent a board for tic-tac-toe.

    Row 0 [0, 1, 2]
    Row 1 [3, 4, 5]
    Row 2 [6, 7, 8]
    """

    DIAGONALS_INDICES = [[0, 4, 8], [2, 4, 6]]
    BLANK = '-'

    @staticmethod
    def has_identical_elements(lst):
        # https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
        # http://stackoverflow.com/q/3844948/
        return not lst or lst.count(lst[0]) == len(lst)

    def __init__(self):
        self.cells = [Board.BLANK]*9
        self.winner = None
        self.filled_cells = 0
        
    @property
    def is_game_over(self):
        return self.winner != None or self.filled_cells == 9

    def mark(self, cell, symbol):
        if self.cells[cell] != Board.BLANK:
            return False
        self.cells[cell] = symbol
        self.filled_cells += 1
        is_winning_move = self.is_winning_move(cell)
        if is_winning_move:
            self.winner = symbol
        return True

    def get_available_cells(self):
        return [i for i, cell_value in enumerate(self.cells) if cell_value == Board.BLANK]

    def __str__(self):
        row_sep = '\n-----\n'
        # cells = [cell for cell in self.cells]
        board_str = row_sep.join('|'.join(self.cells[i:i+3]) for i in range(0, len(self.cells), 3))
        return board_str

    def is_winning_move(self, cell):
        paths = self.get_paths(cell)
        for path in paths:
            if self.has_identical_elements(path):
                return True
        return False

    def get_paths(self, cell):
        row = self.get_row(cell)
        col = self.get_col(cell)
        diags = self.get_diags(cell)
        return [row, col] + diags

    def get_diags(self, cell):
        DIAGONALS_INDICES = [i for i in self.DIAGONALS_INDICES if cell in i]
        diagonals = []
        for diagonal_indices in DIAGONALS_INDICES:
            diagonal = self.get_elements(self.cells, diagonal_indices)
            diagonals.append(diagonal)
        return diagonals

    def get_row(self, cell):
        first_element = cell // 3 * 3
        indices = [first_element, first_element + 1, first_element + 2]
        return self.get_elements(self.cells, indices)

    def get_col(self, cell):
        first_element = cell % 3
        indices = [first_element, first_element + 3, first_element + 6]
        return self.get_elements(self.cells, indices)

    @staticmethod
    def get_elements(lst, indices):
        return [lst[i] for i in indices]



