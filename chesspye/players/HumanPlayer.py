'''
Created on Jun 20, 2013

@author: nick
'''

from Enums import player_types
from Player import Player
        
class HumanPlayer(Player):
    
    def __init__(self, name, color):
        super(HumanPlayer, self).__init__(name, player_types.HUMAN, color)