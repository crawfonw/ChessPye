'''
Created on Jun 22, 2013

@author: nick
'''
import unittest

from chesspye.games import VanillaChess
from chesspye.pieces import King, Rook, colors

class TestEndgameChecking(unittest.TestCase):
    
    def setUp(self):
        self.game = VanillaChess(None, None, None)
        self.game.board.clear_board()
        
        self.game.board.set_square_to_piece('e1', King(colors.WHITE))
        self.game.board.set_square_to_piece('h1', Rook(colors.WHITE))
        self.game.board.set_square_to_piece('a1', Rook(colors.WHITE))

    def tearDown(self):
        pass
    
    def testIsThreeMoveRepetitionAfterThreeConsecutiveMoves(self):
        pass

    def testIsThreeMoveRepetitionAfterThreeNonconsecutiveMoves(self):
        pass
    
    def testIsNotThreeMoveRepetition(self):
        pass
    
    def testIsNotThreeMoveDueToKingsideCastleWhite(self):
        pass
    
    def testIsNotThreeMoveDueToKingsideCastleBlack(self):
        pass
    
    def testIsNotThreeMoveDueToQueensideCastleWhite(self):
        pass
    
    def testIsNotThreeMoveDueToQueensideCastleBlack(self):
        pass

if __name__ == "__main__":
    unittest.main()