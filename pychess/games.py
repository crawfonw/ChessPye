'''
Created on Jun 20, 2013

@author: nick
'''

from boards import ClassicBoard
from pieces import colors, move_types
from utils import Vec2d

from math import copysign

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
    
    def is_pseudo_legal_board_position(self):
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
                if Vec2d(move) + Vec2d(from_sq) == Vec2d(to_sq):
                    if piece.can_jump:
                        return True
                    else:
                        #This piece can move here assuming it is unblocked
                        #Now find the straight-line path and make sure nothing is blocking
                        f = lambda x : int(copysign(1,x)) if x != 0 else 0
                        unit_move = Vec2d(f(move[0]), f(move[1]))
                        curr_sq = Vec2d(from_sq) + unit_move
                        while tuple(curr_sq) != to_sq:
                            if not self.board.square_is_on_board(tuple(curr_sq)):
                                return False
                            if self.board.pieces[tuple(curr_sq)] is not None:
                                return False
                            curr_sq += unit_move
                        return True
        elif piece.move_type == move_types.MAX:
            for move in pattern_types:
                dir_vec = Vec2d(move) #a unit vector
                move_vec = Vec2d(to_sq[0] - from_sq[0], to_sq[1] - from_sq[1])
                #This direction is a valid movement if vectorized coordinates 
                #have an angle of zero between them and point the same direction
                #(i.e. scalar multiples of one another)
                if dir_vec.get_angle_between(move_vec) == 0:
                    curr_sq = Vec2d(from_sq) + dir_vec
                    while tuple(curr_sq) != to_sq:
                        if not self.board.square_is_on_board(tuple(curr_sq)):
                            return False
                        if self.board.pieces[tuple(curr_sq)] is not None and not piece.can_jump:
                            return False
                        curr_sq += dir_vec
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