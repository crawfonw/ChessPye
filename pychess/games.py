'''
Created on Jun 20, 2013

@author: nick
'''

from boards import ClassicBoard
from pieces import colors, move_types

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
    
    def is_king_in_check(self, color):
        pass
    
    def is_king_in_checkmate(self, color):
        return False
    
    def is_valid_board_position(self):
        pass
    
    def move_piece(self, from_sq, to_sq):
        if from_sq == to_sq:
            return False
        if not self.board.square_is_on_board(from_sq):
            return False
        piece = self.board.pieces[from_sq]
        if piece is not None:
            if self.piece_can_move_from_to(piece, from_sq, to_sq):
                piece.has_moved = True
                self.board.pieces[from_sq] = None
                self.board.pieces[to_sq] = piece
                return True
        return False
    
    def piece_can_move_from_to(self, piece, from_sq, to_sq):
        pattern_types = None
        to_sq_piece = self.board.pieces[to_sq]
        if self.board.pieces[to_sq] is not None:
            if piece.color == to_sq_piece.color:
                return False
            else:
                pattern_types = piece.attack_patterns()
        else:
            pattern_types = piece.move_patterns()
            
        if piece.move_type == move_types.EXACT:
            for move in pattern_types:
                if tuple(sum(x) for x in zip(move, from_sq)) == to_sq:
                    if piece.can_jump:
                        return True
                    else:
                        #This piece can move here assuming it is unblocked
                        #Now find the straight-line path and make sure nothing is blocking
                        
                        ##This is incorrect thinking... Implement the vector class
                        curr_sq = from_sq
                        while curr_sq != to_sq:
                            curr_sq = tuple(sum(x) for x in zip(move, curr_sq))
                            if not self.board.square_is_on_board(curr_sq):
                                return False
                            if self.board.pieces[curr_sq] is not None:
                                return False
                        return True

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