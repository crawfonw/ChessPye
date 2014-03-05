'''
Created on Mar 1, 2014

@author: Nick Crawford

Uses the minimax algorithm (http://en.wikipedia.org/wiki/Minimax)
to look ahead n moves.
'''

from algorithms import BoardTreeNode
from algorithms import material_score
from pieces import piece_types, colors
from AIPlayer import AIPlayer

class MinimaxAI(AIPlayer):
    
    def __init__(self, name, color, parallel=False):
        super(MinimaxAI, self).__init__(name, color, parallel)
        self.depth = 2
        self.scoring_f = material_score
    
    def move(self):
        self.last_nodes_expanded = 0
        return self.minimax_move() 
        
    def minimax_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for i, action in enumerate(actions):
            av = self.minimax(action, self.depth, -self.color)
            action_values[av] = action.move
            print 'Subtree for %s move(s) evaluated.' % (i+1)
        if self.color == colors.WHITE:
            return action_values[max(action_values)]
        else:
            return action_values[min(action_values)]
        
    def minimax(self, node, depth, color):
        if depth == 0:
            self.last_nodes_expanded += 0
            return self.scoring_f(node.board, self.game)
        children = node.generate_children(color)
        if color == colors.WHITE:
            best = float('-inf')
            for child in children:
                val = self.minimax(child, depth - 1, -1)
                best = max(best, val)
            print 'Best for this subtree: %s' % str(best)
            return best
        else:
            best = float('inf')
            for child in children:
                val = self.minimax(child, depth - 1, 1)
                best = min(best, val)
            print 'Best for this subtree: %s' % str(best)
            return best
                
    def choose_promotion(self): #TODO: make this smarter (i.e. check for mate with each piece (well, really only the knight)
        return piece_types.QUEEN
        