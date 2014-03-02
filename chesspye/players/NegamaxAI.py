'''
Created on Mar 1, 2014

@author: Nick Crawford

Uses the negamax algorithm (http://en.wikipedia.org/wiki/Negamax)
to look ahead n moves.
'''

from copy import deepcopy
from random import choice

from algorithms import BoardTreeNode, negamax, minimax
from pieces import piece_types, colors
from AIPlayer import AIPlayer
        
class NegamaxAI(AIPlayer):
    
    def __init__(self, name, color):
        super(NegamaxAI, self).__init__(name, color)

    def score_board(self, board):
        if self.game.rules.is_checkmate(colors.WHITE, board):
            return float('inf')
        elif self.game.rules.is_checkmate(colors.BLACK, board):
            return float('-inf')
        elif self.game.rules.is_draw(board, self.game.positions):
            return 0
        else:
            score = 0
            for piece in board.pieces.itervalues():
                if piece is not None:
                    score += piece.color * piece.value
        return score
    
    def move(self):
        return self.negamax_move()
        
    def minimax_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for i, action in enumerate(actions):
            av = minimax(action, 1, -self.color, self.score_board)[0]
            action_values[av] = action.move
            print 'Subtree for %s move(s) evaluated.' % (i+1)
        if self.color == colors.WHITE:
            return action_values[max(action_values)]
        else:
            return action_values[min(action_values)]
        
    def negamax_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for i, action in enumerate(actions):
            print 'Running negamax for %s: %s' % (action.move, action.board)
            av = -negamax(action, 1, -self.color, self.score_board)[0]
            action_values[av] = action.move
            print 'Subtree for %s move(s) evaluated.' % (i+1)
        return action_values[max(action_values)]
                
    def choose_promotion(self): #TODO: make this smarter (i.e. check for mate with each piece (well, really only the knight)
        return piece_types.QUEEN
        