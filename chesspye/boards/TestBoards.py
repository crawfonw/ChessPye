'''
Created on Jun 20, 2013

@author: nick
'''

from Board import Board

from pieces import Pawn, Knight, Rook, King, colors

class SmallTestBoard(Board):
    
    def __init__(self):
        super(SmallTestBoard, self).__init__(8,8)
        
#         self.set_square_to_piece('d4', Pawn(colors.BLACK, times_moved=2))
#         self.set_square_to_piece('b5', Pawn(colors.BLACK, times_moved=2))
#         self.set_square_to_piece('c2', Pawn(colors.WHITE))
#             
#         self.pieces[(0,6)] = King(colors.WHITE)
#         self.pieces[(7,6)] = King(colors.BLACK)
#         self.kings[colors.BLACK] = (7,6)
#         self.kings[colors.WHITE] = (0,6)

        self.set_square_to_piece('d4', Pawn(colors.WHITE, times_moved=2))
        self.set_square_to_piece('b3', Pawn(colors.WHITE, times_moved=2))
        self.set_square_to_piece('c6', Pawn(colors.BLACK, times_moved=1))
           
        self.pieces[(7,1)] = King(colors.BLACK)
        self.pieces[(3,2)] = King(colors.WHITE)
        self.kings[colors.BLACK] = (7,1)
        self.kings[colors.WHITE] = (3,2)
        
class PawnAndKnightsTestBoard(Board):
    
    def __init__(self):
        super(PawnAndKnightsTestBoard, self).__init__(8,8)
        
        self.set_square_to_piece('f2', Pawn(colors.WHITE))
        self.set_square_to_piece('g2', Pawn(colors.WHITE))
        self.set_square_to_piece('h2', Pawn(colors.WHITE))
        self.set_square_to_piece('f3', Knight(colors.WHITE))
        
        self.set_square_to_piece('f7', Pawn(colors.BLACK))
        self.set_square_to_piece('g7', Pawn(colors.BLACK))
        self.set_square_to_piece('h7', Pawn(colors.BLACK))
        self.set_square_to_piece('f6', Knight(colors.BLACK))
        
        self.pieces[(7,6)] = King(colors.BLACK)
        self.pieces[(0,6)] = King(colors.WHITE)
        self.kings[colors.BLACK] = (7,6)
        self.kings[colors.WHITE] = (0,6)
        
        