'''
Created on Feb 27, 2014

@author: Nick Crawford
'''

from interfaces import Interface
from players import player_types

class CLI(Interface):
    
    def __init__(self, game_instance):
        super(CLI, self).__init__(game_instance)
        
    def start(self):
        self.draw_board_update()
        while not self.game.has_winner():
            move = self.offer_move(self.game.active_player())
            response = self.game.play_turn(move)
            if response == 'promote':
                choice = self.offer_promote()
                self.game.handle_pawn_promotion(choice)
            elif response == 'invalid':
                self.display_message('Invalid move!')
            self.draw_board_update()
        
    def display_message(self, message):
        print message
        
    def draw_board_update(self):
        print str(self.game.board)
        
    def offer_move(self, player):
        if player.type == player_types.HUMAN:
            print '%s to move.' % player.name
            move = ''
            while len(move.split('-')) != 2:
                move = raw_input('Enter move ([from]-[to]):\n')
            return move.split('-')
        elif player.type == player_types.AI:
            return player.move()
        
    def offer_promote(self, player):
        choice = ''
        if player.type == player_types.HUMAN:
            while choice.upper() not in ('B', 'N', 'R', 'Q'):
                choice = raw_input('Promote to B, N, R, or Q:\n')
        elif player.type == player_types.AI:
            choice = player.choose_promotion()
        return choice
            