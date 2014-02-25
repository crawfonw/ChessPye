'''
Created on Jun 22, 2013

@author: nick
'''
import unittest

from chesspye.game.games import VanillaChess

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = VanillaChess(None,None)
        self.game.board.clear_board()

    def tearDown(self):
        pass
    
    def testKingIsInCheckmate(self):
        self.board.set_square_to_piece('f1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('h1', Rook(colors.BLACK))
        self.board.set_square_to_piece('a2', Rook(colors.BLACK))
        
        self.assertTrue(self.game.is_checkmate(colors.WHITE), 'King cannot move, block, nor take out of check')

if __name__ == "__main__":
    unittest.main()