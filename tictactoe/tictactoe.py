from copy import deepcopy
import math

"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    x_counter = 0
    o_counter = 0
    for row in board:
        x_counter += row.count(X)
        o_counter += row.count(O)
    
    if x_counter == o_counter:
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    valid_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                valid_moves.append((i, j))
                
    return valid_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = deepcopy(board)
    if boardcopy[action[0]][action[1]] != EMPTY:
        raise Exception("You must select an empty square for a valide move!")
    else:
        boardcopy[action[0]][action[1]] = player(board)
    return boardcopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        #For horizontal check
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != EMPTY):
            return board[i][0]
        #For vertical check
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != EMPTY):
            return board[0][i]
    #For diagnol check
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and (board[1][1] != EMPTY):
        return board[1][1]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        score = -math.inf
        best_action = None
        
        for action in actions(board):
            min_value = minvalue(result(board, action))
            
            if min_value > score:
                score = min_value
                best_action = action
        return best_action
        
    elif player(board) == O:
        score = math.inf
        best_action = None
    
        for action in actions(board):
            max_value = maxvalue(result(board, action))
            
            if max_value < score:
                score = max_value
                best_action = action
        return best_action
    
def maxvalue(board):
    if terminal(board):
        return utility(board)
    num = -math.inf
    for action in actions(board):
        num = max(num, minvalue(result(board, action)))
    return num

def minvalue(board):
    if terminal(board):
        return utility(board)
    
    num = math.inf
    for action in actions(board):
        num = min(num, maxvalue(result(board, action)))
    return num
        
    