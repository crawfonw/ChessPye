'''
Created on Jun 22, 2013

@author: nick
'''
import unittest

from chesspye.board.boards import Board, ClassicBoard
from chesspye.board.pieces import colors, Pawn, King, Queen, Knight, Bishop, Rook

class TestGenericBoardCreation(unittest.TestCase):

    def setUp(self):
        self.width = 12
        self.height = 15
        self.board = Board(self.width,self.height)

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

class TestClassicBoardCreation(unittest.TestCase):

    def setUp(self):
        self.board = ClassicBoard()

    def tearDown(self):
        pass
    
    def testBoardDoesCallSuperCorrectly(self):
        self.assertEqual(8, self.board.width, 'Board width %s != 8' % self.board.width)
        self.assertEqual(8, self.board.height, 'Board height %s != 8' % self.board.height)
        
    def testBoardDoesHaveCorrectNumberOfPieces(self):
        real_pieces_count = 0
        for piece in self.board.pieces.values():
            if piece is not None:
                real_pieces_count += 1
        self.assertEqual(32, real_pieces_count, 'Piece count is neq 32')
        
    def testBoardDoesHaveKingDictionarySetUpCorrectly(self):
        self.assertEqual(self.board.kings[colors.WHITE], (0,4), 'White king dict should be (0,4)')
        self.assertEqual(self.board.kings[colors.BLACK], (7,4), 'Black king dict should be (7,4)')
    
    def testBoardDoesHavePawnsInCorrectPosition(self):
        for i in range(self.board.width):
            if not isinstance(self.board.pieces[(1,i)], Pawn):
                self.fail('%s in %s is not of type Pawn' % (repr(self.board.pieces[(1,i)]), (1,i)))
            elif not isinstance(self.board.pieces[(6,i)], Pawn):
                self.fail('%s in %s is not of type Pawn' % (repr(self.board.pieces[(6,i)]), (6,i)))
            elif not self.board.pieces[(1,i)].color == colors.WHITE:
                self.fail('%s in not of color White' % (repr(self.board.pieces[(1,i)])))
            elif not self.board.pieces[(6,i)].color == colors.BLACK:
                self.fail('%s in not of color Black' % (repr(self.board.pieces[(6,i)])))
    
    def testBoardDoesHaveRooksInCorrectPosition(self):
        self.assertTrue(isinstance(self.board.pieces[(0,0)], Rook), '%s is not of type Rook')
        self.assertEqual(colors.WHITE, self.board.pieces[(0,0)].color, '%s is not of color WHITE' % repr(self.board.pieces[(0,0)]))
        self.assertTrue(isinstance(self.board.pieces[(0,7)], Rook), '%s is not of type Rook')
        self.assertEqual(colors.WHITE, self.board.pieces[(0,7)].color, '%s is not of color WHITE' % repr(self.board.pieces[(0,7)]))
        
        self.assertTrue(isinstance(self.board.pieces[(7,0)], Rook), '%s is not of type Rook')
        self.assertEqual(colors.BLACK, self.board.pieces[(7,0)].color, '%s is not of color BLACK' % repr(self.board.pieces[(7,0)]))
        self.assertTrue(isinstance(self.board.pieces[(7,7)], Rook), '%s is not of type Rook')
        self.assertEqual(colors.BLACK, self.board.pieces[(7,7)].color, '%s is not of color BLACK' % repr(self.board.pieces[(7,7)]))
    
    def testBoardDoesHaveKnightsInCorrectPosition(self):
        self.assertTrue(isinstance(self.board.pieces[(0,1)], Knight), '%s is not of type Knight')
        self.assertEqual(colors.WHITE, self.board.pieces[(0,1)].color, '%s is not of color WHITE' % repr(self.board.pieces[(0,1)]))
        self.assertTrue(isinstance(self.board.pieces[(0,6)], Knight), '%s is not of type Knight')
        self.assertEqual(colors.WHITE, self.board.pieces[(0,6)].color, '%s is not of color WHITE' % repr(self.board.pieces[(0,6)]))
        
        self.assertTrue(isinstance(self.board.pieces[(7,1)], Knight), '%s is not of type Knight')
        self.assertEqual(colors.BLACK, self.board.pieces[(7,1)].color, '%s is not of color BLACK' % repr(self.board.pieces[(7,1)]))
        self.assertTrue(isinstance(self.board.pieces[(7,6)], Knight), '%s is not of type Knight')
        self.assertEqual(colors.BLACK, self.board.pieces[(7,6)].color, '%s is not of color BLACK' % repr(self.board.pieces[(7,6)]))
    
    def testBoardDoesHaveBishopsInCorrectPosition(self):
        self.assertTrue(isinstance(self.board.pieces[(0,2)], Bishop), '%s is not of type Bishop')
        self.assertEqual(colors.WHITE, self.board.pieces[(0,2)].color, '%s is not of color WHITE' % repr(self.board.pieces[(0,2)]))
        self.assertTrue(isinstance(self.board.pieces[(0,5)], Bishop), '%s is not of type Bishop')
        self.assertEqual(colors.WHITE, self.board.pieces[(0,5)].color, '%s is not of color WHITE' % repr(self.board.pieces[(0,5)]))
        
        self.assertTrue(isinstance(self.board.pieces[(7,2)], Bishop), '%s is not of type Bishop')
        self.assertEqual(colors.BLACK, self.board.pieces[(7,2)].color, '%s is not of color BLACK' % repr(self.board.pieces[(7,2)]))
        self.assertTrue(isinstance(self.board.pieces[(7,5)], Bishop), '%s is not of type Bishop')
        self.assertEqual(colors.BLACK, self.board.pieces[(7,5)].color, '%s is not of color BLACK' % repr(self.board.pieces[(7,5)]))
    
    def testBoardDoesHaveKingsInCorrectPosition(self):
        self.assertTrue(isinstance(self.board.pieces[(0,4)], King), '%s is not of type King')
        self.assertEqual(colors.WHITE, self.board.pieces[(0,4)].color, '%s is not of color WHITE' % repr(self.board.pieces[(0,3)]))
        
        self.assertTrue(isinstance(self.board.pieces[(7,4)], King), '%s is not of type King')
        self.assertEqual(colors.BLACK, self.board.pieces[(7,4)].color, '%s is not of color BLACK' % repr(self.board.pieces[(7,3)]))
    
    def testBoardDoesHaveQueensInCorrectPosition(self):
        self.assertTrue(isinstance(self.board.pieces[(0,3)], Queen), '%s is not of type Queen')
        self.assertEqual(colors.WHITE, self.board.pieces[(0,3)].color, '%s is not of color WHITE' % repr(self.board.pieces[(0,4)]))
        
        self.assertTrue(isinstance(self.board.pieces[(7,3)], Queen), '%s is not of type Queen')
        self.assertEqual(colors.BLACK, self.board.pieces[(7,3)].color, '%s is not of color BLACK' % repr(self.board.pieces[(7,4)]))

