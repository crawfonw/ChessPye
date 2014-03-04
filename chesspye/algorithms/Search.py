'''
Created on Mar 2, 2014

@author: Nick Crawford
'''

def minimax(node, depth, color, scoring_f):
    if depth == 0:
        return scoring_f(node.board), node.move
    children = node.generate_children(color)
    if color == 1:
        best = float('-inf')
        for child in children:
            val = minimax(child, depth - 1, -1, scoring_f)
            best = max(best, val)
        print 'Best for this subtree: %s' % str(best)
        return best
    else:
        best = float('inf')
        for child in children:
            val = minimax(child, depth - 1, 1, scoring_f)
            best = min(best, val)
        print 'Best for this subtree: %s' % str(best)
        return best

def negamax(node, depth, color, scoring_f):
    #print 'Evaluating %s at depth %s' % (node.move, depth)
    if depth == 0 or node.is_terminal():
        score = scoring_f(node.board)
        #print '%s score = %s' % (node.move, score)
        return score * color
    best = float('-inf')
    for child in node.generate_children(color):
        val = -negamax(child, depth - 1, -color, scoring_f)
        best = max(best, val)
    return best

def negamax_ab(node, depth, alpha, beta, color, scoring_f):
    #print 'Evaluating %s at depth %s' % (node.move, depth)
    if depth == 0 or node.is_terminal():
        score = scoring_f(node.board)
        #print '%s score = %s' % (node.move, score)
        return score * color
    best = float('-inf')
    for child in node.generate_children(color):
        val = -negamax_ab(child, depth - 1, -beta, -alpha, -color, scoring_f)
        best = max(best, val)
        alpha = max(alpha, val)
        if alpha >= beta:
            break
    return best