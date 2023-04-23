from copy import deepcopy
import pygame

RED = (255, 0, 0)
GREEN = (255, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def minimax(position, depth, alpha, beta, max_player, game):
    '''alpha maximum score can max get and beta minimum, if for each branch the alpha which is max be greater that beta which is min, cut that branch'''

    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth - 1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, alpha, beta, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return minEval, best_move


def minimax2(position, depth, alpha, beta, max_player, game):
    '''alpha maximum score can max get and beta minimum, if for each branch the alpha which is max be greater that beta which is min, cut that branch'''

    if depth == 0 or position.winner() is not None:
        return position.evaluate2(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth - 1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, alpha, beta, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    '''we get the row and column and move the piece to those and if we jumped over the piece, remove that piece'''
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    '''this is the successor function which stores all the valid moves of AI in moves list. then it calls simulating move function and update the copy of board based on the movement of piece'''
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # after each move a copy of board and pieces with new moves will be showed
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves
