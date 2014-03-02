'''
Created on Mar 1, 2014

@author: Nick Crawford

Greedy, but dumb, AI. Scores the board based on piece count
and only for its next immediate move. Doesn't look at potential
opponent moves. Possibly worse than the RandomAI since you can
force it to take pieces.
'''

from copy import deepcopy
from random import choice

from pieces import piece_types, colors
from AIPlayer import AIPlayer
        
class HalfLookAI(AIPlayer):
    
    def __init__(self, name, color):
        super(HalfLookAI, self).__init__(name, color)

    def score_board(self, board):
        if self.game.rules.is_checkmate(colors.WHITE, board):
            return float('inf')
        elif self.game.rules.is_checkmate(colors.BLACK, board):
            return float('-inf')
        elif self.game.rules.is_stalemate(colors.WHITE, board) or self.game.rules.is_stalemate(colors.BLACK, board):
            return 0
        else:
            score = 0
            for piece in board.pieces.itervalues():
                if piece is not None:
                    score += piece.color * piece.value
        return score
        
    def move(self):
        scores = []
        my_pieces = self.game.board.get_pieces_for_color(self.color)
        for from_sq, piece in my_pieces:
            vectors = piece.all_patterns()
            for move_vector in vectors:
                possible_moves = self.game.rules.generate_all_valid_target_squares_for_attack_vector(from_sq, piece, move_vector, self.game.board)
                for move in possible_moves:
                    test_board = deepcopy(self.game.board)
                    if self.game.rules.is_valid_move(from_sq, move, test_board):
                        self.game.rules.move_piece(from_sq, move, test_board)
                        score = self.score_board(test_board) * self.color
                        if len(scores) > 0:
                            if score > scores[0][0]:
                                scores = []
                                scores.append((score, (from_sq, move)))
                            elif score == scores[0][0]:
                                scores.append((score, (from_sq, move)))
                        else:
                            scores.append((score, (from_sq, move)))
        print scores
        return choice(scores)[1]
                
    def choose_promotion(self):
        return piece_types.QUEEN
        