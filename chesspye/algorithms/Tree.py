'''
Created on Mar 2, 2014

@author: Nick Crawford
'''

from copy import deepcopy

class BoardTreeNode(object):
    
    def __init__(self, board, rules, positions, move):
        self.board = board
        self.rules = rules
        self.positions = positions
        self.move = move #what move got us here
    
    def __len__(self):
        size = 1
        print len(self.children)
        for child in self.children:
            size += len(child)
        return size
    
    def is_terminal(self):
        return self.rules.is_game_over(1, self.board, self.positions)

    def generate_children(self, color):
        children = []
        color_pieces = self.board.get_pieces_for_color(color)
        for from_sq, piece in color_pieces:
            vectors = piece.all_patterns()
            for move_vector in vectors:
                possible_moves = self.rules.generate_all_valid_target_squares_for_vector(from_sq, piece, move_vector, self.board)
                for move in possible_moves:
                    test_board = deepcopy(self.board) #shouldn't matter but just in case something changes
                    test_rules = deepcopy(self.rules)
                    test_pos = deepcopy(self.positions)
                    if self.rules.move_piece(from_sq, move, test_board):
                        try:
                            test_pos[test_board] += 1
                        except:
                            test_pos[test_board] = 1
                        children.append(BoardTreeNode(test_board, test_rules, test_pos, (from_sq, move)))
        return children