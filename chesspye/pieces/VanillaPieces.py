'''
Created on Jun 21, 2013

@author: nick
'''

import os

from pieces import ChessPiece, colors, piece_types, move_types
from utils import enum, scalar_mult_tuple

VANILLA_SPRITES = os.path.realpath('sprites.png')

def vanilla_type_to_obj(piece_type, color):
    if piece_type == piece_types.PAWN:
        return Pawn(color)
    elif piece_type == piece_types.KNIGHT:
        return Knight(color)
    elif piece_type == piece_types.BISHOP:
        return Bishop(color)
    elif piece_type == piece_types.ROOK:
        return Rook(color)
    elif piece_type == piece_types.QUEEN:
        return Queen(color)
    elif piece_type == piece_types.KING:
        return King(color)
    else:
        return None
    
def str_to_vanilla_type(string):
    string = string.upper()
    if string == 'P':
        return piece_types.PAWN
    elif string == 'N':
        return piece_types.KNIGHT
    elif string == 'B':
        return piece_types.BISHOP
    elif string == 'R':
        return piece_types.ROOK
    elif string == 'Q':
        return piece_types.QUEEN
    elif string == 'K':
        return piece_types.KING
    else:
        return None 
        

class Pawn(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Pawn, self).__init__('Pawn', color, piece_types.PAWN, 1, 9817, 'P', times_moved, move_types.EXACT, VANILLA_SPRITES)
        
    def sprite_region(self):
        if self.color == colors.WHITE:
            return ((0, 0, 64, 64))
        else:
            return ((0, 64, 64, 64))
        
    def move_patterns(self):
        if not self.has_moved():
            return [scalar_mult_tuple(self.color, arg) for arg in [(2,0), (1,0)]]
        else:
            return [scalar_mult_tuple(self.color, (1,0))]
        
    def attack_patterns(self):
        return [scalar_mult_tuple(self.color, arg) for arg in [(1,1), (1,-1)]]

class Knight(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Knight, self).__init__('Knight', color, piece_types.KNIGHT, 3, 9816, 'N', times_moved, move_types.EXACT, VANILLA_SPRITES, True)
    
    def sprite_region(self):
        if self.color == colors.WHITE:
            return ((128, 0, 64, 64))
        else:
            return ((128, 64, 64, 64))
    
    def move_patterns(self):
        return [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
    
    attack_patterns = move_patterns

class Bishop(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Bishop, self).__init__('Bishop', color, piece_types.BISHOP, 3, 9815, 'B', times_moved, move_types.MAX, VANILLA_SPRITES)
    
    def sprite_region(self):
        if self.color == colors.WHITE:
            return ((64, 0, 64, 64))
        else:
            return ((64, 64, 64, 64))
    
    def move_patterns(self):
        return [(1,1), (1,-1), (-1,1), (-1,-1)]
    
    attack_patterns = move_patterns
        
class Rook(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Rook, self).__init__('Rook', color, piece_types.ROOK, 5, 9814, 'R', times_moved, move_types.MAX, VANILLA_SPRITES)
    
    def sprite_region(self):
        if self.color == colors.WHITE:
            return ((192, 0, 64, 64))
        else:
            return ((192, 64, 64, 64))
    
    def move_patterns(self):
        return [(1,0), (-1,0), (0,1), (0,-1)]
    
    attack_patterns = move_patterns

class Queen(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(Queen, self).__init__('Queen', color, piece_types.QUEEN, 9, 9813, 'Q', times_moved, move_types.MAX, VANILLA_SPRITES)
    
    def sprite_region(self):
        if self.color == colors.WHITE:
            return ((256, 0, 64, 64))
        else:
            return ((256, 64, 64, 64))
    
    def move_patterns(self):
        return [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    
    attack_patterns = move_patterns

class King(ChessPiece):
    def __init__(self, color, times_moved=0):
        super(King, self).__init__('King', color, piece_types.KING, 999, 9812, 'K', times_moved, move_types.EXACT, VANILLA_SPRITES)
    
    def sprite_region(self):
        if self.color == colors.WHITE:
            return ((320, 0, 64, 64))
        else:
            return ((320, 64, 64, 64))
    
    def move_patterns(self):
        return [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    
    attack_patterns = move_patterns