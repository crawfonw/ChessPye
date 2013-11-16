'''
Created on Jun 21, 2013

@author: nick
'''

from games import VanillaChess
from pieces import Rook, Knight
from pieces import colors

g = VanillaChess(None, None)

p1 = ((0,0), Rook(colors.WHITE)) #a1
p2 = ((3,0), Knight(colors.BLACK)) #a4
p3 = ((0,2), Knight(colors.BLACK)) #c1

if __name__ == '__main__':
    g.board.pieces[(0,0)] = None
    print g.board
    print g.score_board()