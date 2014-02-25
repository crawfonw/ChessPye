'''
Created on Jun 20, 2013

@author: nick
'''

from chesspye.board.boards import ClassicBoard
from chesspye.board.pieces import piece_types, colors
from rules import VanillaRules

class VanillaChess(object):

    def __init__(self, white_player, black_player, interface):
        self.board = ClassicBoard()
        self.rules = VanillaRules()
        self.interface = interface
        self.white_player = white_player
        self.black_player = black_player
        
    def __repr__(self):
        return 'VanillaChess(white_player=%r, black_player=%r)' % (self.white_player, self.black_player) 
    
    def handle_pawn_promotion(self):
        last_move = self.moves.peek() 
        if last_move[0].piece_type == piece_types.PAWN:
            if last_move[0].color == colors.WHITE:
                if last_move[2][0] == self.board.height - 1:
                    self.dispatch_promotion_choice()
            elif last_move[0].color == colors.BLACK:
                if last_move[2][0] == 0:
                    self.dispatch_promotion_choice()
    
    def dispatch_promotion_choice(self):
        return interface.promote()
    
    def check_for_endgame(self, color):
        result = self.rules.is_game_over(color)
        if result:
            return result
        return False
    
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