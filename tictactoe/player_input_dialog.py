import tkinter as tk
from tkinter import simpledialog


class PlayerInputDialog(simpledialog.Dialog):

    def body(self, master):
        self.is_play_with_com = False

        tk.Label(master, text="Player 1: ").grid(row=0)
        tk.Label(master, text="Player 2: ").grid(row=1)
        
        self.player_1_e = tk.Entry(master)
        self.player_2_e = tk.Entry(master)

        self.player_1_e.grid(row=0, column=1)
        self.player_2_e.grid(row=1, column=1)
        
        self.play_with_com_v = tk.IntVar()
        play_with_com_cb = tk.Checkbutton(master, text="Play with computer", command=self._toggle_player_2_e, variable=self.play_with_com_v)
        play_with_com_cb.grid(row=2, columnspan=2)

        return self.player_1_e # initial focus

    def buttonbox(self):
        box = tk.Frame(self)

        w = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Quit", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def _toggle_player_2_e(self):
        if self.play_with_com_v.get() == 1:
            self.player_2_e.configure(state='disabled')
            self.is_play_with_com = True
        else:
            self.player_2_e.configure(state='normal')
            self.is_play_with_com = False

    def apply(self):
        player_1_name = self.player_1_e.get()
        if self.is_play_with_com:
            player_2_name = None
        else:
            player_2_name = self.player_2_e.get()        
        self.result = player_1_name, player_2_name, self.is_play_with_com
