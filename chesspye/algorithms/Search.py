'''
Created on Mar 2, 2014

@author: Nick Crawford
'''

import pp

def negamax_parallel(node, depth, alpha, beta, color, scoring_f):
    #print 'Evaluating %s at depth %s' % (node.move, depth)
    if depth == 0 or node.is_terminal():
        ppservers = ()
        job_server = pp.Server(ppservers=ppservers)

        funcs = (negamax_parallel, node.generate_children, node.is_terminal, )
        modules = ()

        job = job_server.submit(scoring_f, (node.board, ), funcs, modules)
        return job() * color
    
    best = float('-inf')
    for child in node.generate_children(color):
        val = -negamax_parallel(child, depth - 1, -beta, -alpha, -color, scoring_f)
        best = max(best, val)
        alpha = max(alpha, val)
        if alpha >= beta:
            break
    return best
        