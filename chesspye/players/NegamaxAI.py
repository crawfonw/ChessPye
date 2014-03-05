'''
Created on Mar 1, 2014

@author: Nick Crawford

Uses the negamax algorithm (http://en.wikipedia.org/wiki/Negamax)
to look ahead n moves.
'''

from algorithms import BoardTreeNode
from algorithms import material_score
from pieces import piece_types, colors
from AIPlayer import AIPlayer

class NegamaxAI(AIPlayer):
    
    def __init__(self, name, color, parallel=False):
        super(NegamaxAI, self).__init__(name, color, parallel)
        self.depth = 2
        self.scoring_f = material_score
    
    def move(self):
        self.last_nodes_expanded = 0
        return self.negamax_move() 
        
    def negamax_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, self.game.positions, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for i, action in enumerate(actions):
            print 'Running negamax for %s: %s' % (action.move, action.board)
            av = -self.negamax(action, self.depth, -self.color, self.scoring_f)
            action_values[av] = action.move
            print 'Subtree for %s move(s) evaluated.' % (i+1)
        print
        print 'Values: %s' % action_values
        return action_values[max(action_values)]
    
    def negamax(self, node, depth, color):
        #print 'Evaluating %s at depth %s' % (node.move, depth)
        if depth == 0 or node.is_terminal():
            score = self.scoring_f(node.board, self.game)
            self.last_nodes_expanded += 0
            #print '%s score = %s' % (node.move, score)
            return score * color
        best = float('-inf')
        for child in node.generate_children(color):
            val = -self.negamax(child, depth - 1, -color)
            best = max(best, val)
        return best
                
    def choose_promotion(self): #TODO: make this smarter (i.e. check for mate with each piece (well, really only the knight)
        return piece_types.QUEEN
        