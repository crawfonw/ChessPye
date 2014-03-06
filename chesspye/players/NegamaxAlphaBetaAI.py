'''
Created on Mar 5, 2014

@author: Nick Crawford

Uses the negamax algorithm with alpha beta pruning (http://en.wikipedia.org/wiki/Negamax)
to look ahead n moves.
'''

import copy_reg
import types
from utils import _pickle_method, _unpickle_method

import pp

from algorithms import BoardTreeNode
from algorithms import material_score
from pieces import piece_types, colors
from AIPlayer import AIPlayer

class NegamaxAlphaBetaAI(AIPlayer):
    
    def __init__(self, name, color, parallel=False):
        super(NegamaxAlphaBetaAI, self).__init__(name, color, parallel)
        self.scoring_f = material_score
    
    def move(self):
        self.last_nodes_expanded = 0
        if self.parallel:
            move = self.negamax_move_parallel()
        else:
            move = self.negamax_ab_move()
        return move
    
    def negamax_ab_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, self.game.positions, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for i, action in enumerate(actions):
            print 'Running negamax_ab for %s: %s' % (action.move, action.board)
            av = -self.negamax_ab(action, self.depth, float('-inf'), float('inf'), -self.color)
            action_values[av] = action.move
            print 'Subtree for %s move(s) evaluated.' % (i+1)
        print
        print 'Values: %s' % action_values
        return action_values[max(action_values)]
    
    def negamax_move_parallel(self):
        
        copy_reg.pickle(types.MethodType, _pickle_method, _unpickle_method)
        
        node = BoardTreeNode(self.game.board, self.game.rules, self.game.positions, None)
        action_values = {}
        actions = node.generate_children(self.color)
        
        ppservers = ()
        job_server = pp.Server(ppservers=ppservers)

        print "Starting pp with", job_server.get_ncpus(), "workers"

        funcs = (node.generate_children, node.is_terminal, )
        modules = ()
        
        jobs = [(action, job_server.submit(negamax_parallel, (action, self.depth, float('-inf'), float('inf'), -self.color, self.scoring_f,), funcs, modules)) for action in actions]
        for action, job in jobs:            
            action_values[-job()] = action.move

        job_server.print_stats()
        
        print 'Values: %s' % action_values
        return action_values[max(action_values)]
    
    def negamax_ab(self, node, depth, alpha, beta, color):
        #print 'Evaluating %s at depth %s' % (node.move, depth)
        if depth == 0 or node.is_terminal():
            score = self.scoring_f(node.board, self.game)
            #print '%s score = %s' % (node.move, score)
            self.last_nodes_expanded += 1
            return score * color
        best = float('-inf')
        for child in node.generate_children(color):
            val = -self.negamax_ab(child, depth - 1, -beta, -alpha, -color)
            best = max(best, val)
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return best
                
    def choose_promotion(self): #TODO: make this smarter (i.e. check for mate with each piece (well, really only the knight)
        return piece_types.QUEEN
        