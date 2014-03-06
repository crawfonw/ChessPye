'''
Created on Mar 5, 2014

@author: Nick Crawford
'''

from algorithms import BoardTreeNode
from algorithms import material_score
from pieces import piece_types, colors
from AIPlayer import AIPlayer

class NegascoutAI(AIPlayer):
    
    def __init__(self, name, color, parallel=False):
        super(NegascoutAI, self).__init__(name, color, parallel)
        self.scoring_f = material_score
    
    def move(self):
        self.last_nodes_expanded = 0
        return self.negascout_move()
    
    def negascout_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, self.game.positions, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for action in actions:
            av = -self.negascout(action, self.depth, float('-inf'), float('inf'), -self.color)
            action_values[av] = action.move
        return action_values[max(action_values)]

    def negascout(self, node, depth, alpha, beta, color):
        if depth == 0 or node.is_terminal():
            self.last_nodes_expanded += 1
            return self.scoring_f(node.board, self.game) * color
        children = node.generate_children(color)
        for child in children:
            if child is not children[0]:
                score = -self.negascout(child, depth - 1, -alpha - 1, -alpha, -color)
                if alpha < score and score < beta:
                    score = -self.negascout(child, depth - 1, -beta, -score, -color)
            else:
                score = -self.negascout(child, depth - 1, -beta, -alpha, -color)
            alpha = max(alpha, score)
            if alpha >= beta:
                break
        return alpha
    
    def choose_promotion(self): #TODO: make this smarter (i.e. check for mate with each piece (well, really only the knight)
        return piece_types.QUEEN