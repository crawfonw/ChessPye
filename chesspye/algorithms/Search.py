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

def negascout(node, depth, alpha, beta, color, scoring_f):
    if depth == 0 or node.is_terminal():
        score = scoring_f(node.board)
        return score * color
    children = node.generate_children(color)
    for child in children:
        if child is not children[0]:
            score = -negascout(child, depth - 1, -alpha - 1, -alpha, -color, scoring_f)
            if alpha < score and score < beta:
                score = -negascout(child, depth - 1, -beta, -score, -color, scoring_f)
        else:
            score = -negascout(child, depth - 1, -beta, -alpha, -color, scoring_f)
        alpha = max(alpha, score)
        if alpha >= beta:
            break
    return alpha
        