'''
Created on Jun 21, 2013

@author: nick
'''

from chesspye.utils import enum

colors = enum(WHITE=1, BLACK=-1)
piece_types = enum(PAWN=0, KNIGHT=1, BISHOP=2, ROOK=3, QUEEN=4, KING=5)
move_types = enum(MAX=0, EXACT=1)