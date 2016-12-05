import sys

import tkinter as tk

import player_input_dialog
import ui


class Gui(tk.Frame, ui.Ui):
    def __init__(self, qtable_pickle_file, master=None):
        self._create_window(master)
        self._create_frames()        
        self._create_widgets()

        self._is_cli = False

        ui.Ui.__init__(self, qtable_pickle_file, False)

    def _create_frames(self):
        self._create_display_frame()
        self._create_board_frame()
        self._create_reset_frame()

    def _create_window(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.master.minsize(width=250, height=330)

        self.master.grid_propagate(False)
        self.master.columnconfigure(0, weight=1) # fill frame
        self.master.rowconfigure(0,weight=1) 

    def _create_display_frame(self):
        self._display_frame = tk.Frame(self.master, width=250, height=50)
        self._display_frame.grid()

    def _create_board_frame(self):
        self._board_frame = tk.Frame(self.master, width=250, height=250, borderwidth=20)
        self._board_frame.grid(row=2)

    def _create_reset_frame(self):
        self._reset_frame = tk.Frame(self.master, width=250, height=30)
        self._reset_frame.grid(row=3)      

    def _create_widgets(self):
        self._create_display_widget()
        self._create_cells()
        self._create_reset_button()
    
    def _create_display_widget(self):
        self.display_text = tk.StringVar()
        self.display_label = tk.Label(self._display_frame, textvariable=self.display_text)
        self.display_label.grid()
        self.display_text.set("Welcome!")

    def _create_cells(self):
        self.cells = []
        for i in range(0, 9):
            button = self._create_cell(i)
            self.cells.append(button)

    def _create_cell(self, cell):
        frame = tk.Frame(self._board_frame, width=70, height=70)
        button = tk.Button(frame, text=" ", command=lambda i=cell: self._submit_chosen_cell(i)) 
        
        frame.grid_propagate(False)  # disables resizing of frame
        frame.columnconfigure(0, weight=1)  # enables button to fill frame
        frame.rowconfigure(0,weight=1)  # any positive number would do the trick

        frame.grid(row=cell // 3, column=cell%3)
        button.grid(sticky="wens") #makes the button expand

        return button

    def _create_reset_button(self):
        self._reset_button = tk.Button(self._reset_frame, text="Reset", command=self._reset)
        self._reset_button.grid()

    def _request_user_data(self):
        dialog = player_input_dialog.PlayerInputDialog(self.master)
        if dialog.result is None:  # user pressed quit in dialog
            self.master.destroy()
            sys.exit()
        return dialog.result

    def _reset(self):
        self.session.start_new_game()

    def _submit_chosen_cell(self, cell):
        self.session.execute_next_move(cell)

    def _mark_cell(self, cell, symbol):
        self.cells[cell].configure(text=symbol, state="disabled", relief=tk.SUNKEN)

    def _disable_cells(self):
        for cell in self.cells:
            cell.configure(state="disabled", relief=tk.SUNKEN)

    def update_new_move(self, cell, display_text, player, is_game_over, board):
        """ Update display when a cell is marked.
            Mark provided cell with player's symbol and display output message.
        """
        self._mark_cell(cell, player.symbol)
        self.display_text.set(display_text)
        if is_game_over:
            self._disable_cells()

    def update_new_game(self, text, board):
        """ Update display when new game is started.  """
        self.display_text.set(text)
        for cell in self.cells:
            cell.configure(text=" ", state="normal", relief=tk.RAISED)
