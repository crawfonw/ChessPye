'''
Created on Jun 21, 2013

@author: nick
'''

from chesspye.utils import enum, scalar_mult_tuple

colors = enum(WHITE=1, BLACK=-1)
piece_types = enum(PAWN=0, KNIGHT=1, BISHOP=2, ROOK=3, QUEEN=4, KING=5)
move_types = enum(MAX=0, EXACT=1)

class ChessPiece(object):
    
    def __init__(self, long_name, color, piece_type, value, utf_code_white, algebraic, times_moved, move_type, can_jump=False):
        self.long_name = long_name
        self.color = color
        self.piece_type = piece_type
        self.value = value
        self.utf_code_white = utf_code_white
        self.algebraic = algebraic
        self.times_moved = times_moved
        self.move_type = move_type
        self.can_jump = can_jump

    def __unicode__(self):
        if self.color == colors.WHITE:
            return unichr(self.utf_code_white)
        elif self.color == colors.BLACK:
            return unichr(self.utf_code_white + 6)
    
    def __str__(self):
        return self.algebraic
    
    def __repr__(self):
        return '%s(long_name=%s, color=%s, piece_type=%s, value=%s, utf_code_white=%s, algebraic=%s, times_moved=%s)' \
            % (self.__class__.__name__, self.long_name, self.color, self.piece_type, \
               self.value, self.utf_code_white, self.algebraic, self.times_moved)
    
    def move_patterns(self):
        '''
            Returns a list of tuples with xy modifier coordinates of how
            this piece moves.
        '''
        return
    
    def attack_patterns(self):
        return
    
    def has_moved(self):
        return self.times_moved > 0

class Pawn(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Pawn, self).__init__('Pawn', color, piece_types.PAWN, 1, 9817, '', times_moved, move_types.EXACT)
        
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