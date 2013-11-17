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
        self.game.board.pieces[(1,3)] = Pawn(colors.WHITE, has_moved=True)
        self.assertFalse(self.game.move_piece((1,3), (3,3)), 'Pawn moved two squares after already moving')
        self.assertTrue(self.game.move_piece((1,3), (2,3)), 'Pawn should be able to move one square')
    
    def testDoublePawnMove(self):
        self.game.board.pieces[(1,3)] = Pawn(colors.WHITE)
        self.assertFalse(self.game.board.pieces[(1,3)].has_moved, 'Piece has not moved')
        self.assertTrue(self.game.move_piece((1,3), (3,3)), 'Pawn has not moved; two square move is possible')
        self.assertTrue(self.game.move_piece((3,3), (4,3)), 'Pawn should be able to move one square')
        self.assertFalse(self.game.move_piece((4,3), (6,3)), 'Pawn should not move two squares')
    
    def testPawnCapture(self):
        self.game.board.pieces[(1,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,4)] = Pawn(colors.BLACK)
        self.game.board.pieces[(3,3)] = Pawn(colors.BLACK)
        self.assertTrue(self.game.move_piece((1,3), (2,4)), 'Pawn may capture to the right')
        self.assertTrue(self.game.move_piece((2,4), (3,3)), 'Pawn may capture to the left')
    
    def testPawnCannotCaptureOwnPiece(self):
        self.game.board.pieces[(1,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.assertFalse(self.game.move_piece((1,3), (2,4)), 'Pawn cannot capture to the right')
        self.assertFalse(self.game.move_piece((1,3), (2,2)), 'Pawn cannot capture to the left')
    
    def testPawnIsBlockedByEnemy(self):
        self.game.board.pieces[(1,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,3)] = Pawn(colors.BLACK)
        self.assertFalse(self.game.move_piece((1,3), (3,3)), 'Pawn is blocked')
        
    def testPawnIsBlockedByAlly(self):
        self.game.board.pieces[(1,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.assertFalse(self.game.move_piece((1,3), (3,3)), 'Pawn is blocked')
        
    def testEnPassent(self):
        self.fail('Not implemented')
        
    def testKnightCanJump(self):
        self.game.board.pieces[(3,3)] = Knight(colors.WHITE)
        self.game.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(3,2)] = Pawn(colors.WHITE)
        self.game.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,2)] = Pawn(colors.WHITE)
        
        self.assertTrue(self.game.move_piece((3,3), (5,4)), 'Knight may jump over blockers')
        self.assertTrue(self.game.move_piece((5,4), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (5,2)), 'Knight may jump over blockers')
        self.assertTrue(self.game.move_piece((5,2), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (1,4)), 'Knight may jump over blockers')
        self.assertTrue(self.game.move_piece((1,4), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (1,2)), 'Knight may jump over blockers')
        self.assertTrue(self.game.move_piece((1,2), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (4,5)), 'Knight may jump over blockers')
        self.assertTrue(self.game.move_piece((4,5), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (2,5)), 'Knight may jump over blockers')
        self.assertTrue(self.game.move_piece((2,5), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (4,1)), 'Knight may jump over blockers')
        self.assertTrue(self.game.move_piece((4,1), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (2,1)), 'Knight may jump over blockers')
        self.assertTrue(self.game.move_piece((2,1), (3,3)), 'Knight may jump over blockers')
    
    def testKnightCapture(self):
        self.game.board.pieces[(3,3)] = Knight(colors.WHITE)
        self.game.board.pieces[(5,4)] = Pawn(colors.BLACK)
        self.game.board.pieces[(5,2)] = Pawn(colors.BLACK)
        self.game.board.pieces[(1,4)] = Pawn(colors.BLACK)
        self.game.board.pieces[(1,2)] = Pawn(colors.BLACK)
        self.game.board.pieces[(4,5)] = Pawn(colors.BLACK)
        self.game.board.pieces[(2,5)] = Pawn(colors.BLACK)
        self.game.board.pieces[(4,1)] = Pawn(colors.BLACK)
        self.game.board.pieces[(2,1)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.game.move_piece((3,3), (5,4)), 'Knight may capture')
        self.assertTrue(self.game.move_piece((5,4), (3,3)), 'Knight may move to empty space')
        
        self.assertTrue(self.game.move_piece((3,3), (5,2)), 'Knight may capture')
        self.assertTrue(self.game.move_piece((5,2), (3,3)), 'Knight may move to empty space')
        
        self.assertTrue(self.game.move_piece((3,3), (1,4)), 'Knight may capture')
        self.assertTrue(self.game.move_piece((1,4), (3,3)), 'Knight may move to empty space')
        
        self.assertTrue(self.game.move_piece((3,3), (1,2)), 'Knight may capture')
        self.assertTrue(self.game.move_piece((1,2), (3,3)), 'Knight may move to empty space')
        
        self.assertTrue(self.game.move_piece((3,3), (4,5)), 'Knight may capture')
        self.assertTrue(self.game.move_piece((4,5), (3,3)), 'Knight may move to empty space')
        
        self.assertTrue(self.game.move_piece((3,3), (2,5)), 'Knight may capture')
        self.assertTrue(self.game.move_piece((2,5), (3,3)), 'Knight may move to empty space')
        
        self.assertTrue(self.game.move_piece((3,3), (4,1)), 'Knight may capture')
        self.assertTrue(self.game.move_piece((4,1), (3,3)), 'Knight may move to empty space')
        
        self.assertTrue(self.game.move_piece((3,3), (2,1)), 'Knight may capture')
        self.assertTrue(self.game.move_piece((2,1), (3,3)), 'Knight may move to empty space')
    
    def testKnightJumpAndCapture(self):
        self.game.board.pieces[(3,3)] = Knight(colors.WHITE)
        self.game.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(3,2)] = Pawn(colors.WHITE)
        self.game.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,2)] = Pawn(colors.WHITE)
        
        self.game.board.pieces[(5,4)] = Pawn(colors.BLACK)
        self.game.board.pieces[(5,2)] = Pawn(colors.BLACK)
        self.game.board.pieces[(1,4)] = Pawn(colors.BLACK)
        self.game.board.pieces[(1,2)] = Pawn(colors.BLACK)
        self.game.board.pieces[(4,5)] = Pawn(colors.BLACK)
        self.game.board.pieces[(2,5)] = Pawn(colors.BLACK)
        self.game.board.pieces[(4,1)] = Pawn(colors.BLACK)
        self.game.board.pieces[(2,1)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.game.move_piece((3,3), (5,4)), 'Knight may jump over blockers to capture')
        self.assertTrue(self.game.move_piece((5,4), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (5,2)), 'Knight may jump over blockers to capture')
        self.assertTrue(self.game.move_piece((5,2), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (1,4)), 'Knight may jump over blockers to capture')
        self.assertTrue(self.game.move_piece((1,4), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (1,2)), 'Knight may jump over blockers to capture')
        self.assertTrue(self.game.move_piece((1,2), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (4,5)), 'Knight may jump over blockers to capture')
        self.assertTrue(self.game.move_piece((4,5), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (2,5)), 'Knight may jump over blockers to capture')
        self.assertTrue(self.game.move_piece((2,5), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (4,1)), 'Knight may jump over blockers to capture')
        self.assertTrue(self.game.move_piece((4,1), (3,3)), 'Knight may jump over blockers')
        
        self.assertTrue(self.game.move_piece((3,3), (2,1)), 'Knight may jump over blockers to capture')
        self.assertTrue(self.game.move_piece((2,1), (3,3)), 'Knight may jump over blockers')


if __name__ == "__main__":
    unittest.main()