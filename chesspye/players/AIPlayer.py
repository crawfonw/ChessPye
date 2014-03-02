'''
Created on Jun 20, 2013

@author: nick
'''

from Enums import player_types
from Player import Player
        
class AIPlayer(Player):
    
    def __init__(self, name, color):
        super(AIPlayer, self).__init__(name, player_types.AI, color)
        self.game = None
        
    def register_game(self, game):
        self.game = game
        
    def move(self):
        raise NotImplementedError()
    
    def choose_promotion(self):
        raise NotImplementedError()