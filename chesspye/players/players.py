'''
Created on Jun 20, 2013

@author: nick
'''

from chesspye.utils import enum

player_types = enum(HUMAN=0, AI=1)

class Player(object):
    
    def __init__(self, name, type, color):
        self.name = name
        self.type = type
        self.color = color
        
class HumanPlayer(Player):
    
    def __init__(self, name, color):
        super(HumanPlayer, self).__init__(name, player_types.HUMAN, color)