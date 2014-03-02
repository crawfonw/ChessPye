'''
Created on Mar 1, 2014

@author: Nick Crawford

Uses the negamax algorithm (http://en.wikipedia.org/wiki/Negamax)
to look ahead n moves.
'''

from copy import deepcopy
from random import choice

from algorithms import BoardTreeNode, negamax
from pieces import piece_types, colors
from AIPlayer import AIPlayer
        
class NegamaxAI(AIPlayer):
    
    def __init__(self, name, color):
        super(NegamaxAI, self).__init__(name, color)

    def score_board(self, board):
        if self.game.rules.is_checkmate(colors.WHITE, board):
            print 'WCh'
            return float('inf')
        elif self.game.rules.is_checkmate(colors.BLACK, board):
            print 'BCh'
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
        node = BoardTreeNode(self.game.board, self.game.rules, None)
        action_values = []
        actions = node.generate_children(self.color)
        for action in actions:
            av = self.color * negamax(action, 2, self.color, self.score_board)[0]
            print av, action.move
            #action_values[av] = action.move
            action_values.append((av, action.move))
        print action_values
        return action_values[max(action_values)]
        
        #best_move = self.color * negamax(node, 2, self.color, self.score_board)
        #best = negamax(node, 2, self.color, self.score_board)
        #print 'Best move: %s (score: %s)' % (str(best[1]), -best[0])
        #return best[1]
                
    def choose_promotion(self): #TODO: make this smarter (i.e. check for mate with each piece (well, really only the knight)
        return piece_types.QUEEN
        