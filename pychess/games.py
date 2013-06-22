'''
Created on Jun 20, 2013

@author: nick
'''

from boards import ClassicBoard
from pieces import colors, pieces
from pieces import to_algebraic
from utils import ctl

class VanillaChess(object):
    '''
        Not sure if this will become an instance of a game or just hold the rules.
        For now it will do both.
    '''
    def __init__(self, white_player, black_player):
        self.board = ClassicBoard()
        self.white_player = white_player
        self.black_player = black_player
        self.white_kingside_castle = True
        self.white_queenside_castle = True
        self.black_kingside_castle = True
        self.black_queenside_castle = True
        self.fifty_move_counter = 0
        self.white_in_checkmate = False
        self.black_in_checkmate = False
        
    def __repr__(self):
        return 'VanillaChess(white_player=%r, black_player=%r)' % (self.white_player, self.black_player) 
        
    def coordinate_to_algebraic(self, to_sq, from_sq):
        #piece_code = 
        pass
    
    def algebraic_to_coordinate(self, algebraic):
        pass
    
    def is_king_in_check(self, color):
        pass
    
    def is_king_in_checkmate(self, color):
        pass
    
    def is_valid_board_position(self):
        pass
    
    def piece_can_move_from_to(self, piece, to_sq, from_sq):
        pass
    
    def score_board(self):
        pass
    
    