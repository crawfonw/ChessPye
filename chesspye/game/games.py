'''
Created on Jun 20, 2013

@author: nick
'''

from chesspye.board.boards import ClassicBoard
from rules import VanillaRules
from chesspye.utils import Stack

class VanillaChess(object):
    '''
        Not sure if this will become an instance of a game or just hold the rules.
        For now it will do both.
    '''
    def __init__(self, white_player, black_player):
        self.board = ClassicBoard()
        self.rules = VanillaRules()
        self.white_player = white_player
        self.black_player = black_player
        self.moves = Stack()
        
    def __repr__(self):
        return 'VanillaChess(white_player=%r, black_player=%r)' % (self.white_player, self.black_player) 
    
    def is_king_in_check(self, color):
        pass
    
    def is_king_in_checkmate(self, color):
        return False
    
    def is_pseudo_legal_board_position(self):
        pass
    
    def play_game(self):
        pass
    
    def repl(self):
        pass

''' This will probably be moved to an AI player since they would only use this...
    def score_board(self):
        if self.is_king_in_checkmate(colors.WHITE):
            return float('inf')
        elif self.is_king_in_checkmate(colors.BLACK):
            return float('-inf')
        else:
            score = 0
            for piece in self.board.pieces.itervalues():
                if piece is not None:
                    score += piece.color * piece.value
        return score 
'''