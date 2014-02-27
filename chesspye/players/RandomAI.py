'''
Created on Feb 27, 2014

@author: Nick Crawford

Completely Random AI. Pick a piece that can move and move it.
That's all.
'''

from random import shuffle

from Enums import player_types
from AIPlayer import AIPlayer
        
class RandomAI(AIPlayer):
    
    def __init__(self, name, color):
        super(RandomAI, self).__init__(name, color)
        
    def move(self):
        my_pieces = self.game.board.get_pieces_for_color(self.color)
        shuffle(my_pieces)
        for from_sq, piece in my_pieces:
            vectors = piece.all_patterns()
            shuffle(vectors)
            for move_vector in vectors:
                possible_moves = self.game.rules.generate_all_valid_target_squares_for_attack_vector(from_sq, piece, move_vector, self.game.board)
                if len(possible_moves) > 0:
                    shuffle(possible_moves)
                    return (from_sq, possible_moves[0])
        