class TestCoordinateToAlgebraicConversions(unittest.TestCase):
    
    def setUp(self):
        self.board = Board(8,8)

    def tearDown(self):
        pass
    
    def testConvertCoordinateToAlgebraicSquare(self):
        letters = ['a','b','c','d','e','f','g','h']
        for i in range(8):
            for j in range(8):
                alg = '%s%s' % (letters[i], j+1)
                conv = self.board.coordinate_to_algebraic_square((j,i))
                self.assertEqual(alg, conv, '%s should be %s' % (conv, alg))
    
    def testConvertAlgebraicToCoordinateSquare(self):
        letters = ['a','b','c','d','e','f','g','h']
        for i in range(len(letters)):
            for j in range(8):
                coords = (j,i)
                conv = self.board.algebraic_to_coordinate_square('%s%s' % (letters[i], j+1))
                self.assertEqual(conv, coords, '%s should be %s' % (conv, coords))
    
    def testConvertCoordinateToAlgebraicMoveOnly(self):
        self.board.pieces[(0,6)] = Knight(colors.WHITE)
        
        knight = self.board.get_coordinate_piece_tuple(0,6)
        f3 = self.board.get_coordinate_piece_tuple(2,5)
        
        correct_move = 'Nf3'
        converted_move = self.board.coordinate_to_algebraic_move(f3, knight)
        self.assertEqual(correct_move, converted_move, 'Move notation %s should be %s' % (converted_move, correct_move))
    
    def testConvertCoordinateToAlgebraicMoveOnlyPawn(self):
        self.skipTest('Not implemented')
    
    def testConvertCoordinateToAlgebraicWithCapture(self):
        self.board.pieces[(0,7)] = Rook(colors.WHITE)
        self.board.pieces[(3,7)] = Pawn(colors.BLACK)
        
        rook = self.board.get_coordinate_piece_tuple(0,7)
        pawn = self.board.get_coordinate_piece_tuple(3,7)
        
        correct_move = 'Rxh4'
        converted_move = self.board.coordinate_to_algebraic_move(pawn, rook)
        self.assertEqual(correct_move, converted_move, 'Move notation %s should be %s' % (converted_move, correct_move))
        
    def testConvertCoordinateToAlgebraicWithCapturePawn(self):
        self.skipTest('Not implemented')
    
    def testConvertCoordinateToAlgebraicWithAmbiguousMove(self):
        self.skipTest('Not implemented')
    
    def testConvertCoordinateToAlgebraicWithAmbiguousCapture(self):
        self.skipTest('Not implemented')
        
    def testConvertCoordinateToAlgebraicEnPassant(self):
        self.skipTest('Not implemented')
        
    def testConvertCoordinateToAlgebraicPawnPromotion(self):
        self.skipTest('Not implemented')
        
