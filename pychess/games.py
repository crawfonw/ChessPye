'''
Created on Jun 20, 2013

@author: nick
'''

from boards import ClassicBoard

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
        
    def coordinate_to_algebraic(self, to_sq, from_sq):
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
    
    