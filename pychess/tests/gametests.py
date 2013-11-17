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
        
    def testPawnCannotMoveThreeSpaces(self):
        self.game.board.pieces[(1,3)] = Pawn(colors.WHITE)
        
        self.assertFalse(self.game.move_piece((4,3), (7,3)), 'Pawn should not move three squares')
    
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
        
    def testRookMovementOnEmptyBoard(self):
        self.game.board.pieces[(3,3)] = Rook(colors.WHITE)
        
        self.assertTrue(self.game.move_piece((3,3), (3,4)), 'Rook can move right one square')
        self.assertTrue(self.game.move_piece((3,4), (3,7)), 'Rook can move right more than one square')
        self.assertTrue(self.game.move_piece((3,7), (3,1)), 'Rook can move left more than one square')
        self.assertTrue(self.game.move_piece((3,1), (3,0)), 'Rook can move left one square')
        self.assertTrue(self.game.move_piece((3,0), (4,0)), 'Rook can move up one square')
        self.assertTrue(self.game.move_piece((4,0), (7,0)), 'Rook can move up more than one square')
        self.assertTrue(self.game.move_piece((7,0), (1,0)), 'Rook can move down more than one square')
        self.assertTrue(self.game.move_piece((1,0), (0,0)), 'Rook can move down one square')
        self.assertFalse(self.game.move_piece((0,0), (2,2)), 'Rook cannot move diagonally')
        
    def testRookCapture(self):
        self.game.board.pieces[(3,3)] = Rook(colors.WHITE)
        self.game.board.pieces[(3,4)] = Pawn(colors.BLACK)
        self.game.board.pieces[(3,7)] = Pawn(colors.BLACK)
        self.game.board.pieces[(3,1)] = Pawn(colors.BLACK)
        self.game.board.pieces[(3,0)] = Pawn(colors.BLACK)
        self.game.board.pieces[(4,0)] = Pawn(colors.BLACK)
        self.game.board.pieces[(7,0)] = Pawn(colors.BLACK)
        self.game.board.pieces[(1,0)] = Pawn(colors.BLACK)
        self.game.board.pieces[(0,0)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.game.move_piece((3,3), (3,4)), 'Rook can move right one square')
        self.assertTrue(self.game.move_piece((3,4), (3,7)), 'Rook can move right more than one square')
        self.assertTrue(self.game.move_piece((3,7), (3,1)), 'Rook can move left more than one square')
        self.assertTrue(self.game.move_piece((3,1), (3,0)), 'Rook can move left one square')
        self.assertTrue(self.game.move_piece((3,0), (4,0)), 'Rook can move up one square')
        self.assertTrue(self.game.move_piece((4,0), (7,0)), 'Rook can move up more than one square')
        self.assertTrue(self.game.move_piece((7,0), (1,0)), 'Rook can move down more than one square')
        self.assertTrue(self.game.move_piece((1,0), (0,0)), 'Rook can move down one square')
        
    def testRookBeingBlocked(self):
        self.game.board.pieces[(3,3)] = Rook(colors.WHITE)
        self.game.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(3,2)] = Pawn(colors.WHITE)
        self.game.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,2)] = Pawn(colors.WHITE)
        
        self.assertFalse(self.game.move_piece((3,3), (3,4)), 'Rook cannot move right one square')
        self.assertFalse(self.game.move_piece((3,3), (3,7)), 'Rook cannot move right more than one square')
        self.assertFalse(self.game.move_piece((3,3), (3,2)), 'Rook cannot move left one square')
        self.assertFalse(self.game.move_piece((3,3), (3,0)), 'Rook cannot move left more than one square')
        self.assertFalse(self.game.move_piece((3,3), (4,3)), 'Rook cannot move up one square')
        self.assertFalse(self.game.move_piece((3,3), (7,3)), 'Rook cannot move up more than one square')
        self.assertFalse(self.game.move_piece((3,3), (2,3)), 'Rook cannot move down one square')
        self.assertFalse(self.game.move_piece((3,3), (0,3)), 'Rook cannot move down more than one square')
        
    def testBishopMovementOnEmptyBoard(self):
        self.game.board.pieces[(3,3)] = Bishop(colors.WHITE)
        
        self.assertTrue(self.game.move_piece((3,3), (4,4)), 'Bishop can move up right one square')
        self.assertTrue(self.game.move_piece((4,4), (7,7)), 'Bishop can move up right more than one square')
        self.assertTrue(self.game.move_piece((7,7), (6,6)), 'Bishop can move down left one square')
        self.assertTrue(self.game.move_piece((6,6), (3,3)), 'Bishop can move down left more than one square')
        self.assertTrue(self.game.move_piece((3,3), (2,4)), 'Bishop can move up left one square')
        self.assertTrue(self.game.move_piece((2,4), (0,6)), 'Bishop can move up left more than one square')
        self.assertTrue(self.game.move_piece((0,6), (1,5)), 'Bishop can move down right one square')
        self.assertTrue(self.game.move_piece((1,5), (5,1)), 'Bishop can move down right more than one square')
        self.assertFalse(self.game.move_piece((1,5), (2,5)), 'Bishop cannot move linearly')
    
    def testBishopCapture(self):
        self.game.board.pieces[(3,3)] = Bishop(colors.WHITE)
        self.game.board.pieces[(4,4)] = Pawn(colors.BLACK)
        self.game.board.pieces[(7,7)] = Pawn(colors.BLACK)
        self.game.board.pieces[(2,4)] = Pawn(colors.BLACK)
        self.game.board.pieces[(0,6)] = Pawn(colors.BLACK)
        self.game.board.pieces[(5,1)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.game.move_piece((3,3), (4,4)), 'Bishop can move up right one square')
        self.assertTrue(self.game.move_piece((4,4), (7,7)), 'Bishop can move up right more than one square')
        self.assertTrue(self.game.move_piece((7,7), (6,6)), 'Bishop can move down left one square')
        self.assertTrue(self.game.move_piece((6,6), (3,3)), 'Bishop can move down left more than one square')
        self.assertTrue(self.game.move_piece((3,3), (2,4)), 'Bishop can move up left one square')
        self.assertTrue(self.game.move_piece((2,4), (0,6)), 'Bishop can move up left more than one square')
        self.assertTrue(self.game.move_piece((0,6), (1,5)), 'Bishop can move down right one square')
        self.assertTrue(self.game.move_piece((1,5), (5,1)), 'Bishop can move down right more than one square')
    
    def testBishopBeingBlocked(self):
        self.game.board.pieces[(3,3)] = Bishop(colors.WHITE)
        self.game.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,3)] = Pawn(colors.WHITE)
        self.game.board.pieces[(3,2)] = Pawn(colors.WHITE)
        self.game.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.game.board.pieces[(4,2)] = Pawn(colors.WHITE)
        
        self.assertFalse(self.game.move_piece((3,3), (4,4)), 'Bishop cannot move up right one square')
        self.assertFalse(self.game.move_piece((3,3), (7,7)), 'Bishop cannot move up right more than one square')
        self.assertFalse(self.game.move_piece((3,3), (2,2)), 'Bishop cannot move down left one square')
        self.assertFalse(self.game.move_piece((3,3), (0,0)), 'Bishop cannot move down left more than one square')
        self.assertFalse(self.game.move_piece((3,3), (2,4)), 'Bishop cannot move up left one square')
        self.assertFalse(self.game.move_piece((3,3), (0,6)), 'Bishop cannot move up left more than one square')
        self.assertFalse(self.game.move_piece((3,3), (4,2)), 'Bishop cannot move down right one square')
        self.assertFalse(self.game.move_piece((3,3), (6,0)), 'Bishop cannot move down right more than one square')
    
    def testKingSideCastle(self):
        self.fail('Not implemented')
        
    def testQueenSideCastle(self):
        self.fail('Not implemented')
        
    def testCannotCastleWhenPiecesBlocking(self):
        self.fail('Not implemented')
        
    def testCannotCastleWhenKingOrRookHasMoved(self):
        self.fail('Not implemented')
        

if __name__ == "__main__":
    unittest.main()