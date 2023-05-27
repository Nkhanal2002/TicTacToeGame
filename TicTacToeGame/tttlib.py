# Narayan Khanal
# Assignment 10: Tic Tac Toe Game
# CS 195 001 
# FileName: tttlib.py

# Constant variables 
BOARD_SPACES = '1','2','3','4','5','6','7','8','9' #board spaces with string values
WINNERS = (('1','2','3'), #rows         # winners combination as a tuple of different tuple combinations
           ('4','5','6'),
           ('7','8','9'),   
           ('1','4','7'), #columns
           ('2','5','8'), 
           ('3','6','9'), 
           ('1','5','9'), #diagonals
           ('3','5','7'))  

def displayBoard(xSpaces:set,oSpaces:set):
    # set up the board, replace spaces with x's and o's
    board = list(BOARD_SPACES)
    for i, space in enumerate(board):
        if space in xSpaces:
            board[i] = 'X'
        elif space in oSpaces:
            board[i] = 'O'
    #clear screen 
    print('\033[H\033[2J', end='')
    print("<---TIC_TAC_TOE GAME BY NARAYAN KHANAL--->\n")
    
    #display board
    print(f'{board[0]} | {board[1]} | {board[2]}' )
    print('---+---+---')
    print(f'{board[3]} | {board[4]} | {board[5]}' )
    print('---+---+---')
    print(f'{board[6]} | {board[7]} | {board[8]}' )

def isWinner(spaces:set) -> bool:
    """Returns True if spaces includes any of the combinations in WINNERS."""
    for combo in WINNERS:
        if spaces. issuperset(combo):
            return True

def getValidMoves(takenSpaces:set) -> set:
    """Returns a set of BOARD_SPACES that are not in taken Spaces."""
    return set(BOARD_SPACES)-takenSpaces

def playGame(playerXmove:callable,playerOmove:callable):
    """Returns 'X' if the winner used xSpaces, None/False if the game is draw, and 'O' if the winner used oSpaces."""
    #initiate the board
    xSpaces = set()
    oSpaces = set()
    #game loop
    while True:
        #X moves
        move = playerXmove(xSpaces,oSpaces)
        xSpaces.add(move)
        if isWinner(xSpaces):
            displayBoard(xSpaces,oSpaces)
            print("X wins!")
            return 'X'

        elif not getValidMoves(xSpaces|oSpaces):
            print('Draw')
            return ''

        # O moves
        move = playerOmove(oSpaces,xSpaces)
        oSpaces.add(move)
        if isWinner(oSpaces):
            print("O wins!")
            return 'O'

def humanMove(mySpaces:set,opponentSpaces:set) -> str: 
    """Returns two players move depending on length of mySpaces and opponentSpaces."""
    validSpace = getValidMoves(mySpaces|opponentSpaces)
    if len(opponentSpaces)>len(mySpaces): # we are playing as O's 
        displayBoard(opponentSpaces, mySpaces)
        print("You are playing as O's")
    else: #we are playing as X's
        displayBoard(mySpaces,opponentSpaces)
        print("You are playing as X's")
    move = input("Please enter a valid move: ")
    while move not in validSpace:
        print('Invalid move!')
        move = input("Please select a valid move: ")
    return move

if __name__=='__main__': 
    playGame(humanMove,humanMove)