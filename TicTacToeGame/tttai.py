# Narayan Khanal
# Assignment 10: Tic Tac Toe Game
# CS 195 001 
# FileName: tttai.py

#import random module
import random

#import user defined function getValidMoves from tttlib 
from tttlib import getValidMoves

def randomBotMove(mySpaces:set, opponentSpaces:set) -> str:
    """Get a random valid tic-tac-toe move."""
    validMoves = getValidMoves(mySpaces|opponentSpaces)
    validMoves = list(validMoves)
    return random.choice(validMoves)