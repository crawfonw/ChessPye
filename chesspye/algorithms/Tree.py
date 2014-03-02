'''
Created on Mar 2, 2014

@author: Nick Crawford
'''

from copy import deepcopy

class BoardTreeNode(object):
    
    def __init__(self, board, rules, move):
        self.board = board
        self.rules = rules
        self.move = move #what move got us here
    
    def __len__(self):
        size = 1
        print len(self.children)
        for child in self.children:
            size += len(child)
        return size

    def generate_children(self, color):
        children = []
        color_pieces = self.board.get_pieces_for_color(color)
        for from_sq, piece in color_pieces:
            vectors = piece.all_patterns()
            for move_vector in vectors:
                possible_moves = self.rules.generate_all_valid_target_squares_for_vector(from_sq, piece, move_vector, self.board)
                for move in possible_moves:
                    test_board = deepcopy(self.board)
                    if self.rules.is_valid_move(from_sq, move, test_board):
                        self.rules.move_piece(from_sq, move, test_board)
                        children.append(BoardTreeNode(test_board, self.rules, (from_sq, move)))
        return children
            