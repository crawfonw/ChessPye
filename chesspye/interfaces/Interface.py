'''
Created on Feb 27, 2014

@author: Nick Crawford
'''

class Interface(object):
    
    def __init__(self, game_instance):
        self.game = game_instance
        
    def start(self):
        raise NotImplementedError()
    
    def offer_move(self, player):
        raise NotImplementedError()
    
    def draw_board_update(self):
        raise NotImplementedError()
    
    def display_message(self, message):
        raise NotImplementedError()
    
    def display_alert(self, message):
        raise NotImplementedError()
    
    def setup(self, game_instance):
        raise NotImplementedError()