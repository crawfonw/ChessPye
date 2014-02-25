'''
Created on Jun 22, 2013

@author: nick
'''
import unittest

from chesspye.board.boards import ClassicBoard
from chesspye.board.pieces import Pawn, Knight, Bishop, Rook, Queen, King, colors, piece_types
from chesspye.game.games import VanillaChess
from chesspye.game.rules import VanillaRules
from chesspye.utils import Stack

class TestPieceMovement(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testMoveNullPiece(self):
        self.assertFalse(self.rules.move_piece((0,0), (0,1), self.board), 'Cannot move NoneType piece')
    
    def testNormalPawnMoveWhite(self):
        self.board.pieces[(1,3)] = Pawn(colors.WHITE, times_moved=1)
        
        self.assertFalse(self.rules.move_piece((1,3), (3,3), self.board), 'Pawn moved two squares after already moving')
        self.assertTrue(self.rules.move_piece((1,3), (2,3), self.board), 'Pawn should be able to move one square')
        
    def testNormalPawnMoveBlack(self):
        self.board.set_square_to_piece('e6', Pawn(colors.BLACK, times_moved=1))
        
        self.assertFalse(self.rules.move_piece('e6', 'e4', self.board), 'Pawn moved two squares after already moving')
        self.assertTrue(self.rules.move_piece('e6', 'e5', self.board), 'Pawn should be able to move one square')
    
    def testDoublePawnMoveWhite(self):
        self.board.pieces[(1,3)] = Pawn(colors.WHITE)
        
        self.assertFalse(self.board.pieces[(1,3)].has_moved(), 'Piece has not moved')
        self.assertTrue(self.rules.move_piece((1,3), (3,3), self.board), 'Pawn has not moved; two square move is possible')
        self.assertTrue(self.rules.move_piece((3,3), (4,3), self.board), 'Pawn should be able to move one square')
        self.assertFalse(self.rules.move_piece((4,3), (6,3), self.board), 'Pawn should not move two squares')
    
    def testDoublePawnMoveBlack(self):
        self.board.set_square_to_piece('e7', Pawn(colors.BLACK))
        
        self.assertFalse(self.board.pieces[self.board.algebraic_to_coordinate_square('e7')].has_moved(), 'Piece has not moved')
        self.assertTrue(self.rules.move_piece('e7', 'e5', self.board), 'Pawn has not moved; two square move is possible')
        self.assertTrue(self.rules.move_piece('e5', 'e4', self.board), 'Pawn should be able to move one square')
        self.assertFalse(self.rules.move_piece('e4', 'e2', self.board), 'Pawn should not move two squares')
        
    def testWhitePawnDoesNotReplacePieceWhenBlockedByAlly(self):
        pawn = Pawn(colors.WHITE)
        other = Rook(colors.WHITE)
        self.board.set_square_to_piece('d2', pawn)
        self.board.set_square_to_piece('d3', other)
        
        self.assertFalse(self.rules.move_piece('d2', 'd3', self.board), 'Pawn is blocked')
        self.assertTrue(self.board.get_square('d2') is pawn, 'Pawn is not on original square')
        self.assertTrue(self.board.get_square('d3') is other, 'Other piece is not on original square')
        
    def testBlackPawnDoesNotReplacePieceWhenBlockedByAlly(self):
        pawn = Pawn(colors.BLACK)
        other = Rook(colors.BLACK)
        self.board.set_square_to_piece('d7', pawn)
        self.board.set_square_to_piece('d6', other)
        
        self.assertFalse(self.rules.move_piece('d7', 'd6', self.board), 'Pawn is blocked')
        self.assertTrue(self.board.get_square('d7') is pawn, 'Pawn is not on original square')
        self.assertTrue(self.board.get_square('d6') is other, 'Other piece is not on original square')
        
    def testWhitePawnCannotMoveMoreThanTwoSpaces(self):
        start = self.board.algebraic_to_coordinate_square('d2')
        self.board.set_square_to_piece('d2', Pawn(colors.WHITE))
        
        for i in range(4, self.board.width):
            self.assertFalse(self.rules.move_piece(start, (i,3), self.board), 'Pawn should not move %s squares' % (i-start[0]))
            
    def testBlackPawnCannotMoveMoreThanTwoSpaces(self):
        start = self.board.algebraic_to_coordinate_square('d7')
        self.board.set_square_to_piece('d7', Pawn(colors.BLACK))
        
        for i in range(0, self.board.width - 4):
            self.assertFalse(self.rules.move_piece(start, (i,3), self.board), 'Pawn should not move %s squares' % (start[0]-i))

    def testWhitePawnCannotMoveBackwards(self):
        self.board.set_square_to_piece('d2', Pawn(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('d2', 'd1', self.board), 'Pawn should not move straight backwards')
        self.assertFalse(self.rules.move_piece('d2', 'c1', self.board), 'Pawn should not move diagonal left backwards')
        self.assertFalse(self.rules.move_piece('d2', 'e1', self.board), 'Pawn should not move diagonal right backwards')
    
    def testBlackPawnCannotMoveBackwards(self):
        self.board.set_square_to_piece('d7', Pawn(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('d7', 'd8', self.board), 'Pawn should not move straight backwards')
        self.assertFalse(self.rules.move_piece('d7', 'c8', self.board), 'Pawn should not move diagonal left backwards')
        self.assertFalse(self.rules.move_piece('d7', 'e8', self.board), 'Pawn should not move diagonal right backwards')
        
    def testWhitePawnCannotMoveSideways(self):
        self.board.set_square_to_piece('d2', Pawn(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('d2', 'c2', self.board), 'Pawn should not move left')
        self.assertFalse(self.rules.move_piece('d2', 'e2', self.board), 'Pawn should not move right')
        
    def testBlackPawnCannotMoveSideways(self):
        self.board.set_square_to_piece('d7', Pawn(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('d7', 'c7', self.board), 'Pawn should not move left')
        self.assertFalse(self.rules.move_piece('d7', 'e7', self.board), 'Pawn should not move right')
    
    def testWhitePawnCannotJumpEnemyInDoubleMove(self):
        self.board.set_square_to_piece('d2', Pawn(colors.WHITE))
        self.board.set_square_to_piece('d3', Pawn(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('d2', 'd4', self.board), 'Pawn is blocked')
        
    def testBlackPawnCannotJumpEnemyInDoubleMove(self):
        self.board.set_square_to_piece('d6', Pawn(colors.WHITE))
        self.board.set_square_to_piece('d7', Pawn(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('d7', 'd5', self.board), 'Pawn is blocked')
        
    def testWhitePawnCannotJumpAllyInDoubleMove(self):
        self.board.set_square_to_piece('d2', Pawn(colors.WHITE))
        self.board.set_square_to_piece('d3', Pawn(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('d2', 'd4', self.board), 'Pawn is blocked')
        
    def testBlackPawnCannotJumpAllyInDoubleMove(self):
        self.board.set_square_to_piece('d2', Pawn(colors.BLACK))
        self.board.set_square_to_piece('d3', Pawn(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('d2', 'd4', self.board), 'Pawn is blocked')

    def testWhiteKnightCanJump(self):
        self.board.pieces[(3,3)] = Knight(colors.WHITE)
        self.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.board.pieces[(4,3)] = Pawn(colors.WHITE)
        self.board.pieces[(3,2)] = Pawn(colors.WHITE)
        self.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.board.pieces[(4,2)] = Pawn(colors.WHITE)
        
        self.assertTrue(self.rules.move_piece((3,3), (5,4), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((5,4), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (5,2), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((5,2), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (1,4), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((1,4), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (1,2), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((1,2), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (4,5), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((4,5), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (2,5), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((2,5), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (4,1), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((4,1), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (2,1), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((2,1), (3,3), self.board), 'Knight may jump over blockers')
        
    def testBlackKnightCanJump(self):
        self.board.pieces[(3,3)] = Knight(colors.BLACK)
        self.board.pieces[(2,3)] = Pawn(colors.BLACK)
        self.board.pieces[(4,3)] = Pawn(colors.BLACK)
        self.board.pieces[(3,2)] = Pawn(colors.BLACK)
        self.board.pieces[(3,4)] = Pawn(colors.BLACK)
        self.board.pieces[(2,2)] = Pawn(colors.BLACK)
        self.board.pieces[(4,4)] = Pawn(colors.BLACK)
        self.board.pieces[(2,4)] = Pawn(colors.BLACK)
        self.board.pieces[(4,2)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.rules.move_piece((3,3), (5,4), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((5,4), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (5,2), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((5,2), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (1,4), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((1,4), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (1,2), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((1,2), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (4,5), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((4,5), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (2,5), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((2,5), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (4,1), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((4,1), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (2,1), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((2,1), (3,3), self.board), 'Knight may jump over blockers')
        
    def testWhiteRookMovementOnEmptyBoard(self):
        self.board.pieces[(3,3)] = Rook(colors.WHITE)
        
        self.assertTrue(self.rules.move_piece((3,3), (3,4), self.board), 'Rook can move right one square')
        self.assertTrue(self.rules.move_piece((3,4), (3,7), self.board), 'Rook can move right more than one square')
        self.assertTrue(self.rules.move_piece((3,7), (3,1), self.board), 'Rook can move left more than one square')
        self.assertTrue(self.rules.move_piece((3,1), (3,0), self.board), 'Rook can move left one square')
        self.assertTrue(self.rules.move_piece((3,0), (4,0), self.board), 'Rook can move up one square')
        self.assertTrue(self.rules.move_piece((4,0), (7,0), self.board), 'Rook can move up more than one square')
        self.assertTrue(self.rules.move_piece((7,0), (1,0), self.board), 'Rook can move down more than one square')
        self.assertTrue(self.rules.move_piece((1,0), (0,0), self.board), 'Rook can move down one square')
        self.assertFalse(self.rules.move_piece((0,0), (2,2), self.board), 'Rook cannot move diagonally')
        
    def testBlackRookMovementOnEmptyBoard(self):
        self.board.pieces[(3,3)] = Rook(colors.BLACK)
        
        self.assertTrue(self.rules.move_piece((3,3), (3,4), self.board), 'Rook can move right one square')
        self.assertTrue(self.rules.move_piece((3,4), (3,7), self.board), 'Rook can move right more than one square')
        self.assertTrue(self.rules.move_piece((3,7), (3,1), self.board), 'Rook can move left more than one square')
        self.assertTrue(self.rules.move_piece((3,1), (3,0), self.board), 'Rook can move left one square')
        self.assertTrue(self.rules.move_piece((3,0), (4,0), self.board), 'Rook can move up one square')
        self.assertTrue(self.rules.move_piece((4,0), (7,0), self.board), 'Rook can move up more than one square')
        self.assertTrue(self.rules.move_piece((7,0), (1,0), self.board), 'Rook can move down more than one square')
        self.assertTrue(self.rules.move_piece((1,0), (0,0), self.board), 'Rook can move down one square')
        self.assertFalse(self.rules.move_piece((0,0), (2,2), self.board), 'Rook cannot move diagonally')
        
    def testWhiteRookBeingBlocked(self):
        self.board.pieces[(3,3)] = Rook(colors.WHITE)
        self.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.board.pieces[(4,3)] = Pawn(colors.WHITE)
        self.board.pieces[(3,2)] = Pawn(colors.WHITE)
        self.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.board.pieces[(4,2)] = Pawn(colors.WHITE)
        
        self.assertFalse(self.rules.move_piece((3,3), (3,4), self.board), 'Rook cannot move right one square')
        self.assertFalse(self.rules.move_piece((3,3), (3,7), self.board), 'Rook cannot move right more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (3,2), self.board), 'Rook cannot move left one square')
        self.assertFalse(self.rules.move_piece((3,3), (3,0), self.board), 'Rook cannot move left more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (4,3), self.board), 'Rook cannot move up one square')
        self.assertFalse(self.rules.move_piece((3,3), (7,3), self.board), 'Rook cannot move up more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (2,3), self.board), 'Rook cannot move down one square')
        self.assertFalse(self.rules.move_piece((3,3), (0,3), self.board), 'Rook cannot move down more than one square')
        
    def testBlackRookBeingBlocked(self):
        self.board.pieces[(3,3)] = Rook(colors.BLACK)
        self.board.pieces[(2,3)] = Pawn(colors.BLACK)
        self.board.pieces[(4,3)] = Pawn(colors.BLACK)
        self.board.pieces[(3,2)] = Pawn(colors.BLACK)
        self.board.pieces[(3,4)] = Pawn(colors.BLACK)
        self.board.pieces[(2,2)] = Pawn(colors.BLACK)
        self.board.pieces[(4,4)] = Pawn(colors.BLACK)
        self.board.pieces[(2,4)] = Pawn(colors.BLACK)
        self.board.pieces[(4,2)] = Pawn(colors.BLACK)
        
        self.assertFalse(self.rules.move_piece((3,3), (3,4), self.board), 'Rook cannot move right one square')
        self.assertFalse(self.rules.move_piece((3,3), (3,7), self.board), 'Rook cannot move right more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (3,2), self.board), 'Rook cannot move left one square')
        self.assertFalse(self.rules.move_piece((3,3), (3,0), self.board), 'Rook cannot move left more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (4,3), self.board), 'Rook cannot move up one square')
        self.assertFalse(self.rules.move_piece((3,3), (7,3), self.board), 'Rook cannot move up more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (2,3), self.board), 'Rook cannot move down one square')
        self.assertFalse(self.rules.move_piece((3,3), (0,3), self.board), 'Rook cannot move down more than one square')
        
    def testWhiteBishopMovementOnEmptyBoard(self):
        self.board.pieces[(3,3)] = Bishop(colors.WHITE)
        
        self.assertTrue(self.rules.move_piece((3,3), (4,4), self.board), 'Bishop can move up right one square')
        self.assertTrue(self.rules.move_piece((4,4), (7,7), self.board), 'Bishop can move up right more than one square')
        self.assertTrue(self.rules.move_piece((7,7), (6,6), self.board), 'Bishop can move down left one square')
        self.assertTrue(self.rules.move_piece((6,6), (3,3), self.board), 'Bishop can move down left more than one square')
        self.assertTrue(self.rules.move_piece((3,3), (2,4), self.board), 'Bishop can move up left one square')
        self.assertTrue(self.rules.move_piece((2,4), (0,6), self.board), 'Bishop can move up left more than one square')
        self.assertTrue(self.rules.move_piece((0,6), (1,5), self.board), 'Bishop can move down right one square')
        self.assertTrue(self.rules.move_piece((1,5), (5,1), self.board), 'Bishop can move down right more than one square')
        self.assertFalse(self.rules.move_piece((1,5), (2,5), self.board), 'Bishop cannot move linearly')
        
    def testBlackBishopMovementOnEmptyBoard(self):
        self.board.pieces[(3,3)] = Bishop(colors.BLACK)
        
        self.assertTrue(self.rules.move_piece((3,3), (4,4), self.board), 'Bishop can move up right one square')
        self.assertTrue(self.rules.move_piece((4,4), (7,7), self.board), 'Bishop can move up right more than one square')
        self.assertTrue(self.rules.move_piece((7,7), (6,6), self.board), 'Bishop can move down left one square')
        self.assertTrue(self.rules.move_piece((6,6), (3,3), self.board), 'Bishop can move down left more than one square')
        self.assertTrue(self.rules.move_piece((3,3), (2,4), self.board), 'Bishop can move up left one square')
        self.assertTrue(self.rules.move_piece((2,4), (0,6), self.board), 'Bishop can move up left more than one square')
        self.assertTrue(self.rules.move_piece((0,6), (1,5), self.board), 'Bishop can move down right one square')
        self.assertTrue(self.rules.move_piece((1,5), (5,1), self.board), 'Bishop can move down right more than one square')
        self.assertFalse(self.rules.move_piece((1,5), (2,5), self.board), 'Bishop cannot move linearly')
    
    def testWhiteBishopBeingBlocked(self):
        self.board.pieces[(3,3)] = Bishop(colors.WHITE)
        self.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.board.pieces[(4,3)] = Pawn(colors.WHITE)
        self.board.pieces[(3,2)] = Pawn(colors.WHITE)
        self.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.board.pieces[(4,2)] = Pawn(colors.WHITE)
        
        self.assertFalse(self.rules.move_piece((3,3), (4,4), self.board), 'Bishop cannot move up right one square')
        self.assertFalse(self.rules.move_piece((3,3), (7,7), self.board), 'Bishop cannot move up right more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (2,2), self.board), 'Bishop cannot move down left one square')
        self.assertFalse(self.rules.move_piece((3,3), (0,0), self.board), 'Bishop cannot move down left more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (2,4), self.board), 'Bishop cannot move up left one square')
        self.assertFalse(self.rules.move_piece((3,3), (0,6), self.board), 'Bishop cannot move up left more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (4,2), self.board), 'Bishop cannot move down right one square')
        self.assertFalse(self.rules.move_piece((3,3), (6,0), self.board), 'Bishop cannot move down right more than one square')
        
    def testBlackBishopBeingBlocked(self):
        self.board.pieces[(3,3)] = Bishop(colors.BLACK)
        self.board.pieces[(2,3)] = Pawn(colors.BLACK)
        self.board.pieces[(4,3)] = Pawn(colors.BLACK)
        self.board.pieces[(3,2)] = Pawn(colors.BLACK)
        self.board.pieces[(3,4)] = Pawn(colors.BLACK)
        self.board.pieces[(2,2)] = Pawn(colors.BLACK)
        self.board.pieces[(4,4)] = Pawn(colors.BLACK)
        self.board.pieces[(2,4)] = Pawn(colors.BLACK)
        self.board.pieces[(4,2)] = Pawn(colors.BLACK)
        
        self.assertFalse(self.rules.move_piece((3,3), (4,4), self.board), 'Bishop cannot move up right one square')
        self.assertFalse(self.rules.move_piece((3,3), (7,7), self.board), 'Bishop cannot move up right more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (2,2), self.board), 'Bishop cannot move down left one square')
        self.assertFalse(self.rules.move_piece((3,3), (0,0), self.board), 'Bishop cannot move down left more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (2,4), self.board), 'Bishop cannot move up left one square')
        self.assertFalse(self.rules.move_piece((3,3), (0,6), self.board), 'Bishop cannot move up left more than one square')
        self.assertFalse(self.rules.move_piece((3,3), (4,2), self.board), 'Bishop cannot move down right one square')
        self.assertFalse(self.rules.move_piece((3,3), (6,0), self.board), 'Bishop cannot move down right more than one square')

class TestPieceCapture(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testWhiteBishopCapture(self):
        self.board.pieces[(3,3)] = Bishop(colors.WHITE)
        self.board.pieces[(4,4)] = Pawn(colors.BLACK)
        self.board.pieces[(7,7)] = Pawn(colors.BLACK)
        self.board.pieces[(2,4)] = Pawn(colors.BLACK)
        self.board.pieces[(0,6)] = Pawn(colors.BLACK)
        self.board.pieces[(5,1)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.rules.move_piece((3,3), (4,4), self.board), 'Bishop can move up right one square')
        self.assertTrue(self.rules.move_piece((4,4), (7,7), self.board), 'Bishop can move up right more than one square')
        self.assertTrue(self.rules.move_piece((7,7), (6,6), self.board), 'Bishop can move down left one square')
        self.assertTrue(self.rules.move_piece((6,6), (3,3), self.board), 'Bishop can move down left more than one square')
        self.assertTrue(self.rules.move_piece((3,3), (2,4), self.board), 'Bishop can move up left one square')
        self.assertTrue(self.rules.move_piece((2,4), (0,6), self.board), 'Bishop can move up left more than one square')
        self.assertTrue(self.rules.move_piece((0,6), (1,5), self.board), 'Bishop can move down right one square')
        self.assertTrue(self.rules.move_piece((1,5), (5,1), self.board), 'Bishop can move down right more than one square')
        
    def testBlackBishopCapture(self):
        self.board.pieces[(3,3)] = Bishop(colors.BLACK)
        self.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.board.pieces[(7,7)] = Pawn(colors.WHITE)
        self.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.board.pieces[(0,6)] = Pawn(colors.WHITE)
        self.board.pieces[(5,1)] = Pawn(colors.WHITE)
        
        self.assertTrue(self.rules.move_piece((3,3), (4,4), self.board), 'Bishop can move up right one square')
        self.assertTrue(self.rules.move_piece((4,4), (7,7), self.board), 'Bishop can move up right more than one square')
        self.assertTrue(self.rules.move_piece((7,7), (6,6), self.board), 'Bishop can move down left one square')
        self.assertTrue(self.rules.move_piece((6,6), (3,3), self.board), 'Bishop can move down left more than one square')
        self.assertTrue(self.rules.move_piece((3,3), (2,4), self.board), 'Bishop can move up left one square')
        self.assertTrue(self.rules.move_piece((2,4), (0,6), self.board), 'Bishop can move up left more than one square')
        self.assertTrue(self.rules.move_piece((0,6), (1,5), self.board), 'Bishop can move down right one square')
        self.assertTrue(self.rules.move_piece((1,5), (5,1), self.board), 'Bishop can move down right more than one square')
        
    def testWhitePawnCapture(self):
        self.board.pieces[(1,3)] = Pawn(colors.WHITE)
        self.board.pieces[(2,4)] = Pawn(colors.BLACK)
        self.board.pieces[(3,3)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.rules.move_piece((1,3), (2,4), self.board), 'Pawn may capture to the right')
        self.assertTrue(self.rules.move_piece((2,4), (3,3), self.board), 'Pawn may capture to the left')
        
    def testBlackPawnCapture(self):
        self.board.set_square_to_piece('d5', Pawn(colors.BLACK))
        self.board.set_square_to_piece('c4', Pawn(colors.WHITE))
        self.board.set_square_to_piece('d3', Pawn(colors.WHITE))
        
        self.assertTrue(self.rules.move_piece('d5', 'c4', self.board), 'Pawn may capture to the left')
        self.assertTrue(self.rules.move_piece('c4', 'd3', self.board), 'Pawn may capture to the right')
    
    def testWhitePawnCannotCaptureOwnPiece(self):
        self.board.pieces[(1,3)] = Pawn(colors.WHITE)
        self.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,2)] = Pawn(colors.WHITE)
        
        self.assertFalse(self.rules.move_piece((1,3), (2,4), self.board), 'Pawn cannot capture to the right')
        self.assertFalse(self.rules.move_piece((1,3), (2,2), self.board), 'Pawn cannot capture to the left')
        
    def testBlackPawnCannotCaptureOwnPiece(self):
        self.board.set_square_to_piece('d5', Pawn(colors.BLACK))
        self.board.set_square_to_piece('c4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('e4', Pawn(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('d5', 'c4', self.board), 'Pawn cannot capture to the right')
        self.assertFalse(self.rules.move_piece('d5', 'e4', self.board), 'Pawn cannot capture to the left')
        
    def testWhitePawnCannotAttackEmptySquare(self):
        self.board.set_square_to_piece('e5', Pawn(colors.WHITE))
        self.assertFalse(self.rules.move_piece('e5', 'd6', self.board), 'Pawn cannot attack empty square')
        self.assertFalse(self.rules.move_piece('e5', 'f6', self.board), 'Pawn cannot attack empty square')
        
    def testBlackPawnCannotAttackEmptySquare(self):
        self.board.set_square_to_piece('e5', Pawn(colors.BLACK))
        self.assertFalse(self.rules.move_piece('e5', 'd4', self.board), 'Pawn cannot attack empty square')
        self.assertFalse(self.rules.move_piece('e5', 'f4', self.board), 'Pawn cannot attack empty square')
        
    def testWhiteRookCapture(self):
        self.board.pieces[(3,3)] = Rook(colors.WHITE)
        self.board.pieces[(3,4)] = Pawn(colors.BLACK)
        self.board.pieces[(3,7)] = Pawn(colors.BLACK)
        self.board.pieces[(3,1)] = Pawn(colors.BLACK)
        self.board.pieces[(3,0)] = Pawn(colors.BLACK)
        self.board.pieces[(4,0)] = Pawn(colors.BLACK)
        self.board.pieces[(7,0)] = Pawn(colors.BLACK)
        self.board.pieces[(1,0)] = Pawn(colors.BLACK)
        self.board.pieces[(0,0)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.rules.move_piece((3,3), (3,4), self.board), 'Rook can move right one square')
        self.assertTrue(self.rules.move_piece((3,4), (3,7), self.board), 'Rook can move right more than one square')
        self.assertTrue(self.rules.move_piece((3,7), (3,1), self.board), 'Rook can move left more than one square')
        self.assertTrue(self.rules.move_piece((3,1), (3,0), self.board), 'Rook can move left one square')
        self.assertTrue(self.rules.move_piece((3,0), (4,0), self.board), 'Rook can move up one square')
        self.assertTrue(self.rules.move_piece((4,0), (7,0), self.board), 'Rook can move up more than one square')
        self.assertTrue(self.rules.move_piece((7,0), (1,0), self.board), 'Rook can move down more than one square')
        self.assertTrue(self.rules.move_piece((1,0), (0,0), self.board), 'Rook can move down one square')
        
    def testBlackRookCapture(self):
        self.board.pieces[(3,3)] = Rook(colors.BLACK)
        self.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.board.pieces[(3,7)] = Pawn(colors.WHITE)
        self.board.pieces[(3,1)] = Pawn(colors.WHITE)
        self.board.pieces[(3,0)] = Pawn(colors.WHITE)
        self.board.pieces[(4,0)] = Pawn(colors.WHITE)
        self.board.pieces[(7,0)] = Pawn(colors.WHITE)
        self.board.pieces[(1,0)] = Pawn(colors.WHITE)
        self.board.pieces[(0,0)] = Pawn(colors.WHITE)
        
        self.assertTrue(self.rules.move_piece((3,3), (3,4), self.board), 'Rook can move right one square')
        self.assertTrue(self.rules.move_piece((3,4), (3,7), self.board), 'Rook can move right more than one square')
        self.assertTrue(self.rules.move_piece((3,7), (3,1), self.board), 'Rook can move left more than one square')
        self.assertTrue(self.rules.move_piece((3,1), (3,0), self.board), 'Rook can move left one square')
        self.assertTrue(self.rules.move_piece((3,0), (4,0), self.board), 'Rook can move up one square')
        self.assertTrue(self.rules.move_piece((4,0), (7,0), self.board), 'Rook can move up more than one square')
        self.assertTrue(self.rules.move_piece((7,0), (1,0), self.board), 'Rook can move down more than one square')
        self.assertTrue(self.rules.move_piece((1,0), (0,0), self.board), 'Rook can move down one square')
        
    def testWhiteKnightCapture(self):
        self.board.pieces[(3,3)] = Knight(colors.WHITE)
        self.board.pieces[(5,4)] = Pawn(colors.BLACK)
        self.board.pieces[(5,2)] = Pawn(colors.BLACK)
        self.board.pieces[(1,4)] = Pawn(colors.BLACK)
        self.board.pieces[(1,2)] = Pawn(colors.BLACK)
        self.board.pieces[(4,5)] = Pawn(colors.BLACK)
        self.board.pieces[(2,5)] = Pawn(colors.BLACK)
        self.board.pieces[(4,1)] = Pawn(colors.BLACK)
        self.board.pieces[(2,1)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.rules.move_piece((3,3), (5,4), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((5,4), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (5,2), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((5,2), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (1,4), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((1,4), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (1,2), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((1,2), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (4,5), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((4,5), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (2,5), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((2,5), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (4,1), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((4,1), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (2,1), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((2,1), (3,3), self.board), 'Knight may move to empty space')
        
    def testBlackKnightCapture(self):
        self.board.pieces[(3,3)] = Knight(colors.BLACK)
        self.board.pieces[(5,4)] = Pawn(colors.WHITE)
        self.board.pieces[(5,2)] = Pawn(colors.WHITE)
        self.board.pieces[(1,4)] = Pawn(colors.WHITE)
        self.board.pieces[(1,2)] = Pawn(colors.WHITE)
        self.board.pieces[(4,5)] = Pawn(colors.WHITE)
        self.board.pieces[(2,5)] = Pawn(colors.WHITE)
        self.board.pieces[(4,1)] = Pawn(colors.WHITE)
        self.board.pieces[(2,1)] = Pawn(colors.WHITE)
        
        self.assertTrue(self.rules.move_piece((3,3), (5,4), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((5,4), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (5,2), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((5,2), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (1,4), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((1,4), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (1,2), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((1,2), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (4,5), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((4,5), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (2,5), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((2,5), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (4,1), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((4,1), (3,3), self.board), 'Knight may move to empty space')
        self.assertTrue(self.rules.move_piece((3,3), (2,1), self.board), 'Knight may capture')
        self.assertTrue(self.rules.move_piece((2,1), (3,3), self.board), 'Knight may move to empty space')
    
    def testWhiteKnightJumpAndCapture(self):
        self.board.pieces[(3,3)] = Knight(colors.WHITE)
        self.board.pieces[(2,3)] = Pawn(colors.WHITE)
        self.board.pieces[(4,3)] = Pawn(colors.WHITE)
        self.board.pieces[(3,2)] = Pawn(colors.WHITE)
        self.board.pieces[(3,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,2)] = Pawn(colors.WHITE)
        self.board.pieces[(4,4)] = Pawn(colors.WHITE)
        self.board.pieces[(2,4)] = Pawn(colors.WHITE)
        self.board.pieces[(4,2)] = Pawn(colors.WHITE)
        self.board.pieces[(5,4)] = Pawn(colors.BLACK)
        self.board.pieces[(5,2)] = Pawn(colors.BLACK)
        self.board.pieces[(1,4)] = Pawn(colors.BLACK)
        self.board.pieces[(1,2)] = Pawn(colors.BLACK)
        self.board.pieces[(4,5)] = Pawn(colors.BLACK)
        self.board.pieces[(2,5)] = Pawn(colors.BLACK)
        self.board.pieces[(4,1)] = Pawn(colors.BLACK)
        self.board.pieces[(2,1)] = Pawn(colors.BLACK)
        
        self.assertTrue(self.rules.move_piece((3,3), (5,4), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((5,4), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (5,2), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((5,2), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (1,4), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((1,4), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (1,2), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((1,2), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (4,5), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((4,5), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (2,5), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((2,5), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (4,1), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((4,1), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (2,1), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((2,1), (3,3), self.board), 'Knight may jump over blockers')
        
    def testBlackKnightJumpAndCapture(self):
        self.board.pieces[(3,3)] = Knight(colors.BLACK)
        self.board.pieces[(2,3)] = Pawn(colors.BLACK)
        self.board.pieces[(4,3)] = Pawn(colors.BLACK)
        self.board.pieces[(3,2)] = Pawn(colors.BLACK)
        self.board.pieces[(3,4)] = Pawn(colors.BLACK)
        self.board.pieces[(2,2)] = Pawn(colors.BLACK)
        self.board.pieces[(4,4)] = Pawn(colors.BLACK)
        self.board.pieces[(2,4)] = Pawn(colors.BLACK)
        self.board.pieces[(4,2)] = Pawn(colors.BLACK)
        
        self.board.pieces[(5,4)] = Pawn(colors.WHITE)
        self.board.pieces[(5,2)] = Pawn(colors.WHITE)
        self.board.pieces[(1,4)] = Pawn(colors.WHITE)
        self.board.pieces[(1,2)] = Pawn(colors.WHITE)
        self.board.pieces[(4,5)] = Pawn(colors.WHITE)
        self.board.pieces[(2,5)] = Pawn(colors.WHITE)
        self.board.pieces[(4,1)] = Pawn(colors.WHITE)
        self.board.pieces[(2,1)] = Pawn(colors.WHITE)
        
        self.assertTrue(self.rules.move_piece((3,3), (5,4), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((5,4), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (5,2), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((5,2), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (1,4), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((1,4), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (1,2), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((1,2), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (4,5), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((4,5), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (2,5), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((2,5), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (4,1), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((4,1), (3,3), self.board), 'Knight may jump over blockers')
        self.assertTrue(self.rules.move_piece((3,3), (2,1), self.board), 'Knight may jump over blockers to capture')
        self.assertTrue(self.rules.move_piece((2,1), (3,3), self.board), 'Knight may jump over blockers')
    
class TestEnPassanteRules(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testWhiteEnPassentToLeft(self):
        black_pawn = Pawn(colors.BLACK)
        black_pawn.times_moved = 1
        self.board.moves.push((black_pawn, None, None))
        
        self.board.set_square_to_piece('e5', Pawn(colors.WHITE))
        self.board.set_square_to_piece('d5', black_pawn)
        
        self.assertTrue(self.rules.move_piece('e5', 'd6', self.board), 'Pawn should be able to en passante to left')
        
    def testBlackEnPassentToLeft(self):
        white_pawn = Pawn(colors.WHITE)
        white_pawn.times_moved = 1
        self.board.moves.push((white_pawn, None, None))
        
        self.board.set_square_to_piece('e4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('d4', white_pawn)
        
        self.assertTrue(self.rules.move_piece('e4', 'd3', self.board), 'Pawn should be able to en passante to left')
        
    def testWhiteEnPassentToRight(self):
        black_pawn = Pawn(colors.BLACK)
        black_pawn.times_moved = 1
        self.board.moves.push((black_pawn, None, None))
        
        self.board.set_square_to_piece('e5', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f5', black_pawn)
        
        self.assertTrue(self.rules.move_piece('e5', 'f6', self.board), 'Pawn should be able to en passante to right')
        
    def testBlackEnPassentToRight(self):
        white_pawn = Pawn(colors.WHITE)
        white_pawn.times_moved = 1
        self.board.moves.push((white_pawn, None, None))
        
        self.board.set_square_to_piece('e4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f4', white_pawn)
        
        self.assertTrue(self.rules.move_piece('e4', 'f3', self.board), 'Pawn should be able to en passante to right')
        
    def testWhiteCannotEnPassentAfterMoreThanOneTurn(self):
        other_piece = Rook(colors.BLACK)
        white_pawn = Pawn(colors.WHITE)
        white_pawn.times_moved = 1
        
        self.board.set_square_to_piece('e5', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f5', white_pawn)
        self.board.set_square_to_piece('a1', other_piece)
        
        self.rules.move_piece('a1', 'a2', self.board)
        self.assertFalse(self.rules.move_piece('f5', 'e6', self.board), 'Pawn cannot en passante after two turns')
        
    def testBlackCannotEnPassentAfterMoreThanOneTurn(self):
        other_piece = Rook(colors.WHITE)
        black_pawn = Pawn(colors.BLACK)
        black_pawn.times_moved = 1
        
        self.board.set_square_to_piece('e4', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f4', black_pawn)
        self.board.set_square_to_piece('a1', other_piece)
        
        self.rules.move_piece('a1', 'a2', self.board)
        self.assertFalse(self.rules.move_piece('f4', 'e3', self.board), 'Pawn cannot en passante after two turns')
    
    def testWhiteCannotEnPassentPawnThatHasMovedTwoSpacesOneAtATime(self):
        black_pawn = Pawn(colors.BLACK)
        black_pawn.times_moved = 2
        self.board.moves.push((black_pawn, None, None))
        
        self.board.set_square_to_piece('e5', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f5', black_pawn)
        
        self.assertFalse(self.rules.move_piece('e5', 'f6', self.board), 'Pawn cannot en passante after two moves')
    
    def testBlackCannotEnPassentPawnThatHasMovedTwoSpacesOneAtATime(self):
        white_pawn = Pawn(colors.WHITE)
        white_pawn.times_moved = 2
        self.board.moves.push((white_pawn, None, None))
        
        self.board.set_square_to_piece('e4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f4', white_pawn)
        
        self.assertFalse(self.rules.move_piece('e4', 'f3', self.board), 'Pawn cannot en passante after two moves')
    
    def testWhiteCannotEnPassentNonPawn(self):
        black_rook = Rook(colors.BLACK)
        black_rook.times_moved = 1
        self.board.moves.push((black_rook, None, None))
        
        self.board.set_square_to_piece('e5', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f5', black_rook)
        
        self.assertFalse(self.rules.move_piece('e5', 'f6', self.board), 'Pawn cannot en passante a non-pawn')
    
    def testBlackCannotEnPassentNonPawn(self):
        white_rook = Rook(colors.WHITE)
        white_rook.times_moved = 1
        self.board.moves.push((white_rook, None, None))
        
        self.board.set_square_to_piece('e4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f4', white_rook)
        
        self.assertFalse(self.rules.move_piece('e4', 'f3', self.board), 'Pawn cannot en passante a non-pawn')
    
    def testWhiteCannotEnPassentOwnPiece(self):
        #Would this even happen?
        white_pawn = Pawn(colors.BLACK)
        white_pawn.times_moved = 1
        self.board.moves.push((white_pawn, None, None))
        
        self.board.set_square_to_piece('e5', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f5', white_pawn)
        
        self.assertFalse(self.rules.move_piece('e5', 'f6', self.board), 'Pawn cannot en passante own pawn')
    
    def testBlackCannotEnPassentOwnPiece(self):
        #Would this even happen?
        black_pawn = Pawn(colors.BLACK)
        black_pawn.times_moved = 1
        self.board.moves.push((black_pawn, None, None))
        
        self.board.set_square_to_piece('e4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f4', black_pawn)
        
        self.assertFalse(self.rules.move_piece('e4', 'f3', self.board), 'Pawn cannot en passante own pawn')

class TestCastlingRules(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testCastleVariablesAreSetCorrectlyWhenWhiteKingMoves(self):
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('e1', 'e2', self.board)
        
        self.assertFalse(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be false')
        self.assertFalse(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be false')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
    def testCastleVariablesAreSetCorrectlyWhenBlackKingMoves(self):
        self.board.set_square_to_piece('e8', King(colors.BLACK))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('e8', 'e7', self.board)
        
        self.assertFalse(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be false')
        self.assertFalse(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be false')
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        
    def testCastleVariablesAreSetCorrectlyWhenWhiteARookMoves(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('a1', 'a2', self.board)
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertFalse(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be false')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
    def testCastleVariablesAreSetCorrectlyWhenWhiteHRookMoves(self):
        self.board.set_square_to_piece('h1', Rook(colors.WHITE))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('h1', 'h2', self.board)
        
        self.assertFalse(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be false')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
    def testCastleVariablesAreSetCorrectlyWhenBlackARookMoves(self):
        self.board.set_square_to_piece('a8', Rook(colors.BLACK))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('a8', 'a7', self.board)
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertFalse(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be false')
        
    def testCastleVariablesAreSetCorrectlyWhenBlackHRookMoves(self):
        self.board.set_square_to_piece('h8', Rook(colors.BLACK))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('h8', 'h7', self.board)
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertFalse(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be false')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
    def testCastleVariablesAreSetCorrectlyWhenWhiteKingsideCastles(self):
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.set_square_to_piece('h1', Rook(colors.WHITE))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('e1', 'g1', self.board)
        
        self.assertFalse(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be false')
        self.assertFalse(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be false')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
    def testCastleVariablesAreSetCorrectlyWhenWhiteQueensideCastles(self):
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('e1', 'c1', self.board)
        
        self.assertFalse(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be false')
        self.assertFalse(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be false')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
    
    def testCastleVariablesAreSetCorrectlyWhenBlackKingsideCastles(self):
        self.board.set_square_to_piece('e8', King(colors.BLACK))
        self.board.set_square_to_piece('h8', Rook(colors.BLACK))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('e8', 'g8', self.board)
        
        self.assertFalse(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be false')
        self.assertFalse(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be false')
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        
    def testCastleVariablesAreSetCorrectlyWhenBlackQueensideCastles(self):
        self.board.set_square_to_piece('e8', King(colors.BLACK))
        self.board.set_square_to_piece('a8', Rook(colors.BLACK))
        
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be true')
        
        self.rules.move_piece('e8', 'c8', self.board)
        
        self.assertFalse(self.rules.game_variables['black_can_kingside_castle'], 'Black kingside castle variable should be false')
        self.assertFalse(self.rules.game_variables['black_can_queenside_castle'], 'Black queenside castle variable should be false')
        self.assertTrue(self.rules.game_variables['white_can_kingside_castle'], 'White kingside castle variable should be true')
        self.assertTrue(self.rules.game_variables['white_can_queenside_castle'], 'White queenside castle variable should be true')
    
    def testWhiteCanKingSideCastle(self):
        rook = Rook(colors.WHITE)
        king = King(colors.WHITE)
        self.board.set_square_to_piece('h1', rook)
        self.board.set_square_to_piece('e1', king)
        
        self.assertTrue(self.rules.move_piece('e1', 'g1', self.board), 'King should be able to castle')
        self.assertEqual(self.board.get_square('h1'), None, 'h1 should be NoneType but is %s' % self.board.get_square('h1'))
        self.assertTrue(self.board.get_square('g1') is king, 'Piece on g1 should be the king')
        self.assertTrue(self.board.get_square('f1') is rook, 'Piece on f1 should be the rook')
        
    def testBlackCanKingSideCastle(self):
        rook = Rook(colors.BLACK)
        king = King(colors.BLACK)
        self.board.set_square_to_piece('h8', rook)
        self.board.set_square_to_piece('e8', king)
        
        self.assertTrue(self.rules.move_piece('e8', 'g8', self.board), 'King should be able to castle')
        self.assertEqual(self.board.get_square('h8'), None, 'h8 should be NoneType but is %s' % self.board.get_square('h8'))
        self.assertTrue(self.board.get_square('g8') is king, 'Piece on g8 should be the king')
        self.assertTrue(self.board.get_square('f8') is rook, 'Piece on f8 should be the rook')
        
    def testWhiteCanQueenSideCastle(self):
        rook = Rook(colors.WHITE)
        king = King(colors.WHITE)
        self.board.set_square_to_piece('a1', rook)
        self.board.set_square_to_piece('e1', king)
        
        self.assertTrue(self.rules.move_piece('e1', 'c1', self.board), 'King should be able to castle')
        self.assertEqual(self.board.get_square('a1'), None, 'a1 should be NoneType but is %s' % self.board.get_square('a1'))
        self.assertTrue(self.board.get_square('c1') is king, 'Piece on g1 should be the king')
        self.assertTrue(self.board.get_square('d1') is rook, 'Piece on f1 should be the rook')
        
    def testBlackCanQueenSideCastle(self):
        rook = Rook(colors.BLACK)
        king = King(colors.BLACK)
        self.board.set_square_to_piece('a8', rook)
        self.board.set_square_to_piece('e8', king)
        
        self.assertTrue(self.rules.move_piece('e8', 'c8', self.board), 'King should be able to castle')
        self.assertEqual(self.board.get_square('a8'), None, 'a8 should be NoneType but is %s' % self.board.get_square('a8'))
        self.assertTrue(self.board.get_square('c8') is king, 'Piece on g8 should be the king')
        self.assertTrue(self.board.get_square('d8') is rook, 'Piece on f8 should be the rook')
        
    def testWhiteCannotCastleWhenPiecesBlocking(self):
        a_rook = Rook(colors.WHITE)
        h_rook = Rook(colors.WHITE)
        king = King(colors.WHITE)
        queen = Queen(colors.WHITE)
        bishop = Bishop(colors.WHITE)
        self.board.set_square_to_piece('a1', a_rook)
        self.board.set_square_to_piece('h1', h_rook)
        self.board.set_square_to_piece('e1', king)
        self.board.set_square_to_piece('d1', queen)
        self.board.set_square_to_piece('f1', bishop)
        
        self.assertFalse(self.rules.move_piece('e1', 'g1', self.board), 'King should not be able to king side castle')
        self.assertFalse(self.rules.move_piece('e1', 'c1', self.board), 'King should not be able to queen side castle')
        
        self.assertTrue(self.board.get_square('e1') is king, 'Piece on e1 should be the king')
        self.assertTrue(self.board.get_square('a1') is a_rook, 'Piece on a1 should be the a rook')
        self.assertTrue(self.board.get_square('h1') is h_rook, 'Piece on h1 should be the h rook')
        self.assertTrue(self.board.get_square('d1') is queen, 'Piece on d1 should be the queen')
        self.assertTrue(self.board.get_square('f1') is bishop, 'Piece on f1 should be a bishop')
        
    def testBlackCannotCastleWhenPiecesBlocking(self):
        a_rook = Rook(colors.BLACK)
        h_rook = Rook(colors.BLACK)
        king = King(colors.BLACK)
        queen = Queen(colors.BLACK)
        bishop = Bishop(colors.BLACK)
        self.board.set_square_to_piece('a8', a_rook)
        self.board.set_square_to_piece('h8', h_rook)
        self.board.set_square_to_piece('e8', king)
        self.board.set_square_to_piece('d8', queen)
        self.board.set_square_to_piece('f8', bishop)
        
        self.assertFalse(self.rules.move_piece('e8', 'g8', self.board), 'King should not be able to king side castle')
        self.assertFalse(self.rules.move_piece('e8', 'c8', self.board), 'King should not be able to queen side castle')
        
        self.assertTrue(self.board.get_square('e8') is king, 'Piece on e8 should be the king')
        self.assertTrue(self.board.get_square('a8') is a_rook, 'Piece on a8 should be the a rook')
        self.assertTrue(self.board.get_square('h8') is h_rook, 'Piece on h8 should be the h rook')
        self.assertTrue(self.board.get_square('d8') is queen, 'Piece on d8 should be the queen')
        self.assertTrue(self.board.get_square('f8') is bishop, 'Piece on f8 should be a bishop')
        
    def testWhiteCannotCastleWhenKingHasMoved(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        self.board.set_square_to_piece('h1', Rook(colors.WHITE))
        self.board.set_square_to_piece('e1', King(colors.WHITE, times_moved=1))
        
        self.assertFalse(self.rules.move_piece('e1', 'g1', self.board), 'King should not be able to king side castle')
        self.assertFalse(self.rules.move_piece('e1', 'c1', self.board), 'King should not be able to queen side castle')
        
    def testBlackCannotCastleWhenKingHasMoved(self):
        self.board.set_square_to_piece('a8', Rook(colors.WHITE))
        self.board.set_square_to_piece('h8', Rook(colors.WHITE))
        self.board.set_square_to_piece('e8', King(colors.WHITE, times_moved=1))
        
        self.assertFalse(self.rules.move_piece('e8', 'g8', self.board), 'King should not be able to king side castle')
        self.assertFalse(self.rules.move_piece('e8', 'c8', self.board), 'King should not be able to queen side castle')
        
    def testWhiteCannotCastleWhenRooksHaveMoved(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE, times_moved=1))
        self.board.set_square_to_piece('h1', Rook(colors.WHITE, times_moved=1))
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e1', 'g1', self.board), 'King should not be able to king side castle')
        self.assertFalse(self.rules.move_piece('e1', 'c1', self.board), 'King should not be able to queen side castle')
        
    def testBlackCannotCastleWhenRooksHaveMoved(self):
        self.board.set_square_to_piece('a8', Rook(colors.BLACK, times_moved=1))
        self.board.set_square_to_piece('h8', Rook(colors.BLACK, times_moved=1))
        self.board.set_square_to_piece('e8', King(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('e8', 'g8', self.board), 'King should not be able to king side castle')
        self.assertFalse(self.rules.move_piece('e8', 'c8', self.board), 'King should not be able to queen side castle')
        
    def testWhiteKingCannotMoveTwoSquaresNormally(self):
        self.board.set_square_to_piece('e4', King(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e4', 'g4', self.board), 'King should not be able to move 2 squares')
        self.assertFalse(self.rules.move_piece('e4', 'c4', self.board), 'King should not be able to move 2 squares')
        
    def testBlackKingCannotMoveTwoSquaresNormally(self):
        self.board.set_square_to_piece('e4', King(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('e4', 'g4', self.board), 'King should not be able to move 2 squares')
        self.assertFalse(self.rules.move_piece('e4', 'c4', self.board), 'King should not be able to move 2 squares')
        
    def testWhiteKingCannotMoveTwoSquaresNormallyFromHomeSquare(self):
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e1', 'g1', self.board), 'King should not be able to move 2 squares')
        self.assertFalse(self.rules.move_piece('e1', 'c1', self.board), 'King should not be able to move 2 squares')
        
    def testBlackKingCannotMoveTwoSquaresNormallyFromHomeSquare(self):
        self.board.set_square_to_piece('e8', King(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e8', 'g8', self.board), 'King should not be able to move 2 squares')
        self.assertFalse(self.rules.move_piece('e8', 'c8', self.board), 'King should not be able to move 2 squares')

class TestCheckRules(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testWhiteKingCannotCastleThroughCheck(self):
        white_rook = Rook(colors.WHITE)
        king = King(colors.WHITE)
        self.board.set_square_to_piece('h1', white_rook)
        self.board.set_square_to_piece('e1', king)
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('e1', 'g1', self.board), 'King should not be able to castle through check')
        self.assertTrue(self.board.get_square('e1') is king, 'Piece on e1 should be the king')
        self.assertTrue(self.board.get_square('h1') is white_rook, 'Piece on h1 should be the white rook')
        
    def testBlackKingCannotCastleThroughCheck(self):
        black_rook = Rook(colors.BLACK)
        king = King(colors.BLACK)
        self.board.set_square_to_piece('h8', black_rook)
        self.board.set_square_to_piece('e8', king)
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e8')
        self.board.set_square_to_piece('f1', Rook(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e8', 'g8', self.board), 'King should not be able to castle through check')
        self.assertTrue(self.board.get_square('e8') is king, 'Piece on e8 should be the king')
        self.assertTrue(self.board.get_square('h8') is black_rook, 'Piece on h8 should be the black rook')
    
    def testWhiteKingCannotCastleIntoCheck(self):
        white_rook = Rook(colors.WHITE)
        king = King(colors.WHITE)
        self.board.set_square_to_piece('h1', white_rook)
        self.board.set_square_to_piece('e1', king)
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('g8', Rook(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('e1', 'g1', self.board), 'King should not be able to castle into check')
        self.assertTrue(self.board.get_square('e1') is king, 'Piece on e1 should be the king')
        self.assertTrue(self.board.get_square('h1') is white_rook, 'Piece on h1 should be the white rook')
        
    def testBlackKingCannotCastleThroughCheck(self):
        black_rook = Rook(colors.BLACK)
        king = King(colors.BLACK)
        self.board.set_square_to_piece('h8', black_rook)
        self.board.set_square_to_piece('e8', king)
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e8')
        self.board.set_square_to_piece('g1', Rook(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e8', 'g8', self.board), 'King should not be able to castle through check')
        self.assertTrue(self.board.get_square('e8') is king, 'Piece on e8 should be the king')
        self.assertTrue(self.board.get_square('h8') is black_rook, 'Piece on h8 should be the black rook')
        
    def testWhiteKingCannotMoveIntoCheck(self):
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('e1', 'f1', self.board), 'King should not be able to move into check')
        
    def testBlackKingCannotMoveIntoCheck(self):
        self.board.set_square_to_piece('e1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('f8', Rook(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e1', 'f1', self.board), 'King should not be able to move into check')
        
    def testWhiteKingCanMoveWhenCheckIsBlockedByOwnPiece(self):
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('f5', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        
        self.assertTrue(self.rules.move_piece('e1', 'f1', self.board), 'King should be able to move into area blocked')
        
    def testBlackKingCanMoveWhenCheckIsBlockedByOwnPiece(self):
        self.board.set_square_to_piece('e1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('f5', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f8', Rook(colors.WHITE))
        
        self.assertTrue(self.rules.move_piece('e1', 'f1', self.board), 'King should be able to move into area blocked')
        
    def testWhiteKingCanMoveWhenCheckIsBlockedByOtherPiece(self):
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('f5', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        
        self.assertTrue(self.rules.move_piece('e1', 'f1', self.board), 'King should be able to move into area blocked')
        
    def testBlackKingCanMoveWhenCheckIsBlockedByOtherPiece(self):
        self.board.set_square_to_piece('e1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('f5', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f8', Rook(colors.WHITE))
        
        self.assertTrue(self.rules.move_piece('e1', 'f1', self.board), 'King should be able to move into area blocked')
    
    def testWhiteCannotMovePinnedPiece(self):
        self.board.set_square_to_piece('f1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('f5', Bishop(colors.WHITE))
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('f5', 'e4', self.board), 'Bishop is pinned')
        
    def testBlackCannotMovePinnedPiece(self):
        self.board.set_square_to_piece('f1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('f5', Bishop(colors.BLACK))
        self.board.set_square_to_piece('f8', Rook(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('f5', 'e4', self.board), 'Bishop is pinned')
        
    def testWhiteCannotMovePinnedRook(self):
        self.board.set_square_to_piece('e2', Rook(colors.WHITE))
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('e8', Rook(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('e2', 'b2', self.board), 'Rook is pinned')
        
    def testBlackCannotMovePinnedRook(self):
        self.board.set_square_to_piece('e2', Rook(colors.BLACK))
        self.board.set_square_to_piece('e1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('e8', Rook(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e2', 'b2', self.board), 'Rook is pinned')
        
    def testWhiteCannotEnPassanteIntoCheck(self):
        black_pawn = Pawn(colors.BLACK, times_moved=1)
        self.board.moves.push((black_pawn, None, None))
        
        self.board.set_square_to_piece('f1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('f5', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        self.board.set_square_to_piece('g5', black_pawn)
        
        self.assertFalse(self.rules.move_piece('f5', 'g6', self.board), 'Pawn is pinned')
        
    def testBlackCannotEnPassanteIntoCheck(self):
        white_pawn = Pawn(colors.WHITE, times_moved=1)
        self.board.moves.push((white_pawn, None, None))
        
        self.board.set_square_to_piece('f1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('f4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f8', Rook(colors.WHITE))
        self.board.set_square_to_piece('g4', white_pawn)
        
        self.assertFalse(self.rules.move_piece('f4', 'g3', self.board), 'Pawn is pinned')
    
    def testWhiteKingMustMoveWhenInCheck(self):
        self.board.set_square_to_piece('f1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('e5', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('e5', 'e6', self.board), 'King must move out of check')
        
    def testBlackKingMustMoveWhenInCheck(self):
        self.board.set_square_to_piece('f1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('e5', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f8', Rook(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e5', 'e6', self.board), 'King must move out of check')
        
    def testWhiteKingIsCheckedByPawn(self):
        self.board.set_square_to_piece('e4', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('e5', Pawn(colors.BLACK))
        
        self.assertFalse(self.rules.move_piece('e4', 'd4', self.board), 'King cannot move into check')
        self.assertFalse(self.rules.move_piece('e4', 'f4', self.board), 'King cannot move into check')
        
    def testBlackKingIsCheckedByPawn(self):
        self.board.set_square_to_piece('e5', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('e4', Pawn(colors.WHITE))
        
        self.assertFalse(self.rules.move_piece('e5', 'd5', self.board), 'King cannot move into check')
        self.assertFalse(self.rules.move_piece('e5', 'f5', self.board), 'King cannot move into check')
    
    def testWhiteCanBlockCheckingPiece(self):
        self.board.set_square_to_piece('f1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('e5', Rook(colors.WHITE))
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        
        self.assertTrue(self.rules.move_piece('e5', 'f5', self.board), 'Rook may block checking piece')
        
    def testBlackCanBlockCheckingPiece(self):
        self.board.set_square_to_piece('f1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('e5', Rook(colors.BLACK))
        self.board.set_square_to_piece('f8', Rook(colors.WHITE))
        
        self.assertTrue(self.rules.move_piece('e5', 'f5', self.board), 'Rook may block checking piece')
        
    def testWhiteCanTakeCheckingPiece(self):
        self.board.set_square_to_piece('f1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('e8', Rook(colors.WHITE))
        self.board.set_square_to_piece('f8', Rook(colors.BLACK))
        
        self.assertTrue(self.rules.move_piece('e8', 'f8', self.board), 'Rook may take checking piece')
        
    def testBlackCanTakeCheckingPiece(self):
        self.board.set_square_to_piece('f1', King(colors.BLACK))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('f1')
        self.board.set_square_to_piece('e8', Rook(colors.BLACK))
        self.board.set_square_to_piece('f8', Rook(colors.WHITE))
        
        self.assertTrue(self.rules.move_piece('e8', 'f8', self.board), 'Rook may take checking piece')

class TestFiftyMoveRule(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testMoveCounterIncrementedOnGeneralMove(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        self.board.set_square_to_piece('h8', Rook(colors.BLACK))
        
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Fifty move counter should be 0')
        
        self.rules.move_piece('a1', 'b1', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 1, 'Fifty move counter should be 1')
        self.rules.move_piece('h8', 'h7', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 2, 'Fifty move counter should be 2')
        self.rules.move_piece('b1', 'b8', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 3, 'Fifty move counter should be 3')
    
    def testMoveCounterIncrementedOnCastle(self):
        self.board.set_square_to_piece('h1', Rook(colors.WHITE))
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.set_square_to_piece('a8', Rook(colors.BLACK))
        self.board.set_square_to_piece('e8', King(colors.BLACK))
        
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Fifty move counter should be 0')
        
        self.rules.move_piece('e1', 'g1', self.board)
        self.rules.move_piece('e8', 'c8', self.board)
        
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 2, 'Fifty move counter should be 2')
        
    
    def testMoveCounterDoesGetResetOnCapture(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        self.board.set_square_to_piece('h8', Rook(colors.BLACK))
        
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Fifty move counter should be 0')
        
        self.rules.move_piece('a1', 'a8', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 1, 'Fifty move counter should be 1')
        self.rules.move_piece('h8', 'a8', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Fifty move counter should be 0')
    
    def testMoveCounterDoesGetResetOnPawnMove(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        self.board.set_square_to_piece('h8', Rook(colors.BLACK))
        self.board.set_square_to_piece('e7', Pawn(colors.BLACK))
        
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Fifty move counter should be 0')
        
        self.rules.move_piece('a1', 'b1', self.board)
        self.rules.move_piece('h8', 'h7', self.board)
        self.rules.move_piece('a1', 'b8', self.board)
        self.rules.move_piece('e7', 'e5', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Fifty move counter should be 0')
        
    def testMoveCounterDoesNotResetOnNormalPieceMove(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        self.board.set_square_to_piece('b1', Knight(colors.WHITE))
        self.board.set_square_to_piece('c1', Bishop(colors.WHITE))
        self.board.set_square_to_piece('d1', Queen(colors.WHITE))
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        
        self.rules.move_piece('a1', 'a2', self.board)
        self.assertNotEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should not be zero')
        self.rules.move_piece('b1', 'c3', self.board)
        self.assertNotEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should not be zero')
        self.rules.move_piece('c1', 'b2', self.board)
        self.assertNotEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should not be zero')
        self.rules.move_piece('d1', 'd8', self.board)
        self.assertNotEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should not be zero')
        self.rules.move_piece('e1', 'f1', self.board)
        self.assertNotEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should not be zero')
        
    def testInvalidMoveDoesNotIncrementCount(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should be zero')
        self.rules.move_piece('a1', 'b2', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should be zero')
    
    def testInvalidMoveThroughCheckDoesNotIncrementCount(self):
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.set_square_to_piece('d8', Rook(colors.BLACK))
        
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should be zero')
        self.rules.move_piece('e1', 'd1', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should be zero')
    
    def testInvalidMoveThroughPinnedPieceDoesNotIncrementCount(self):
        self.board.set_square_to_piece('e2', Rook(colors.WHITE))
        self.board.set_square_to_piece('e1', King(colors.WHITE))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.board.set_square_to_piece('e8', Rook(colors.BLACK))
        
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should be zero')
        self.rules.move_piece('e2', 'b2', self.board)
        self.assertEqual(self.rules.game_variables['fifty_move_counter'], 0, 'Counter should be zero')
    
    def testDrawDetectionByFiftyMove(self):
        self.board.set_square_to_piece('a1', Rook(colors.WHITE))
        self.rules.game_variables['fifty_move_counter'] = 99
        
        self.assertFalse(self.rules.is_fifty_move(), 'Should not be a draw')
        self.rules.move_piece('a1', 'a2', self.board)
        self.assertTrue(self.rules.is_fifty_move(), 'Should be a draw')

class TestMiscellaneousRules(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testWhiteKingDictionaryGetsUpdatedOnNormalMove(self):
        #Location should be cleared in setUp method
        self.assertTrue(self.board.kings[colors.WHITE] is None, 'White king location should not be set')
        self.assertTrue(self.board.kings[colors.BLACK] is None, 'Black king location should not be set')
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e4')
        self.assertEqual(self.board.kings[colors.WHITE], self.board.algebraic_to_coordinate_square('e4'), 'White king location not be set to e1')
        
        squares = [(4,4), (3,4), (3,3), (3,4), (4,3), (3,4), (4,5), (3,4)] #up, down, left, right, upleft, downright, upright, downleft
        current = (3,4)
        self.board.set_square_to_piece('e4', King(colors.WHITE))
        for next in squares:
            self.rules.move_piece(current, next, self.board)
            self.assertEqual(self.board.kings[colors.WHITE], next, 'White king location not be set to %s' % str(next))
            self.assertTrue(self.board.kings[colors.BLACK] is None, 'Black king location should not be set')
            current = next
            
    def testBlackKingDictionaryGetsUpdatedOnNormalMove(self):
        #Location should be cleared in setUp method
        self.assertTrue(self.board.kings[colors.WHITE] is None, 'White king location should not be set')
        self.assertTrue(self.board.kings[colors.BLACK] is None, 'Black king location should not be set')
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e4')
        self.assertEqual(self.board.kings[colors.BLACK], self.board.algebraic_to_coordinate_square('e4'), 'Black king location not be set to e1')
        
        squares = [(4,4), (3,4), (3,3), (3,4), (4,3), (3,4), (4,5), (3,4)] #up, down, left, right, upleft, downright, upright, downleft
        current = (3,4)
        self.board.set_square_to_piece('e4', King(colors.BLACK))
        for next in squares:
            self.rules.move_piece(current, next, self.board)
            self.assertTrue(self.board.kings[colors.WHITE] is None, 'White king location should not be set')
            self.assertEqual(self.board.kings[colors.BLACK], next, 'White king location not be set to %s' % str(next))
            current = next
    
    def testWhiteKingDictionaryGetsUpdatedOnKingsideCastle(self):
        rook = Rook(colors.WHITE)
        king = King(colors.WHITE)
        self.board.set_square_to_piece('h1', rook)
        self.board.set_square_to_piece('e1', king)
        
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.assertTrue(self.board.kings[colors.BLACK] is None, 'Black king location should not be set')
        
        self.assertTrue(self.rules.move_piece('e1', 'g1', self.board), 'King should be able to castle')
        self.assertEqual(self.board.kings[colors.WHITE], self.board.algebraic_to_coordinate_square('g1'), 'White king location not be set to g1')
        self.assertTrue(self.board.kings[colors.BLACK] is None, 'Black king location should not be set')
        
    def testBlackKingDictionaryGetsUpdatedOnKingsideCastle(self):
        rook = Rook(colors.BLACK)
        king = King(colors.BLACK)
        self.board.set_square_to_piece('h8', rook)
        self.board.set_square_to_piece('e8', king)
        
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e8')
        self.assertTrue(self.board.kings[colors.WHITE] is None, 'White king location should not be set')
        
        self.assertTrue(self.rules.move_piece('e8', 'g8', self.board), 'King should be able to castle')
        self.assertEqual(self.board.kings[colors.BLACK], self.board.algebraic_to_coordinate_square('g8'), 'Black king location not be set to g8')
        self.assertTrue(self.board.kings[colors.WHITE] is None, 'White king location should not be set')
        
    def testWhiteKingDictionaryGetsUpdatedOnQueensideCastle(self):
        rook = Rook(colors.WHITE)
        king = King(colors.WHITE)
        self.board.set_square_to_piece('a1', rook)
        self.board.set_square_to_piece('e1', king)
        
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('e1')
        self.assertTrue(self.board.kings[colors.BLACK] is None, 'Black king location should not be set')
        
        self.assertTrue(self.rules.move_piece('e1', 'c1', self.board), 'King should be able to castle')
        self.assertEqual(self.board.kings[colors.WHITE], self.board.algebraic_to_coordinate_square('c1'), 'White king location not be set to c1')
        self.assertTrue(self.board.kings[colors.BLACK] is None, 'Black king location should not be set')
        
    def testBlackKingDictionaryGetsUpdatedOnQueensideCastle(self):
        rook = Rook(colors.BLACK)
        king = King(colors.BLACK)
        self.board.set_square_to_piece('a8', rook)
        self.board.set_square_to_piece('e8', king)
        
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('e8')
        self.assertTrue(self.board.kings[colors.WHITE] is None, 'White king location should not be set')
        
        self.assertTrue(self.rules.move_piece('e8', 'c8', self.board), 'King should be able to castle')
        self.assertEqual(self.board.kings[colors.BLACK], self.board.algebraic_to_coordinate_square('c8'), 'White king location not be set to c8')
        self.assertTrue(self.board.kings[colors.WHITE] is None, 'White king location should not be set')
        
class TestStalemateRules(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testWhiteStalemateWithNoOtherPieces(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('f2', Rook(colors.BLACK))
        self.board.set_square_to_piece('b8', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_stalemate(colors.WHITE, self.board), 'White is stalemated')
        
    def testBlackStalemateWithNoOtherPieces(self):
        self.board.set_square_to_piece('a1', King(colors.BLACK))
        self.board.set_square_to_piece('f2', Rook(colors.WHITE))
        self.board.set_square_to_piece('b8', Rook(colors.WHITE))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_stalemate(colors.BLACK, self.board), 'Black is stalemated')
        
    def testWhiteStalemateWithBlockedPawns(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('c3', Pawn(colors.WHITE))
        self.board.set_square_to_piece('c4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f2', Rook(colors.BLACK))
        self.board.set_square_to_piece('b8', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_stalemate(colors.WHITE, self.board), 'White is stalemated')
        
    def testBlackStalemateWithBlockedPawns(self):
        self.board.set_square_to_piece('a1', King(colors.BLACK))
        self.board.set_square_to_piece('c4', Pawn(colors.BLACK))
        self.board.set_square_to_piece('c3', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f2', Rook(colors.WHITE))
        self.board.set_square_to_piece('b8', Rook(colors.WHITE))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_stalemate(colors.BLACK, self.board), 'Black is stalemated')
        
    def testWhiteIsNotStalematedWithOtherPiecesToMove(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('e6', Pawn(colors.WHITE))
        self.board.set_square_to_piece('f2', Rook(colors.BLACK))
        self.board.set_square_to_piece('b8', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertFalse(self.rules.is_stalemate(colors.WHITE, self.board), 'White is not stalemated')
        
    def testBlackIsNotStalematedWithOtherPiecesToMove(self):
        self.board.set_square_to_piece('a1', King(colors.BLACK))
        self.board.set_square_to_piece('e6', Pawn(colors.BLACK))
        self.board.set_square_to_piece('f2', Rook(colors.WHITE))
        self.board.set_square_to_piece('b8', Rook(colors.WHITE))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertFalse(self.rules.is_stalemate(colors.BLACK, self.board), 'Black is not stalemated')
        
    def testWhiteIsNotStalematedWithKingToMove(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('f3', Rook(colors.BLACK))
        self.board.set_square_to_piece('b8', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertFalse(self.rules.is_stalemate(colors.WHITE, self.board), 'White is not stalemated')
        
    def testBlackIsNotStalematedWithKingToMove(self):
        self.board.set_square_to_piece('a1', King(colors.BLACK))
        self.board.set_square_to_piece('f3', Rook(colors.WHITE))
        self.board.set_square_to_piece('b8', Rook(colors.WHITE))
        self.board.kings[colors.BLACK] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertFalse(self.rules.is_stalemate(colors.BLACK, self.board), 'Black is not stalemated')
        
    def testWhiteIsStalemateWithOwnPieceBlocking(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('a2', Pawn(colors.WHITE))
        self.board.set_square_to_piece('a3', Pawn(colors.BLACK))
        self.board.set_square_to_piece('b8', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_stalemate(colors.WHITE, self.board), 'White is stalemated')
        
class TestCheckmateRules(unittest.TestCase):

    def setUp(self):
        self.rules = VanillaRules()
        self.board = ClassicBoard()
        self.board.clear_board()

    def tearDown(self):
        pass
    
    def testWhiteIsCheckmatedWithNoOtherPieces(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('f2', Rook(colors.BLACK))
        self.board.set_square_to_piece('b8', Rook(colors.BLACK))
        self.board.set_square_to_piece('c3', Bishop(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_checkmate(colors.WHITE, self.board), 'White is checkmated')
        
    def testWhiteIsCheckmatedWithOwnPiecesBlocking(self):
        self.board.set_square_to_piece('g1', King(colors.WHITE))
        self.board.set_square_to_piece('f2', Pawn(colors.WHITE))
        self.board.set_square_to_piece('g2', Pawn(colors.WHITE))
        self.board.set_square_to_piece('h2', Pawn(colors.WHITE))
        self.board.set_square_to_piece('a1', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('g1')
        
        self.assertTrue(self.rules.is_checkmate(colors.WHITE, self.board), 'White is checkmated')
        
    def testWhiteIsCheckmatedWithPinnedAndGuardedPiece(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('a2', Rook(colors.WHITE))
        self.board.set_square_to_piece('b2', Queen(colors.BLACK))
        self.board.set_square_to_piece('a8', Rook(colors.BLACK))
        self.board.set_square_to_piece('b3', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_checkmate(colors.WHITE, self.board), 'White is checkmated')
        
    def testWhiteCanBlockCheckmate(self):
        self.board.set_square_to_piece('b1', King(colors.WHITE))
        self.board.set_square_to_piece('c5', Rook(colors.WHITE))
        self.board.set_square_to_piece('g1', Rook(colors.BLACK))
        self.board.set_square_to_piece('f2', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('b1')
        
        self.assertFalse(self.rules.is_checkmate(colors.WHITE, self.board), 'White can block with rook')
        
    def testWhiteCanTakeCheckmate(self):
        self.board.set_square_to_piece('b1', King(colors.WHITE))
        self.board.set_square_to_piece('g5', Rook(colors.WHITE))
        self.board.set_square_to_piece('g1', Rook(colors.BLACK))
        self.board.set_square_to_piece('f2', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('b1')
        
        self.assertFalse(self.rules.is_checkmate(colors.WHITE, self.board), 'White can take with rook')
        
    def testWhiteCannotBlockKnightCheckmate(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('a5', Rook(colors.WHITE))
        self.board.set_square_to_piece('b3', Knight(colors.BLACK))
        self.board.set_square_to_piece('d3', Bishop(colors.BLACK))
        self.board.set_square_to_piece('e2', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_checkmate(colors.WHITE, self.board), 'White cannot move nor block')
        
    def testWhiteCanTakeKnightCheckmate(self):
        self.board.set_square_to_piece('a1', King(colors.WHITE))
        self.board.set_square_to_piece('b5', Rook(colors.WHITE))
        self.board.set_square_to_piece('b3', Knight(colors.BLACK))
        self.board.set_square_to_piece('d3', Bishop(colors.BLACK))
        self.board.set_square_to_piece('e2', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertTrue(self.rules.is_checkmate(colors.WHITE, self.board), 'White cannot move nor block')
        
    def testKingCanTakeOutOfCheckmate(self):
        self.board.set_square_to_piece('c1', King(colors.WHITE))
        self.board.set_square_to_piece('d1', Rook(colors.BLACK))
        self.board.set_square_to_piece('h2', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertFalse(self.rules.is_checkmate(colors.WHITE, self.board), 'White cannot move nor block')
        
    def testCannotBlockMultipleCheckingPieces(self):
        self.board.set_square_to_piece('c3', King(colors.WHITE))
        self.board.set_square_to_piece('b8', Rook(colors.WHITE))
        self.board.set_square_to_piece('g1', Rook(colors.WHITE))
        self.board.set_square_to_piece('a3', Rook(colors.BLACK))
        self.board.set_square_to_piece('h3', Rook(colors.BLACK))
        self.board.kings[colors.WHITE] = self.board.algebraic_to_coordinate_square('a1')
        
        self.assertFalse(self.rules.can_a_piece_block_or_take_check(colors.WHITE, self.board), 'White cannot block with either rook')
    
if __name__ == "__main__":
    unittest.main()