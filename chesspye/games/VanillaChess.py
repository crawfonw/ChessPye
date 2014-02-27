'''
Created on Jun 20, 2013

@author: nick
'''

from chesspye.boards import ClassicBoard
from chesspye.pieces import piece_types, colors
from chesspye.rules import VanillaRules

class VanillaChess(object):

    def __init__(self, white_player, black_player, interface):
        self.board = ClassicBoard()
        self.rules = VanillaRules()
        self.positions = {}
        self.interface = interface
        self.players = [white_player, black_player]
        self.active_player_id = 0
        
    def __repr__(self):
        return 'VanillaChess(white_player=%r, black_player=%r)' % (self.white_player, self.black_player)
    
    def active_player(self):
        return self.players[self.active_player_id]
    
    def next_player(self):
        self.active_player_id = (self.active_player_id + 1) % len(self.players)
    
    def handle_pawn_promotion(self):
        last_move = self.board.moves.peek() 
        if last_move[0].piece_type == piece_types.PAWN:
            if last_move[0].color == colors.WHITE:
                if last_move[2][0] == self.board.height - 1:
                    self.dispatch_promotion_choice(last_move)
            elif last_move[0].color == colors.BLACK:
                if last_move[2][0] == 0:
                    self.dispatch_promotion_choice(last_move)
    
    def dispatch_promotion_choice(self, move):
        new_piece_obj = self.interface.promote(self.active_player())
        self.board[move[2]] = new_piece_obj
    
    def update_position_dict(self):
        try:
            self.positions[self.board] += 1
        except KeyError:
            self.positions[self.board] = 1
    
    def end_of_game(self, color):
        result = self.rules.is_game_over(color, self.board, self.positions)
        if result:
            return result
        return False
    
    def end_of_turn_cleanup(self):
        self.handle_pawn_promotion()
    
    def play_game(self):
        while True:
            self.interface.draw_board_update(self.board)
            move = self.interface.offer_move(self.active_player())
            if isinstance(move, str):
                from_sq, to_sq = move.split('-')
            elif isinstance(move, tuple):
                from_sq, to_sq = move
            else:
                from_sq, to_sq = (None, None)
            is_valid = self.rules.move_piece(from_sq, to_sq, self.board)
            if is_valid:
                self.end_of_turn_cleanup()
                if self.end_of_game(self.active_player().color * -1):
                    break
                else:
                    self.next_player()
            else:
                self.interface.display_message('Invalid move')
        return self.active_player()

''' This will probably be moved to an AI player since they would only use this...
    def score_board(self):
        if self.is_king_in_checkmate(colors.WHITE):
            return float('inf')
        elif self.is_king_in_checkmate(colors.BLACK):
            return float('-inf')
        else:
            score = 0
            for piece in self.board.pieces.itervalues():
                if piece is not None:
                    score += piece.color * piece.value
        return score 
'''