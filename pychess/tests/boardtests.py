'''
Created on Jun 22, 2013

@author: nick
'''
import unittest

from pychess.boards import Board, ClassicBoard
from pychess.pieces import colors, Pawn, King, Queen, Knight, Bishop, Rook

class TestBoardCreation(unittest.TestCase):

    def setUp(self):
        self.width = 12
        self.height = 15
        self.board = Board(self.width,self.height)
        self.cboard = ClassicBoard()

    def tearDown(self):
        pass
    
    def testBoardDoesHaveCorrectWidth(self):
        self.assertEqual(self.width, self.board.width, 'Board width %s != %s' % (self.board.width, self.width))
    
    def testBoardDoesHaveCorrectHeight(self):
        self.assertEqual(self.height, self.board.height, 'Board height %s != %s' % (self.board.height, self.height))
    
    def testBoardDoesHaveAllNoneTypeObjectsInSquares(self):
        for piece in self.board.pieces.values():
            if piece is not None:
                self.fail('Pieces %s is not of NoneType' % repr(piece))

    def testBoardDoesCallSuperCorrectly(self):
        self.assertEqual(8, self.cboard.width, 'Board width %s != 8' % self.cboard.width)
        self.assertEqual(8, self.cboard.height, 'Board height %s != 8' % self.cboard.height)
        
    def testBoardDoesHaveCorrectNumberOfPieces(self):
        real_pieces_count = 0
        for piece in self.cboard.pieces.values():
            if piece is not None:
                real_pieces_count += 1
        self.assertEqual(32, real_pieces_count, 'Piece count is neq 32')
    
    def testBoardDoesHavePawnsInCorrectPosition(self):
        for i in range(self.cboard.width):
            if not isinstance(self.cboard.pieces[(1,i)], Pawn):
                self.fail('%s in %s is not of type Pawn' % (repr(self.cboard.pieces[(1,i)]), (1,i)))
            elif not isinstance(self.cboard.pieces[(6,i)], Pawn):
                self.fail('%s in %s is not of type Pawn' % (repr(self.cboard.pieces[(6,i)]), (6,i)))
            elif not self.cboard.pieces[(1,i)].color == colors.WHITE:
                self.fail('%s in not of color White' % (repr(self.cboard.pieces[(1,i)])))
            elif not self.cboard.pieces[(6,i)].color == colors.BLACK:
                self.fail('%s in not of color Black' % (repr(self.cboard.pieces[(6,i)])))
    
    def testBoardDoesHaveRooksInCorrectPosition(self):
        self.assertTrue(isinstance(self.cboard.pieces[(0,0)], Rook), '%s is not of type Rook')
        self.assertEqual(colors.WHITE, self.cboard.pieces[(0,0)].color, '%s is not of color WHITE' % repr(self.cboard.pieces[(0,0)]))
        self.assertTrue(isinstance(self.cboard.pieces[(0,7)], Rook), '%s is not of type Rook')
        self.assertEqual(colors.WHITE, self.cboard.pieces[(0,7)].color, '%s is not of color WHITE' % repr(self.cboard.pieces[(0,7)]))
        
        self.assertTrue(isinstance(self.cboard.pieces[(7,0)], Rook), '%s is not of type Rook')
        self.assertEqual(colors.BLACK, self.cboard.pieces[(7,0)].color, '%s is not of color BLACK' % repr(self.cboard.pieces[(7,0)]))
        self.assertTrue(isinstance(self.cboard.pieces[(7,7)], Rook), '%s is not of type Rook')
        self.assertEqual(colors.BLACK, self.cboard.pieces[(7,7)].color, '%s is not of color BLACK' % repr(self.cboard.pieces[(7,7)]))
    
    def testBoardDoesHaveKnightsInCorrectPosition(self):
        self.assertTrue(isinstance(self.cboard.pieces[(0,1)], Knight), '%s is not of type Knight')
        self.assertEqual(colors.WHITE, self.cboard.pieces[(0,1)].color, '%s is not of color WHITE' % repr(self.cboard.pieces[(0,1)]))
        self.assertTrue(isinstance(self.cboard.pieces[(0,6)], Knight), '%s is not of type Knight')
        self.assertEqual(colors.WHITE, self.cboard.pieces[(0,6)].color, '%s is not of color WHITE' % repr(self.cboard.pieces[(0,6)]))
        
        self.assertTrue(isinstance(self.cboard.pieces[(7,1)], Knight), '%s is not of type Knight')
        self.assertEqual(colors.BLACK, self.cboard.pieces[(7,1)].color, '%s is not of color BLACK' % repr(self.cboard.pieces[(7,1)]))
        self.assertTrue(isinstance(self.cboard.pieces[(7,6)], Knight), '%s is not of type Knight')
        self.assertEqual(colors.BLACK, self.cboard.pieces[(7,6)].color, '%s is not of color BLACK' % repr(self.cboard.pieces[(7,6)]))
    
    def testBoardDoesHaveBishopsInCorrectPosition(self):
        self.assertTrue(isinstance(self.cboard.pieces[(0,2)], Bishop), '%s is not of type Bishop')
        self.assertEqual(colors.WHITE, self.cboard.pieces[(0,2)].color, '%s is not of color WHITE' % repr(self.cboard.pieces[(0,2)]))
        self.assertTrue(isinstance(self.cboard.pieces[(0,5)], Bishop), '%s is not of type Bishop')
        self.assertEqual(colors.WHITE, self.cboard.pieces[(0,5)].color, '%s is not of color WHITE' % repr(self.cboard.pieces[(0,5)]))
        
        self.assertTrue(isinstance(self.cboard.pieces[(7,2)], Bishop), '%s is not of type Bishop')
        self.assertEqual(colors.BLACK, self.cboard.pieces[(7,2)].color, '%s is not of color BLACK' % repr(self.cboard.pieces[(7,2)]))
        self.assertTrue(isinstance(self.cboard.pieces[(7,5)], Bishop), '%s is not of type Bishop')
        self.assertEqual(colors.BLACK, self.cboard.pieces[(7,5)].color, '%s is not of color BLACK' % repr(self.cboard.pieces[(7,5)]))
    
    def testBoardDoesHaveKingsInCorrectPosition(self):
        self.assertTrue(isinstance(self.cboard.pieces[(0,3)], King), '%s is not of type King')
        self.assertEqual(colors.WHITE, self.cboard.pieces[(0,3)].color, '%s is not of color WHITE' % repr(self.cboard.pieces[(0,3)]))
        
        self.assertTrue(isinstance(self.cboard.pieces[(7,3)], King), '%s is not of type King')
        self.assertEqual(colors.BLACK, self.cboard.pieces[(7,3)].color, '%s is not of color BLACK' % repr(self.cboard.pieces[(7,3)]))
    
    def testBoardDoesHaveQueensInCorrectPosition(self):
        self.assertTrue(isinstance(self.cboard.pieces[(0,4)], Queen), '%s is not of type Queen')
        self.assertEqual(colors.WHITE, self.cboard.pieces[(0,4)].color, '%s is not of color WHITE' % repr(self.cboard.pieces[(0,4)]))
        
        self.assertTrue(isinstance(self.cboard.pieces[(7,4)], Queen), '%s is not of type Queen')
        self.assertEqual(colors.BLACK, self.cboard.pieces[(7,4)].color, '%s is not of color BLACK' % repr(self.cboard.pieces[(7,4)]))

