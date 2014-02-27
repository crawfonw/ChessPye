'''
Created on Jun 20, 2013

@author: nick
'''

from chesspye.utils import enum

player_types = enum(HUMAN=0, AI=1)

class Player(object):
    
    def __init__(self, type, color):
        self.type = type
        self.color = color
        
class HumanPlayer(Player):
    
    def __init__(self, color):
        super(HumanPlayer, self).__init__(player_types.HUMAN, color)