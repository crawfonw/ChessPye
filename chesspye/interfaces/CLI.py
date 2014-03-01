'''
Created on Feb 27, 2014

@author: Nick Crawford
'''

from interfaces import Interface
from players import player_types

class CLI(Interface):
    
    def __init__(self):
        super(CLI, self).__init__()
        
    def setup(self, game_instance):
        pass
        
    def display_message(self, message):
        print message
        
    def draw_board_update(self, board):
        print str(board)
        
    def offer_move_to_human(self, player):
        if player.type == player_types.HUMAN:
            print '%s to move.' % player.name
            return raw_input('Enter move ([from]-[to]):\n')
        else:
            raise TypeError()