class TestBoardEqualityAndHashing(unittest.TestCase):
    
    def setUp(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.d = {}

    def tearDown(self):
        pass
    
    def testFullBoardEquality(self):
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
    def testFullAndEmptyBoardInequality(self):
        self.board2.clear_board()
        
        self.assertNotEqual(self.board1, self.board2, 'Boards are not set up the same')
        
    def testSameMemoryObjectSinglePiecesBoardEquality(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.board1.clear_board()
        self.board2.clear_board()
        
        white_rook = Rook(colors.WHITE)
        self.board1.set_square_to_piece('h1', white_rook)
        self.board2.set_square_to_piece('h1', white_rook)
        
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
    def testDifferentMemoryObjectSinglePiecesBoardEquality(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.board1.clear_board()
        self.board2.clear_board()
        
        white_rook1 = Rook(colors.WHITE)
        white_rook2 = Rook(colors.WHITE)
        self.board1.set_square_to_piece('h1', white_rook1)
        self.board2.set_square_to_piece('h1', white_rook2)
        
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
    def testSameMemoryObjectMultiplePiecesBoardEquality(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.board1.clear_board()
        self.board2.clear_board()
        
        white_rook = Rook(colors.WHITE)
        white_queen = Queen(colors.WHITE)
        black_pawn = Pawn(colors.BLACK)
        self.board1.set_square_to_piece('h1', white_rook)
        self.board1.set_square_to_piece('c3', white_queen)
        self.board1.set_square_to_piece('e7', black_pawn)
        self.board2.set_square_to_piece('h1', white_rook)
        self.board2.set_square_to_piece('c3', white_queen)
        self.board2.set_square_to_piece('e7', black_pawn)
        
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
    def testDifferentMemoryObjectMultiplePiecesBoardEquality(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.board1.clear_board()
        self.board2.clear_board()
        
        white_rook1 = Rook(colors.WHITE)
        white_rook2 = Rook(colors.WHITE)
        white_queen1 = Queen(colors.WHITE)
        white_queen2 = Queen(colors.WHITE)
        black_pawn1 = Pawn(colors.BLACK)
        black_pawn2 = Pawn(colors.BLACK)
        self.board1.set_square_to_piece('h1', white_rook1)
        self.board1.set_square_to_piece('c3', white_queen1)
        self.board1.set_square_to_piece('e7', black_pawn1)
        self.board2.set_square_to_piece('h1', white_rook2)
        self.board2.set_square_to_piece('c3', white_queen2)
        self.board2.set_square_to_piece('e7', black_pawn2)
        
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
    def testSameMemoryObjectMultiplePiecesBoardEqualityModify(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.board1.clear_board()
        self.board2.clear_board()
        
        white_rook = Rook(colors.WHITE)
        white_queen = Queen(colors.WHITE)
        black_pawn = Pawn(colors.BLACK)
        self.board1.set_square_to_piece('h1', white_rook)
        self.board1.set_square_to_piece('c3', white_queen)
        self.board2.set_square_to_piece('h1', white_rook)
        self.board2.set_square_to_piece('c3', white_queen)
        
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
        self.board1.set_square_to_piece('e7', black_pawn)
        self.board2.set_square_to_piece('e7', black_pawn)
        
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
    def testDifferentMemoryObjectMultiplePiecesBoardEqualityModify(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.board1.clear_board()
        self.board2.clear_board()
        
        white_rook1 = Rook(colors.WHITE)
        white_rook2 = Rook(colors.WHITE)
        white_queen1 = Queen(colors.WHITE)
        white_queen2 = Queen(colors.WHITE)
        black_pawn1 = Pawn(colors.BLACK)
        black_pawn2 = Pawn(colors.BLACK)
        self.board1.set_square_to_piece('h1', white_rook1)
        self.board1.set_square_to_piece('c3', white_queen1)
        self.board2.set_square_to_piece('h1', white_rook2)
        self.board2.set_square_to_piece('c3', white_queen2)
        
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
        self.board1.set_square_to_piece('e7', black_pawn1)
        self.board2.set_square_to_piece('e7', black_pawn2)
        
        self.assertEqual(self.board1, self.board2, 'Boards are set up the same')
        
    def testDifferentSizedBoardsAreNotEqual(self):
        self.board1 = Board(8,8)
        self.board2 = Board(9,9)
        
        self.assertNotEqual(self.board1, self.board2, 'Boards are different dimensions')
        
    def testDifferentWidthBoardsAreNotEqual(self):
        self.board1 = Board(8,8)
        self.board2 = Board(9,8)
        
        self.assertNotEqual(self.board1, self.board2, 'Boards widths are different size')
        
    def testDifferentHeightBoardsAreNotEqual(self):
        self.board1 = Board(8,8)
        self.board2 = Board(8,9)
        
        self.assertNotEqual(self.board1, self.board2, 'Boards heights are different size')
        
    def testDictWithEqualBoardsHasOneEntry(self):
        self.d[self.board1] = 1
        self.d[self.board2] = 2
        
        self.assertEqual(len(self.d), 1, 'Dict should only have a single entry')
        self.assertEqual(self.d[self.board1], 2, 'Entry for board1 should be same as entry for board2 (2)')
        self.assertEqual(self.d[self.board2], 2, 'Entry for board2 should be same as entry for board1 (2)')
        
    def testDictWithNotEqualBoardsHasMultipleEntries(self):
        self.board1.clear_board()
        self.d[self.board1] = 1
        self.d[self.board2] = 2
        
        self.assertEqual(len(self.d), 2, 'Dict should only have two entries')
        self.assertEqual(self.d[self.board1], 1, 'Entry for board1 should be 1')
        self.assertEqual(self.d[self.board2], 2, 'Entry for board2 should be 2')
    
    def testSameMemoryObjectSinglePiecesBoardDictEquality(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.board1.clear_board()
        self.board2.clear_board()
        
        white_rook = Rook(colors.WHITE)
        self.board1.set_square_to_piece('h1', white_rook)
        self.board2.set_square_to_piece('h1', white_rook)
        
        self.d[self.board1] = 1
        self.d[self.board2] = 2
        
        self.assertEqual(len(self.d), 1, 'Dict should only have a single entry')
        self.assertEqual(self.d[self.board1], 2, 'Entry for board1 should be same as entry for board2 (2)')
        self.assertEqual(self.d[self.board2], 2, 'Entry for board2 should be same as entry for board1 (2)')
        
    def testDifferentMemoryObjectSinglePiecesBoardDictEquality(self):
        self.board1 = ClassicBoard()
        self.board2 = ClassicBoard()
        self.board1.clear_board()
        self.board2.clear_board()
        
        white_rook1 = Rook(colors.WHITE)
        white_rook2 = Rook(colors.WHITE)
        self.board1.set_square_to_piece('h1', white_rook1)
        self.board2.set_square_to_piece('h1', white_rook2)
        
        self.d[self.board1] = 1
        self.d[self.board2] = 2
        
        self.assertEqual(len(self.d), 1, 'Dict should only have a single entry')
        self.assertEqual(self.d[self.board1], 2, 'Entry for board1 should be same as entry for board2 (2)')
        self.assertEqual(self.d[self.board2], 2, 'Entry for board2 should be same as entry for board1 (2)')
        
    def testDictWithDifferentSizedBoardsHasMultipleEntries(self):
        self.board1 = Board(8,8)
        self.board2 = Board(9,9)
        
        self.d[self.board1] = 1
        self.d[self.board2] = 2
        
        self.assertEqual(len(self.d), 2, 'Dict should only have a single entry')
        self.assertEqual(self.d[self.board1], 1, 'Entry for board1 should be 1')
        self.assertEqual(self.d[self.board2], 2, 'Entry for board2 should be 2')
        
    def testDictDifferentWidthBoardsHasMultipleEntries(self):
        self.board1 = Board(8,8)
        self.board2 = Board(9,8)
        
        self.d[self.board1] = 1
        self.d[self.board2] = 2
        
        self.assertEqual(len(self.d), 2, 'Dict should only have a single entry')
        self.assertEqual(self.d[self.board1], 1, 'Entry for board1 should be 1')
        self.assertEqual(self.d[self.board2], 2, 'Entry for board2 should be 2')
        
    def testDifferentHeightBoardsHasMultipleEntries(self):
        self.board1 = Board(8,8)
        self.board2 = Board(8,9)
        
        self.d[self.board1] = 1
        self.d[self.board2] = 2
        
        self.assertEqual(len(self.d), 2, 'Dict should only have a single entry')
        self.assertEqual(self.d[self.board1], 1, 'Entry for board1 should be 1')
        self.assertEqual(self.d[self.board2], 2, 'Entry for board2 should be 2')

if __name__ == "__main__":
    unittest.main()