class TestCoordinateToAlgebraicConversions(unittest.TestCase):
    
    def setUp(self):
        self.board = Board(8,8)

    def tearDown(self):
        pass
    
    def testConvertCoordinateToAlgebraicMoveOnly(self):
        self.board.pieces[(0,6)] = Knight(colors.WHITE)
        
        knight = self.board.get_coordinate_piece_tuple(0,6)
        f3 = self.board.get_coordinate_piece_tuple(2,5)
        
        correct_move = 'Nf3'
        converted_move = self.board.coordinate_to_algebraic(f3, knight)
        self.assertEqual(correct_move, converted_move, 'Move notation %s should be %s' % (converted_move, correct_move))
    
    def testConvertCoordinateToAlgebraicMoveOnlyPawn(self):
        self.fail('Not implemented')
    
    def testConvertCoordinateToAlgebraicWithCapture(self):
        self.board.pieces[(0,7)] = Rook(colors.WHITE)
        self.board.pieces[(3,7)] = Pawn(colors.BLACK)
        
        rook = self.board.get_coordinate_piece_tuple(0,7)
        pawn = self.board.get_coordinate_piece_tuple(3,7)
        
        correct_move = 'Rxh4'
        converted_move = self.board.coordinate_to_algebraic(pawn, rook)
        self.assertEqual(correct_move, converted_move, 'Move notation %s should be %s' % (converted_move, correct_move))
        
    def testConvertCoordinateToAlgebraicWithCapturePawn(self):
        self.fail('Not implemented')
    
    def testConvertCoordinateToAlgebraicWithAmbiguousMove(self):
        self.fail('Not implemented')
    
    def testConvertCoordinateToAlgebraicWithAmbiguousCapture(self):
        self.fail('Not implemented')
        
    def testConvertCoordinateToAlgebraicEnPassant(self):
        self.fail('Not implemented')
        
    def testConvertCoordinateToAlgebraicPawnPromotion(self):
        self.fail('Not implemented') 

if __name__ == "__main__":
    unittest.main()