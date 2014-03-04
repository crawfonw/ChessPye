'''
Created on Mar 2, 2014

@author: Nick Crawford
'''

from copy import deepcopy
from pieces import piece_types, colors, vanilla_type_to_obj

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

    #temporary
    def handle_pawn_promotion(self, choice):
        last_move = self.board.moves.peek()
        if last_move is not None:
            if last_move[0].piece_type == piece_types.PAWN:
                if last_move[0].color == colors.WHITE:
                    if last_move[2][0] == self.board.height - 1:
                        self.board.pieces[last_move[2]] = vanilla_type_to_obj(choice, last_move[0].color)
                elif last_move[0].color == colors.BLACK:
                    if last_move[2][0] == 0:
                        self.board.pieces[last_move[2]] = vanilla_type_to_obj(choice, last_move[0].color)
        
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
                        self.handle_pawn_promotion(piece_types.QUEEN) #just assume it's a queen for now
                        children.append(BoardTreeNode(test_board, test_rules, test_pos, (from_sq, move)))
        return children