'''
Created on Jun 21, 2013

@author: nick
'''

from chesspye.pieces import colors
from chesspye.utils import enum, scalar_mult_tuple

class ChessPiece(object):
    
    def __init__(self, long_name, color, piece_type, value, utf_code_white, algebraic, times_moved, move_type, can_jump=False):
        self.long_name = long_name
        self.color = color
        self.piece_type = piece_type
        self.value = value
        self.utf_code_white = utf_code_white
        self.algebraic = algebraic
        self.times_moved = times_moved
        self.move_type = move_type
        self.can_jump = can_jump

    def __unicode__(self):
        if self.color == colors.WHITE:
            return unichr(self.utf_code_white)
        elif self.color == colors.BLACK:
            return unichr(self.utf_code_white + 6)
    
    def __str__(self):
        #temp
        ret = self.algebraic
        if self.color == colors.BLACK:
            ret = ret.lower()
        return ret
    
    def __repr__(self):
        return '%s(long_name=%s, color=%s, piece_type=%s, value=%s, utf_code_white=%s, algebraic=%s, times_moved=%s)' \
            % (self.__class__.__name__, self.long_name, self.color, self.piece_type, \
               self.value, self.utf_code_white, self.algebraic, self.times_moved)
    
    #These are needed to hash the boards for easy three fold repetition detection
    #I don't particularly like this, but in terms of hashing for repetition detection it's all we need to check
    def __hash__(self):
        return hash(self.piece_type)
    
    def __eq__(self, o):
        if isinstance(o, ChessPiece):
            return self.piece_type == o.piece_type
        else:
            return False
    
    def move_patterns(self):
        '''
            Returns a list of tuples with xy modifier coordinates of how
            this piece moves.
        '''
        raise NotImplementedError()
    
    def attack_patterns(self):
        raise NotImplementedError()
    
    def all_patterns(self):
        return list(set(self.move_patterns()).union(set(self.attack_patterns())))
    
    def has_moved(self):
        return self.times_moved > 0