'''
Created on Jun 21, 2013

@author: nick
'''

from util import enum

colors = enum(WHITE=0, BLACK=1)
pieces = enum(PAWN=0, KNIGHT=1, BISHOP=2, ROOK=3, QUEEN=4, KING=5)

def to_utf2(piece, color):
    return '%s_%s' % (color, piece)

def to_utf(piece, color):
    if color == colors.WHITE:
        if piece == pieces.KING:
            return unichr(9812)
        elif piece == pieces.QUEEN:
            return unichr(9813)
        elif piece == pieces.ROOK:
            return unichr(9814)
        elif piece == pieces.BISHOP:
            return unichr(9815)
        elif piece == pieces.KNIGHT:
            return unichr(9816)
        elif piece == pieces.PAWN:
            return unichr(9817)
        else:
            return ValueError('Piece code %s does not match any known pieces.' % piece)
    elif color == colors.BLACK:
        if piece == pieces.KING:
            return unichr(9818)
        elif piece == pieces.QUEEN:
            return unichr(9819)
        elif piece == pieces.ROOK:
            return unichr(9820)
        elif piece == pieces.BISHOP:
            return unichr(9821)
        elif piece == pieces.KNIGHT:
            return unichr(9822)
        elif piece == pieces.PAWN:
            return unichr(9823)
        else:
            return ValueError('Piece code %s does not match any known pieces.' % piece)
    else:
        raise ValueError('Color code %s does not match that of White or Black.' % color)