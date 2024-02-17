"""
Tic Tac Toe Player
"""

import math
import copy

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

    moves = 0
    for row in board:
        for collumn in row:
            if collumn != EMPTY:
                moves = moves + 1

    if (moves % 2) == 0:
        return X
    
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    aa = []
    for ridx, row in enumerate(board):
        for cidx, collumn in enumerate(row):
            if collumn == EMPTY:
                aa.append((ridx, cidx))

    return aa


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    result = copy.deepcopy(board)

    row, cell = action
    if result[row][cell] != EMPTY:
        raise NameError("invalid move")
    
    p = player(board)
    result[row][cell] = p
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] != EMPTY and (board[0][0] == board[0][1] == board[0][2]):
        return board[0][0]
    elif board[1][0] != EMPTY and (board[1][0] == board[1][1] == board[1][2]):
        return board[1][0]
    elif board[2][0] != EMPTY and (board[2][0] == board[2][1] == board[2][2]):
        return board[2][0]
    elif board[0][0] != EMPTY and (board[0][0] == board[1][0] == board[2][0]):
        return board[0][0]
    elif board[0][1] != EMPTY and (board[0][1] == board[1][1] == board[2][1]):
        return board[0][1]
    elif board[0][2] != EMPTY and (board[0][2] == board[1][2] == board[2][2]):
        return board[0][2]
    elif board[0][0] != EMPTY and (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    elif board[0][2] != EMPTY and (board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    if len(actions(board)) == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    p = player(board)
    aa = actions(board)

    best_action = ()
    best_score = None
    for action in aa:
        if p == X:
            score = min_value(result(board, action))
            if best_score == None or score > best_score:
                best_score = score
                best_action = action
        
        elif p == O:
            score = max_value(result(board, action))
            if best_score == None or score < best_score:
                best_score = score
                best_action = action

    return best_action


def max_value(board, menor_valor_atual=math.inf):
    if terminal(board):
        return utility(board)
    
    v = (-math.inf)
    for action in actions(board):
       menor_valor_obtido = min_value(result(board, action), v)
       if menor_valor_obtido > menor_valor_atual:
           return menor_valor_obtido
       
       v = max(v, menor_valor_obtido)

    return v


def min_value(board, maior_valor_atual=-math.inf):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        maior_valor_obtido = max_value(result(board, action), v)
        if maior_valor_obtido < maior_valor_atual:
            return maior_valor_obtido
        
        v = min(v, maior_valor_obtido)

    return v