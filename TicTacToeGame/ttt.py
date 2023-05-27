# Narayan Khanal
# Assignment 10: Tic Tac Toe Game
# CS 195 001 
# FileName: ttt.py


#import sys module
import sys

#import humanMove and playGame functions from tttlib
from tttlib import humanMove, playGame

#import randomBotMove function from tttai
from tttai import randomBotMove

INSTRUCTIONS = """
Please run:
    python ttt.py PlayerType
        where PlayerType is 
            h - human
            r - randomBot
"""
PLAYERS_TYPES = {
    "h": humanMove,
    "r": randomBotMove
}
if __name__=="__main__":
    if len(sys.argv) == 3 and sys.argv[1] in PLAYERS_TYPES and sys.argv[2] in PLAYERS_TYPES:
        playGame(PLAYERS_TYPES[sys.argv[1]],PLAYERS_TYPES[sys.argv[2]])
    else:
        print(INSTRUCTIONS)
