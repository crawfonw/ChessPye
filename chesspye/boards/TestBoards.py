'''
Created on Jun 20, 2013

@author: nick
'''

from Board import Board

from pieces import Pawn, Knight, Rook, King, colors

class SmallTestBoard(Board):
    
    def __init__(self):
        super(SmallTestBoard, self).__init__(8,8)
        
        self.set_square_to_piece('d4', Pawn(colors.BLACK, times_moved=2))
        self.set_square_to_piece('b5', Pawn(colors.BLACK, times_moved=2))
        self.set_square_to_piece('c2', Pawn(colors.WHITE))
           
        self.pieces[(0,1)] = King(colors.WHITE)
        self.pieces[(7,6)] = King(colors.BLACK)
        self.kings[colors.BLACK] = (7,6)
        self.kings[colors.WHITE] = (0,1)

#         self.set_square_to_piece('d5', Pawn(colors.WHITE, times_moved=2))
#         self.set_square_to_piece('b4', Pawn(colors.WHITE, times_moved=2))
#         self.set_square_to_piece('c7', Pawn(colors.BLACK))
#          
#         self.pieces[(7,1)] = King(colors.BLACK)
#         self.pieces[(0,6)] = King(colors.WHITE)
#         self.kings[colors.BLACK] = (7,1)
#         self.kings[colors.WHITE] = (0,6)
        
        