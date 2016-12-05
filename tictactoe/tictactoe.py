import argparse

from tkinter import Tk

import game_cli
import gui
import learning_cli

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--learn", help="Plays computer against itself", action="store_true")
parser.add_argument("-q", "--qtable", help="File to store qtable", default="computer.pickle")
parser.add_argument("-c", "--cli", help="Play CLI version of tic tac toe", action="store_true")
parser.add_argument("-a", "--alpha", help="Learning rate", type=float, default="0.1")
parser.add_argument("-g", "--gamma", help="Discount rate", type=float, default="0.9")
parser.add_argument("-d", "--delta", help="Rate of change of epsilon", type=float, default="0.0")
parser.add_argument("-e", "--epsilon", help="Probability of using greedy instead of random", type=float, default="0.9")

args = parser.parse_args()

# def restricted_float(x):
#     x = float(x)
#     if x >= 0.0 and x <= 1.0:
#         raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]"%(x,))
#     return x

# p = argparse.ArgumentParser()
# p.add_argument("--arg", type=restricted_float)

qtable_pickle_file = args.qtable

if args.learn:
    learning_cli.LearningCli(args.qtable, args.alpha, args.gamma, args.delta, args.epsilon)
elif args.cli:
    game_cli.GameCli(args.qtable, args.alpha, args.gamma, args.delta, args.epsilon)
else:
    root = Tk()
    gui.Gui(args.qtable, root)
    root.mainloop()
