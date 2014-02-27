'''
Created on Feb 22, 2014

@author: Nick Crawford

Note on the move_rules dict:
    Each rule method must consume (from_sq, to_sq, move_vector, piece, board):
        piece - instance of a Piece
        from_sq, to_sq - each a tuple of coordinates of starting and ending pos
        move_vector - computed via from_sq and to_sq in main move handling method
        board - the current board state of the game
        move_stack - Stack obj containing all the previous moves
    
    If more rules are added (i.e. for variants) they must be in the extended
    rules class if you want them to interact with game_variables (duh)
'''

class Rules(object):
    
    def __init__(self):
        self.move_rules_and_actions = {}
        self.game_variables = {}
        
    def register_move_rule_handler_pair(self, rule, handler):
        self.move_rules_and_actions[rule] = handler
            
    def register_game_variable(self, name, val):
        self.game_variables[name] = val