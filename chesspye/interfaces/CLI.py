'''
Created on Feb 27, 2014

@author: Nick Crawford
'''

from chesspye.interfaces import Interface
from chesspye.players.players import player_types

class CLI(Interface):
    
    def __init__(self):
        super(CLI, self).__init__()
        
    def display_message(self, message):
        print message
        
    def draw_board_update(self, board):
        print str(board)
        
    def offer_move(self, player):
        if player.type == player_types.AI:
            return player.move()
        elif player.type == player_types.HUMAN:
            print '%s to move.' % player.name
            return raw_input('Enter move ([from]-[to]):\n')
        else:
            raise TypeError()