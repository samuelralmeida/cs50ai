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

    aa = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                aa.add((i, j))

    return aa


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid Action!!!")

    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        # check rows
        if board[i][0] != EMPTY and all(cell == board[i][0] for cell in board[i]):
            return board[i][0]
        
        # check collumns
        if board[0][i] != EMPTY and all(cell == board[0][i] for cell in [row[i] for row in board]):
            return board[0][i]

    # check diagonals
    if board[0][0] != EMPTY and all(cell == board[0][0] for cell in [board[i][i] for i in range(3)]):
        return board[0][0]

    if board[0][2] != EMPTY and all(cell == board[0][2] for cell in [board[i][2 - i] for i in range(3)]):
        return board[0][2]

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
            score = min_value(result(board, action), -math.inf)
            if best_score == None or score > best_score:
                best_score = score
                best_action = action
        
        elif p == O:
            score = max_value(result(board, action), math.inf)
            if best_score == None or score < best_score:
                best_score = score
                best_action = action

    return best_action


def max_value(board, highest_current_value):
    if terminal(board):
        return utility(board)
    
    lowest_possible_value = (-math.inf)
    for action in actions(board):
        lower_value = min_value(result(board, action), lowest_possible_value)
        if lower_value > highest_current_value:
            return lower_value
        
        lowest_possible_value = max(lowest_possible_value, lower_value)

    return lowest_possible_value


def min_value(board, lowest_curret_value):
    if terminal(board):
        return utility(board)
    
    highest_possible_value = math.inf
    for action in actions(board):
        higher_value = max_value(result(board, action), highest_possible_value)
        if higher_value < lowest_curret_value:
            return higher_value
        
        highest_possible_value = min(highest_possible_value, higher_value)

    return highest_possible_value