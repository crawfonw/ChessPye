'''
Created on Jun 20, 2013

@author: nick
'''

from boards import ClassicBoard
from pieces import piece_types, colors, vanilla_type_to_obj
from players import player_types
from rules import VanillaRules

class VanillaChess(object):

    def __init__(self, white_player, black_player):
        self.name = 'Classic Chess'
        self.board = ClassicBoard()
        self.rules = VanillaRules()
        self.positions = {}
        self.players = [white_player, black_player]
        self.active_player_id = 0
        
        for player in self.players:
            if player.type == player_types.AI:
                player.register_game(self) #might be bad
        
    def __repr__(self):
        return 'VanillaChess(white_player=%r, black_player=%r)' % (self.players[0], self.players[1])
    
    def active_player(self):
        return self.players[self.active_player_id]
    
    def inactive_player(self):
        return self.players[(self.active_player_id + 1) % len(self.players)]
    
    def next_player(self):
        self.active_player_id = (self.active_player_id + 1) % len(self.players)
    
    def update_position_dict(self):
        try:
            self.positions[self.board] += 1
        except KeyError:
            self.positions[self.board] = 1
    
    def has_winner(self):
        return self.end_of_game(self.active_player().color) or self.end_of_game(-self.active_player().color)
    
    def end_of_game(self, color):
        result = self.rules.is_game_over(color, self.board, self.positions)
        if result:
            return result
        return False
    
    def get_move_for_player(self, player):
        if self.active_player().type == player_types.AI:
            return self.active_player().move()
        elif self.active_player().type == player_types.HUMAN:
            return self.interface.offer_move_to_human(self.active_player())
        else:
            raise TypeError()
    
    def play_turn(self, move):
        message = ''
        from_sq, to_sq = move
        is_valid = self.rules.move_piece(from_sq, to_sq, self.board)
        if is_valid:
            #self.update_position_dict()
            print self.positions
            is_end = self.end_of_game(-self.active_player().color)
            if is_end:
                message = 'Game over! %s' % is_end
            else:
                if self.has_promotion():
                    message = 'promote'
                self.next_player()
        else:
            message = 'invalid'
        return message
    
    def has_promotion(self):
        last_move = self.board.moves.peek() 
        if last_move is not None:
            if last_move[0].piece_type == piece_types.PAWN:
                if last_move[0].color == colors.WHITE:
                    if last_move[2][0] == self.board.height - 1:
                        return True
                elif last_move[0].color == colors.BLACK:
                    if last_move[2][0] == 0:
                        return True
            return False
    
    def handle_pawn_promotion(self, choice):
        last_move = self.board.moves.peek() 
        if last_move[0].piece_type == piece_types.PAWN:
            if last_move[0].color == colors.WHITE:
                if last_move[2][0] == self.board.height - 1:
                    self.board.pieces[last_move[2]] = vanilla_type_to_obj(choice, last_move[0].color)
                    self.board.moves.push((self.board.pieces[last_move[2]], last_move[1], last_move[2]))
            elif last_move[0].color == colors.BLACK:
                if last_move[2][0] == 0:
                    self.board.pieces[last_move[2]] = vanilla_type_to_obj(choice, last_move[0].color)
                    self.board.moves.push((self.board.pieces[last_move[2]], last_move[1], last_move[2]))