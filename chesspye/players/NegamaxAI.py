'''
Created on Mar 1, 2014

@author: Nick Crawford

Uses the negamax algorithm (http://en.wikipedia.org/wiki/Negamax)
to look ahead n moves.
'''

import copy_reg
import types
from utils import _pickle_method, _unpickle_method

import pp, sys

from copy import deepcopy
from random import choice
import time

from algorithms import BoardTreeNode, negamax, minimax, negamax_ab, negamax_parallel, negascout
from pieces import piece_types, colors
from AIPlayer import AIPlayer
from algorithms import material_score

class NegamaxAI(AIPlayer):
    
    def __init__(self, name, color, parallel=False):
        super(NegamaxAI, self).__init__(name, color, parallel)
        self.depth = 2
        self.scoring_f = material_score
    
    def move(self):
        if self.parallel:
            move = self.negamax_move_parallel()
        else:
            move = self.negamax_ab_move()
        return move 
        
    def minimax_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for i, action in enumerate(actions):
            av = minimax(action, self.depth, -self.color, self.score_board)
            action_values[av] = action.move
            print 'Subtree for %s move(s) evaluated.' % (i+1)
        if self.color == colors.WHITE:
            return action_values[max(action_values)]
        else:
            return action_values[min(action_values)]
        
    def negamax_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, self.game.positions, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for i, action in enumerate(actions):
            print 'Running negamax for %s: %s' % (action.move, action.board)
            av = -negamax(action, self.depth, -self.color, self.score_board)
            action_values[av] = action.move
            print 'Subtree for %s move(s) evaluated.' % (i+1)
        print
        print 'Values: %s' % action_values
        return action_values[max(action_values)]
    
    def negamax_ab_move(self):
        node = BoardTreeNode(self.game.board, self.game.rules, self.game.positions, None)
        action_values = {}
        actions = node.generate_children(self.color)
        for i, action in enumerate(actions):
            print 'Running negamax_ab for %s: %s' % (action.move, action.board)
            av = -negamax_ab(action, self.depth, float('-inf'), float('inf'), -self.color, self.score_board)
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
        
        jobs = [(action, job_server.submit(negamax_parallel, (action, self.depth, float('-inf'), float('inf'), -self.color, self.score_board,), funcs, modules)) for action in actions]
        for action, job in jobs:            
            action_values[-job()] = action.move

        job_server.print_stats()
        
        print 'Values: %s' % action_values
        return action_values[max(action_values)]
                
    def choose_promotion(self): #TODO: make this smarter (i.e. check for mate with each piece (well, really only the knight)
        return piece_types.QUEEN
        