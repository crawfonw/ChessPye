'''
Created on Jun 20, 2013

@author: nick
'''

from pieces import colors, pieces
from pieces import to_utf

class Board(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.white_pieces = {}
        self.black_pieces = {}
    
    def __str__(self):
        s = u'\n'
        for i in range(self.height): #row
            s += '%s ' % (self.height - i)
            for j in range(self.width): #col
                color = None
                piece = None
                if self.white_pieces.has_key((i,j)):
                    color = colors.WHITE
                    piece = self.white_pieces[(i,j)]
                elif self.black_pieces.has_key((i,j)):
                    color = colors.BLACK
                    piece = self.black_pieces[(i,j)]
                if color is not None and piece is not None:
                    s += '| %s ' % to_utf(piece,color)
                else:
                    s += '|   '
            s += '|\n  --'
            s += '----' * self.width
            s += '\n'
        s += '  '
        for i in range(self.height):
            s += '| %s ' % chr(97 + i)
        s += '\n'
        return s.encode('UTF-8')
    
    def __repr__(self):
        s = 'Board(width=%s,height=%s) Contents:\nWhite:\n' % (self.width, self.height)
        for piece in self.white_pieces.viewitems():
            s += '%s at %s\n' % (piece[1], piece[0])
        s += 'Black\n'
        for piece in self.black_pieces.viewitems():
            s += '%s at %s\n' % (piece[1], piece[0])
        return s

class ClassicBoard(Board):
    
    def __init__(self):
        super(ClassicBoard, self).__init__(8,8)
        self.black_pieces = {(0,0):pieces.ROOK, (0,1):pieces.KNIGHT, (0,2):pieces.BISHOP,
                             (0,3):pieces.QUEEN, (0,4):pieces.KING, (0,5):pieces.BISHOP,
                             (0,6):pieces.KNIGHT, (0,7):pieces.ROOK, (1,0):pieces.PAWN, 
                             (1,1):pieces.PAWN, (1,2):pieces.PAWN, (1,3):pieces.PAWN, 
                             (1,4):pieces.PAWN, (1,5):pieces.PAWN, (1,6):pieces.PAWN,
                             (1,7):pieces.PAWN}
        self.white_pieces = {(7,0):pieces.ROOK, (7,1):pieces.KNIGHT, (7,2):pieces.BISHOP,
                             (7,3):pieces.QUEEN, (7,4):pieces.KING, (7,5):pieces.BISHOP,
                             (7,6):pieces.KNIGHT, (7,7):pieces.ROOK, (6,0):pieces.PAWN, 
                             (6,1):pieces.PAWN, (6,2):pieces.PAWN, (6,3):pieces.PAWN, 
                             (6,4):pieces.PAWN, (6,5):pieces.PAWN, (6,6):pieces.PAWN,
                             (6,7):pieces.PAWN}
        