'''
Created on Jun 22, 2013

@author: nick
'''
import unittest

from pychess.games import VanillaChess
from pychess.pieces import Pawn, Knight, Bishop, Rook, Queen, King, colors

class TestPieceMovement(unittest.TestCase):

    def setUp(self):
        self.game = VanillaChess(None,None)
        self.game.board.clear_board()

    def tearDown(self):
        pass
    
    def testMoveNullPiece(self):
        self.assertFalse(self.game.move_piece((0,0), (0,1)), 'Cannot move NoneType piece')
    
    def testNormalPawnMove(self):
        self.game.board.pieces[(3,2)] = Pawn(colors.WHITE, has_moved=True)
        self.assertFalse(self.game.move_piece((3,2), (3,4)), 'Pawn moved two squares after already moving')
        self.assertTrue(self.game.move_piece((3,2), (3,3)), 'Pawn should be able to move one square')
    
    def testDoublePawnMove(self):
        self.game.board.pieces[(3,1)] = Pawn(colors.WHITE)
        self.assertFalse(self.game.board.pieces[(3,1)].has_moved, 'Piece has not moved')
        self.assertTrue(self.game.move_piece((3,1), (3,3)), 'Pawn has not moved; two square move is possible')
        self.assertTrue(self.game.move_piece((3,3), (3,4)), 'Pawn should be able to move one square')
        self.assertFalse(self.game.move_piece((3,4), (3,6)), 'Pawn should not move two squares')
    
    def testPawnCapture(self):
        pass
    
    def testPawnIsBlocked(self):
        pass
    
    def testEnPassent(self):
        self.fail('Not implemented')


if __name__ == "__main__":
    unittest.main()