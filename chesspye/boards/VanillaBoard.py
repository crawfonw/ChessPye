'''
Created on Jun 20, 2013

@author: nick
'''

from Board import Board

from pieces import Pawn, Knight, Bishop, Rook, Queen, King, colors, piece_types
from utils import ctl, letter_to_number, Stack

class VanillaBoard(Board):
    
    def __init__(self):
        super(VanillaBoard, self).__init__(8,8)
        self.pieces[(0,0)] = Rook(colors.WHITE) #Fischer Random will look so much cleaner
        self.pieces[(0,1)] = Knight(colors.WHITE)
        self.pieces[(0,2)] = Bishop(colors.WHITE)
        self.pieces[(0,3)] = Queen(colors.WHITE)
        self.pieces[(0,4)] = King(colors.WHITE)
        self.pieces[(0,5)] = Bishop(colors.WHITE)
        self.pieces[(0,6)] = Knight(colors.WHITE)
        self.pieces[(0,7)] = Rook(colors.WHITE)
        self.pieces[(7,0)] = Rook(colors.BLACK)
        self.pieces[(7,1)] = Knight(colors.BLACK)
        self.pieces[(7,2)] = Bishop(colors.BLACK)
        self.pieces[(7,3)] = Queen(colors.BLACK)
        self.pieces[(7,4)] = King(colors.BLACK)
        self.pieces[(7,5)] = Bishop(colors.BLACK)
        self.pieces[(7,6)] = Knight(colors.BLACK)
        self.pieces[(7,7)] = Rook(colors.BLACK)
        for i in range(self.width):
            self.pieces[(1,i)] = Pawn(colors.WHITE)
            self.pieces[(6,i)] = Pawn(colors.BLACK)
        self.kings[colors.BLACK] = (7,4)
        self.kings[colors.WHITE] = (0,4)
        