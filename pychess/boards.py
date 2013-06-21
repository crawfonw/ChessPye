'''
Created on Jun 20, 2013

@author: nick
'''

from pieces import COLORS, PIECES
from pieces import to_utf

class Board(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.white_pieces = {}
        self.black_pieces = {}
    
    def __str__(self):
        print self.encode()
        return '' #This is hacky; I hate messing with Unicode...
    
    def encode(self):
        s = u'\n'
        for i in range(self.height): #row
            s += '%s ' % (self.height - i)
            for j in range(self.width): #col
                color = None
                piece = None
                if self.white_pieces.has_key((i,j)):
                    color = COLORS.WHITE
                    piece = self.white_pieces[(i,j)]
                elif self.black_pieces.has_key((i,j)):
                    color = COLORS.BLACK
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
        return s

class ClassicBoard(Board):
    
    def __init__(self):
        super(ClassicBoard, self).__init__(8,8)
        self.black_pieces = {(0,0):PIECES.ROOK, (0,1):PIECES.KNIGHT, (0,2):PIECES.BISHOP,
                             (0,3):PIECES.QUEEN, (0,4):PIECES.KING, (0,5):PIECES.BISHOP,
                             (0,6):PIECES.KNIGHT, (0,7):PIECES.ROOK, (1,0):PIECES.PAWN, 
                             (1,1):PIECES.PAWN, (1,2):PIECES.PAWN, (1,3):PIECES.PAWN, 
                             (1,4):PIECES.PAWN, (1,5):PIECES.PAWN, (1,6):PIECES.PAWN,
                             (1,7):PIECES.PAWN}
        self.white_pieces = {(7,0):PIECES.ROOK, (7,1):PIECES.KNIGHT, (7,2):PIECES.BISHOP,
                             (7,3):PIECES.QUEEN, (7,4):PIECES.KING, (7,5):PIECES.BISHOP,
                             (7,6):PIECES.KNIGHT, (7,7):PIECES.ROOK, (6,0):PIECES.PAWN, 
                             (6,1):PIECES.PAWN, (6,2):PIECES.PAWN, (6,3):PIECES.PAWN, 
                             (6,4):PIECES.PAWN, (6,5):PIECES.PAWN, (6,6):PIECES.PAWN,
                             (6,7):PIECES.PAWN}
        