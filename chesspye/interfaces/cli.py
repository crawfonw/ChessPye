'''
Created on Feb 27, 2014

@author: Nick Crawford
'''

from chesspye.interfaces.interface import Interface
from chesspye.players.players import player_types

class CLI(Interface):
    
    def __init__(self):
        super(CLI, self).__init__()
        
    def draw_update(self, board):
        print str(board)
        
    def offer_move(self, player):
        if player.type == player_types.AI:
            return player.move()
        elif player.type == player_types.HUMAN:
            return raw_input('Enter move ([from]-[to]):')
        else:
            raise TypeError()