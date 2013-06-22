'''
Created on Jun 21, 2013

@author: nick
'''

from boards import ClassicBoard
from games import VanillaChess
from pieces import Rook, Knight, colors

c = ClassicBoard()
g = VanillaChess(None, None)

p1 = ((0,0), Rook(colors.WHITE)) #a1
p2 = ((3,0), Knight(colors.BLACK)) #a4
p3 = ((0,2), Knight(colors.BLACK)) #c1

if __name__ == '__main__':
    print c
    #print c.__repr__()
    print g.coordinate_to_algebraic(p2, p1)
    print g.coordinate_to_algebraic(p3, p1)