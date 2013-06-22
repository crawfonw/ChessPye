'''
Created on Jun 21, 2013

@author: nick
'''

from utils import enum

colors = enum(WHITE=0, BLACK=1)
pieces = enum(PAWN=0, KNIGHT=1, BISHOP=2, ROOK=3, QUEEN=4, KING=5)

class ChessPiece(object):
    
    def __init__(self, long_name, color, piece_type, value, utf_code_white, algebraic, has_moved):
        self.long_name = long_name
        self.color = color
        self.piece_type = piece_type
        self.value = value
        self.utf_code_white = utf_code_white
        self.algebraic = algebraic
        self.has_moved = has_moved

    def __unicode__(self):
        if self.color == colors.WHITE:
            return unichr(self.utf_code_white)
        elif self.color == colors.BLACK:
            return unichr(self.utf_code_white + 6)
    
    def __str__(self):
        return self.algebraic
    
    def __repr__(self):
        return '%s(long_name=%s, color=%s, piece_type=%s, value=%s, utf_code_white=%s, algebraic=%s, has_moved=%s)' \
            % (self.__class__.__name__, self.long_name, self.color, self.piece_type, \
               self.value, self.utf_code_white, self.algebraic, self.has_moved)
            
class Pawn(ChessPiece): #Icky, pawns aren't pieces, per-say!
    def __init__(self, color, has_moved=False):
        super(Pawn, self).__init__('Pawn', color, pieces.PAWN, 1, 9817, '', has_moved)

class Knight(ChessPiece):
    def __init__(self, color, has_moved=False):
        super(Knight, self).__init__('Knight', color, pieces.KNIGHT, 3, 9816, 'N', has_moved)

class Bishop(ChessPiece):
    def __init__(self, color, has_moved=False):
        super(Bishop, self).__init__('Bishop', color, pieces.BISHOP, 3, 9815, 'B', has_moved)
        
class Rook(ChessPiece):
    def __init__(self, color, has_moved=False):
        super(Rook, self).__init__('Rook', color, pieces.ROOK, 5, 9814, 'R', has_moved)

class Queen(ChessPiece):
    def __init__(self, color, has_moved=False):
        super(Queen, self).__init__('Queen', color, pieces.QUEEN, 9, 9813, 'Q', has_moved)

class King(ChessPiece):
    def __init__(self, color, has_moved=False):
        super(King, self).__init__('King', color, pieces.KING, 999, 9812, 'K', has_moved)