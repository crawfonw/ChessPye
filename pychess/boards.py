'''
Created on Jun 20, 2013

@author: nick
'''

from pieces import colors
from pieces import Pawn, Knight, Bishop, Rook, Queen, King
from utils import ctl

class Board(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pieces = {}
    
    def __str__(self):
        s = u'\n'
        for i in range(self.height): #row
            s += '%s ' % (self.height - i)
            for j in range(self.width): #col
                if self.pieces.has_key((i,j)):
                    s += '| %s ' % self.pieces[(i,j)].__unicode__()
                else:
                    s += '|   '
            s += '|\n  --'
            s += '----' * self.width
            s += '\n'
        s += '  '
        for i in range(self.height):
            s += '| %s ' % ctl(i)
        s += '\n'
        return s.encode('UTF-8')
    
    def __repr__(self):
        s = 'Board(width=%s,height=%s) Contents:\n' % (self.width, self.height)
        for piece in self.pieces.viewitems():
            s += '%s at %s\n' % (piece[1].__repr__(), piece[0])
        return s

class ClassicBoard(Board):
    
    def __init__(self):
        super(ClassicBoard, self).__init__(8,8)
        self.pieces = {(0,0):Rook(colors.BLACK), (0,1):Knight(colors.BLACK), (0,2):Bishop(colors.BLACK),
                             (0,3):Queen(colors.BLACK), (0,4):King(colors.BLACK), (0,5):Bishop(colors.BLACK),
                             (0,6):Knight(colors.BLACK), (0,7):Rook(colors.BLACK), (1,0):Pawn(colors.BLACK), 
                             (1,1):Pawn(colors.BLACK), (1,2):Pawn(colors.BLACK), (1,3):Pawn(colors.BLACK), 
                             (1,4):Pawn(colors.BLACK), (1,5):Pawn(colors.BLACK), (1,6):Pawn(colors.BLACK),
                             (1,7):Pawn(colors.BLACK), \
                             
                             (7,0):Rook(colors.WHITE), (7,1):Knight(colors.WHITE), (7,2):Bishop(colors.WHITE),
                             (7,3):Queen(colors.WHITE), (7,4):King(colors.WHITE), (7,5):Bishop(colors.WHITE),
                             (7,6):Knight(colors.WHITE), (7,7):Rook(colors.WHITE), (6,0):Pawn(colors.WHITE), 
                             (6,1):Pawn(colors.WHITE), (6,2):Pawn(colors.WHITE), (6,3):Pawn(colors.WHITE), 
                             (6,4):Pawn(colors.WHITE), (6,5):Pawn(colors.WHITE), (6,6):Pawn(colors.WHITE),
                             (6,7):Pawn(colors.WHITE)}
        