'''
Created on Jun 20, 2013

@author: nick
'''

import pygame

from players import player_types
from utils import spritesheet

from Interface import Interface
from pygamehelper import PygameHelper

class GUI(Interface, PygameHelper):
    
    def __init__(self, game_instance):
        Interface.__init__(self, game_instance)
        PygameHelper.__init__(self)
        self.first_selected_square = None
        self.second_selected_square = None
        self.current_move = None
        
        self.squares = []
        self.region_to_coord = {}
        self.coord_to_region = {}
        self.sprites = {}
        
        self.white_square_color = (247, 196, 145)
        self.black_square_color = (188, 123, 64)
        
        self.game = game_instance
        self.setup()
    
    #Functions for Interface
    def display_message(self, message):
        print message
    
    def offer_move_to_human(self):
        if self.first_selected_square is not None and self.second_selected_square is not None:
            return (self.first_selected_square, self.second_selected_square)
        
    def start(self):
        self.mainLoop(60)
    
    #Functions for class
    def setup(self):
        self.title = self.game.name
        self.create_squares()
        self.load_piece_images()
        
    def create_squares(self):
        unit_width = self.size[0] / self.game.board.width
        unit_height = self.size[1] / self.game.board.height
        for i in range(self.game.board.width):
            for j in range(self.game.board.height):
                #print 'Creating square: (%s, %s, %s, %s)' % (i * unit_width, j * unit_height, unit_width, unit_height)
                self.squares.append(pygame.Rect(i * unit_width, j * unit_height, unit_width, unit_height))
                self.region_to_coord[(i * unit_width, j * unit_height)] = ((self.game.board.width - j - 1), i)
                self.coord_to_region[((self.game.board.width - j - 1), i)] = (i * unit_width, j * unit_height)
                
    def load_piece_images(self):
        ss_path = ''
        ss = None
        for piece in self.game.board.pieces.values():
            if piece is not None:
                try:
                    if ss_path != piece.sprite_file:
                        ss = spritesheet(piece.sprite_file)
                except:
                    pass 
                try:
                    self.sprites[(piece.piece_type, piece.color)] = ss.image_at(piece.sprite_region(), colorkey=(0, 0, 255))
                except:
                    pass

    def highlight_selected_square(self):
        if self.first_selected_square is not None:
            pygame.draw.rect(self.screen, (0, 255, 0), self.first_selected_square, 1)

    def draw_squares(self):
        c = 0
        counted = 1
        for square in self.squares:
            if c == 0:
                pygame.draw.rect(self.screen, self.white_square_color, square)
            elif c == 1:
                pygame.draw.rect(self.screen, self.black_square_color, square)
            else:
                raise ValueError()
            if counted == self.game.board.height:
                counted = 1
            else:
                c = (c + 1) % 2
                counted += 1
    
    def draw_pieces(self):
        for square, piece in self.game.board.pieces.items():
            if piece is not None:
                try:
                    self.screen.blit(self.sprites[(piece.piece_type, piece.color)], self.coord_to_region[square])
                except:
                    pass
    
    #Functions for PygameHelper
    def mainLoop(self, fps=0):
        self.running = True
        self.fps = fps
        
        while self.running and not self.game.has_winner():
            pygame.display.set_caption("%s: (fps: %i)" % (self.title, self.clock.get_fps()))
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
            
            response = ''
            if self.game.active_player().type == player_types.HUMAN:
                if self.first_selected_square is not None and self.second_selected_square is not None:
                    print 'Attempting to move for %s...' % self.game.active_player()
                    from_sq = self.region_to_coord[(self.first_selected_square[0], self.first_selected_square[1])]
                    to_sq = self.region_to_coord[(self.second_selected_square[0], self.second_selected_square[1])]
                    response = self.game.play_turn((from_sq, to_sq))
            elif self.game.active_player().type == player_types.AI:
                from_sq, to_sq = self.game.active_player().move()
                response = self.game.play_turn((from_sq, to_sq))
            
            if response == 'promote':
                choice = self.offer_promote(self.game.active_player())
                self.game.handle_pawn_promotion(choice)
            elif response == 'invalid':
                self.display_message('Invalid move!')
            if self.first_selected_square is not None and self.second_selected_square is not None:
                self.first_selected_square = None
                self.second_selected_square = None
    
    def update(self):
        self.draw_squares()
        self.draw_pieces()
        self.highlight_selected_square()
    
    def mouseUp(self, button, pos):
        if self.game.active_player().type == player_types.HUMAN:
            clicked_squares = [s for s in self.squares if s.collidepoint(pos)]
            if len(clicked_squares) == 1:
                print clicked_squares[0], self.region_to_coord[(clicked_squares[0].x, clicked_squares[0].y)]
                square_coords = self.region_to_coord[(clicked_squares[0].x, clicked_squares[0].y)]
                if self.first_selected_square == clicked_squares[0]:
                    self.first_selected_square = None
                elif self.game.board.pieces[square_coords] is not None and self.first_selected_square is None:
                    if self.game.board.pieces[square_coords].color == self.game.active_player().color:
                        self.first_selected_square = clicked_squares[0]
                elif self.first_selected_square is not None and self.second_selected_square is None:
                    self.second_selected_square = clicked_squares[0]
                    
    def offer_promote(self, player):
        raise NotImplementedError()
                