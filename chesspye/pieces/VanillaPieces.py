'''
Created on Jun 21, 2013

@author: nick
'''

from chesspye.pieces import ChessPiece, colors, piece_types, move_types
from chesspye.utils import enum, scalar_mult_tuple

class Pawn(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Pawn, self).__init__('Pawn', color, piece_types.PAWN, 1, 9817, 'P', times_moved, move_types.EXACT)
        
    def move_patterns(self):
        if not self.has_moved():
            return [scalar_mult_tuple(self.color, arg) for arg in [(2,0), (1,0)]]
        else:
            return [scalar_mult_tuple(self.color, (1,0))]
        
    def attack_patterns(self):
        return [scalar_mult_tuple(self.color, arg) for arg in [(1,1), (1,-1)]]

class Knight(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Knight, self).__init__('Knight', color, piece_types.KNIGHT, 3, 9816, 'N', times_moved, move_types.EXACT, True)
        
    def move_patterns(self):
        return [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
    
    attack_patterns = move_patterns

class Bishop(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Bishop, self).__init__('Bishop', color, piece_types.BISHOP, 3, 9815, 'B', times_moved, move_types.MAX)
        
    def move_patterns(self):
        return [(1,1), (1,-1), (-1,1), (-1,-1)]
    
    attack_patterns = move_patterns
        
class Rook(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Rook, self).__init__('Rook', color, piece_types.ROOK, 5, 9814, 'R', times_moved, move_types.MAX)
        
    def move_patterns(self):
        return [(1,0), (-1,0), (0,1), (0,-1)]
    
    attack_patterns = move_patterns

class Queen(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Queen, self).__init__('Queen', color, piece_types.QUEEN, 9, 9813, 'Q', times_moved, move_types.MAX)
        
    def move_patterns(self):
        return [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    
    attack_patterns = move_patterns

class King(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(King, self).__init__('King', color, piece_types.KING, 999, 9812, 'K', times_moved, move_types.EXACT)
        
    def move_patterns(self):
        return [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    
    attack_patterns = move_patterns