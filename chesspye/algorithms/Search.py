'''
Created on Mar 2, 2014

@author: Nick Crawford
'''

def minimax(node, depth, maximizing, scoring_f):
    if depth == 0 or not node.has_child():
        return scoring_f(node.obj)
    if maximizing:
        best_val = float('-inf')
        for child in node.children:
            val = minimax(child, depth - 1, False, scoring_f)
            best_val = max(best_val, val)
            return best_val
    else:
        best_val = float('inf')
        for child in node.children:
            val = minimax(child, depth - 1, True, scoring_f)
            best_val = max(best_val, val)
            return best_val
            
def negamax(node, depth, color, scoring_f):
    if depth == 0:
        return scoring_f(node.board) * color, node.move
    best = [(float('-inf'), None)]
    for child in node.generate_children(-color):
        val, move = negamax(child, depth - 1, -color, scoring_f)
        val = -val
        best.append((val, move))
        print 'Color: %s' % color
        print 'Best so far %s - %s' % (str(best[0]), str(best[1]))
    return max(best)