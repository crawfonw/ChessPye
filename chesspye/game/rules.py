'''
Created on Feb 22, 2014

@author: Nick Crawford

Note on the move_rules dict:
    Each rule method must consume (from_sq, to_sq, move_vector, piece, board, move_stack):
        piece - instance of a Piece
        from_sq, to_sq - each a tuple of coordinates of starting and ending pos
        move_vector - computed via from_sq and to_sq in main move handling method
        board - the current board state of the game
        move_stack - Stack obj containing all the previous moves
    
    If more rules are added (i.e. for variants) they must be in the extended
    rules class if you want them to interact with game_variables (duh)
'''

from chesspye.board.pieces import colors, move_types, piece_types
from chesspye.utils import Vec2d

from math import copysign

class Rules(object):
    
    def __init__(self):
        self.move_rules = {} #These are all checked every move
        self.game_variables = {}
        
    def register_move_rule(self, f, name=None):
        if name is None:
            self.move_rules[f.__name__] = f
        else:
            self.move_rules[name] = f
            
    def register_game_variable(self, name, val):
        self.game_variables[name] = val

class VanillaRules(Rules):

    def __init__(self):
        super(VanillaRules, self).__init__()
        self.register_game_variable('white_can_kingside_castle', True)
        self.register_game_variable('white_can_queenside_castle', True)
        self.register_game_variable('black_can_kingside_castle', True)
        self.register_game_variable('black_can_queenside_castle', True)
        self.register_game_variable('fifty_move_counter', 0)
        
        self.register_move_rule(self.handle_en_passante, 'en_passante')
        self.register_move_rule(self.handle_castle, 'castle')
        
        
    def move_piece(self, from_sq, to_sq, board, move_stack=None): #move_stack=None for test methods (aka laziness)
        if type(from_sq) == type(to_sq):
            if type(from_sq) == tuple:
                return self.move_piece_coordinate(from_sq, to_sq, board, move_stack)
            elif type(from_sq) == str:
                return self.move_piece_algebraic(from_sq, to_sq, board, move_stack)
            else:
                raise TypeError("Invalid square specification data type %s" % type(from_sq))
        else:
            raise TypeError("from_sq and to_sq datatypes must match! (Inputs were %s and %s.)" % (type(from_sq), type(to_sq)))
    
    def move_piece_algebraic(self, from_sq, to_sq, board, move_stack):
        #i.e. d1-d4 not Qd4
        return self.move_piece_coordinate(board.algebraic_to_coordinate_square(from_sq), \
                          board.algebraic_to_coordinate_square(to_sq), board, move_stack)

    def move_piece_coordinate(self, from_sq, to_sq, board, move_stack):
        if from_sq == to_sq:
            return False
        if not board.square_is_on_board(from_sq):
            return False
        piece = board.pieces[from_sq]
        if piece is not None:
            move_vector = Vec2d(to_sq) - Vec2d(from_sq)
            
            for name, rule in self.move_rules.items():
                rule_applied = rule(from_sq, to_sq, move_vector, piece, board, move_stack) 
                if rule_applied is not None:
                    return rule_applied
                
            if self.piece_can_move_from_to(piece, from_sq, to_sq, board):
                board.pieces[from_sq] = None
                board.pieces[to_sq] = piece
                
                if piece.color == colors.WHITE:
                    if piece.piece_type == piece_types.KING:
                        self.game_variables['white_can_kingside_castle'] = False
                        self.game_variables['white_can_queenside_castle'] = False
                    #Hard-coded
                    #TODO: Un-hardcode rook locations for support for possible variants 
                    elif piece.piece_type == piece_types.ROOK:
                        if not piece.has_moved():
                            if from_sq == (0,7):
                                self.game_variables['white_can_kingside_castle'] = False
                            elif from_sq == (0,0):
                                self.game_variables['white_can_queenside_castle'] = False
                elif piece.color == colors.BLACK:
                    if piece.piece_type == piece_types.KING:
                        self.game_variables['black_can_kingside_castle'] = False
                        self.game_variables['black_can_queenside_castle'] = False
                    elif piece.piece_type == piece_types.ROOK:
                        if not piece.has_moved():
                            if from_sq == (7,7):
                                self.game_variables['black_can_kingside_castle'] = False
                            elif from_sq == (7,0):
                                self.game_variables['black_can_queenside_castle'] = False
                
                piece.times_moved += 1
                return True
            
        return False
    
    def piece_can_move_from_to(self, piece, from_sq, to_sq, board):
        pattern_types = None
        to_sq_piece = board.pieces[to_sq]
        if to_sq_piece is not None:
            if piece.color == to_sq_piece.color:
                return False
            else:
                pattern_types = piece.attack_patterns()
        else:
            pattern_types = piece.move_patterns()
        
        if piece.move_type == move_types.EXACT:
            #The following logic might not work for weird moving piece_types
            #(i.e. Knight) if they cannot jump
            #TODO: verify/fix this
            for move in pattern_types:
                if Vec2d(move) + Vec2d(from_sq) == Vec2d(to_sq):
                    if piece.can_jump:
                        return True
                    else:
                        #This piece can move here assuming it is unblocked
                        #Now find the straight-line path and make sure nothing is blocking
                        f = lambda x : int(copysign(1,x)) if x != 0 else 0
                        unit_move = Vec2d(f(move[0]), f(move[1])) #unit vector in direction of move
                        curr_sq = Vec2d(from_sq) + unit_move
                        while tuple(curr_sq) != to_sq:
                            if not board.square_is_on_board(tuple(curr_sq)):
                                return False
                            if board.pieces[tuple(curr_sq)] is not None:
                                return False
                            curr_sq += unit_move
                        return True
        elif piece.move_type == move_types.MAX:
            for move in pattern_types:
                dir_vec = Vec2d(move) #a unit vector
                move_vec = Vec2d(to_sq[0] - from_sq[0], to_sq[1] - from_sq[1])
                #This direction is a valid movement if vectorized coordinates 
                #have an angle of zero between them and point the same direction
                #(i.e. scalar multiples of one another)
                if dir_vec.get_angle_between(move_vec) == 0:
                    curr_sq = Vec2d(from_sq) + dir_vec
                    while tuple(curr_sq) != to_sq:
                        if not board.square_is_on_board(tuple(curr_sq)):
                            return False
                        if board.pieces[tuple(curr_sq)] is not None and not piece.can_jump:
                            return False
                        curr_sq += dir_vec
                    return True
    
    def handle_en_passante(self, from_sq, to_sq, move_vector, piece, board, move_stack):
        if piece.piece_type == piece_types.PAWN and tuple(move_vector) in piece.attack_patterns():
            other = board.pieces[tuple(Vec2d(from_sq) + Vec2d(0, move_vector.y))]
            if other is not None and other.piece_type == piece_types.PAWN and other.color != piece.color:
                last_move = move_stack.peek()
                if other is last_move[0] and other.times_moved == 1: #Want the same exact piece (in memory)
                    board.pieces[from_sq] = None
                    board.pieces[to_sq] = piece
                    piece.times_moved += 1
                    return True
                return False
            
    def handle_castle(self, from_sq, to_sq, move_vector, piece, board, move_stack):
        if piece.piece_type == piece_types.KING and move_vector.get_length() == 2:
            if piece.has_moved():
                return False
            if self.piece_can_move_from_to(piece, from_sq, to_sq, board):
                if piece.color == colors.WHITE:
                    if self.game_variables['white_can_kingside_castle'] and move_vector == Vec2d(0,2):
                            rook_loc = tuple(Vec2d(to_sq) + Vec2d(0,1))
                            rook_dest = tuple(Vec2d(to_sq) + Vec2d(0,-1))
                    elif self.game_variables['white_can_queenside_castle'] and move_vector == Vec2d(0,-2):
                        rook_loc = tuple(Vec2d(to_sq) + Vec2d(0,-2))
                        rook_dest = tuple(Vec2d(to_sq) + Vec2d(0,1))
                    else:
                        return False
                elif piece.color == colors.BLACK:
                    if self.game_variables['black_can_kingside_castle'] and move_vector == Vec2d(0,2):
                        rook_loc = tuple(Vec2d(to_sq) + Vec2d(0,1))
                        rook_dest = tuple(Vec2d(to_sq) + Vec2d(0,-1))
                    elif self.game_variables['black_can_queenside_castle'] and move_vector == Vec2d(0,-2):
                        rook_loc = tuple(Vec2d(to_sq) + Vec2d(0,-2))
                        rook_dest = tuple(Vec2d(to_sq) + Vec2d(0,1))
                    else:
                        return False
                
                if not board.square_is_on_board(rook_loc):
                    return False
                rook = board.pieces[rook_loc]
                if rook is None or rook.piece_type != piece_types.ROOK or rook.has_moved():
                    return False
                
                board.pieces[from_sq] = None
                board.pieces[to_sq] = piece
                piece.times_moved += 1
                
                board.pieces[rook_loc] = None
                board.pieces[rook_dest] = rook
                rook.times_moved += 1
                
                if piece.color == colors.WHITE:
                    self.game_variables['white_can_kingside_castle'] = False
                    self.game_variables['white_can_queenside_castle'] = False
                elif piece.color == colors.BLACK:
                    self.game_variables['black_can_kingside_castle'] = False
                    self.game_variables['black_can_queenside_castle'] = False
                return True