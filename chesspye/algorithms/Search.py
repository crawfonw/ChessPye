'''
Created on Mar 2, 2014

@author: Nick Crawford
'''

def minimax(node, depth, color, scoring_f):
    if depth == 0:
        print 'Scoring board: %s' % node.board
        print 'Score: %s' % (scoring_f(node.board))
        return scoring_f(node.board), node.move
    children = node.generate_children(color)
    if color == 1:
        best = [(float('-inf'), None)]
        for child in children:
            val, move = minimax(child, depth - 1, -1, scoring_f)
            best.append((val, move))
        return max(best)
    else:
        best = [(float('inf'), None)]
        for child in children:
            val, move = minimax(child, depth - 1, 1, scoring_f)
            best.append((val, move))
        return min(best)
            
def negamax(node, depth, color, scoring_f):
    if depth == 0:
        return scoring_f(node.board) * color, node.move
    best = [(float('-inf'), None)]
    for child in node.generate_children(color):
        val, move = negamax(child, depth - 1, -color, scoring_f)
        best.append((-val, move))
        print 'Color: %s' % color
        print 'Best so far %s - %s' % (str(best[0]), str(best[1]))
    return max(best)