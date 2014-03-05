'''
Created on Mar 5, 2014

@author: Nick Crawford
'''

from pieces import colors

def material_score(board, game):
    if game.rules.is_checkmate(colors.WHITE, board):
        return float('inf')
    elif game.rules.is_checkmate(colors.BLACK, board):
        return float('-inf')
    elif game.rules.is_draw(board, game.positions):
        return 0
    else:
        score = 0
        for piece in board.pieces.itervalues():
            if piece is not None:
                score += piece.color * piece.value
    return score