'''
Created on Jun 20, 2013

@author: nick
'''

import pygame

from Interface import Interface
from pygamehelper import PygameHelper
from utils import spritesheet

class GUI(Interface, PygameHelper):
    
    def __init__(self):
        #super(GUI, self).__init__()
        PygameHelper.__init__(self)
        self.board = None
        self.selected_square = None
        
        self.squares = []
        self.region_to_coord = {}
        self.coord_to_region = {}
        self.sprites = {}
        
        self.white_square_color = (247, 196, 145)
        self.black_square_color = (188, 123, 64)
        
    def setup(self, game_instance):
        self.board = game_instance.board
        self.title = game_instance.name
        self.create_squares()
        self.load_piece_images()
        
    def create_squares(self):
        unit_width = self.size[0] / self.board.width 
        unit_height = self.size[1] / self.board.height
        for i in range(self.board.width):
            for j in range(self.board.height):
                print 'Creating square: (%s, %s, %s, %s)' % (i * unit_width, j * unit_height, unit_width, unit_height)
                self.squares.append(pygame.Rect(i * unit_width, j * unit_height, unit_width, unit_height))
                self.region_to_coord[(i * unit_width, j * unit_height)] = ((self.board.width - j - 1), i)
                self.coord_to_region[((self.board.width - j - 1), i)] = (i * unit_width, j * unit_height)
                
    def load_piece_images(self):
        ss_path = ''
        ss = None
        for piece in self.board.pieces.values():
            if piece is not None:
                try:
                    if ss_path != piece.sprite_file:
                        ss = spritesheet(piece.sprite_file)
                except:
                    pass 
                try:
                    self.sprites[piece.piece_type] = ss.image_at(piece.sprite_region())
                except:
                    pass

    def highlight_selected_square(self):
        if self.selected_square is not None:
            pygame.draw.rect(self.screen, (0, 255, 0), self.selected_square, 1)

    def draw_squares(self):
        c = 1
        counted = 1
        for square in self.squares:
            if c == 0:
                pygame.draw.rect(self.screen, self.white_square_color, square)
            elif c == 1:
                pygame.draw.rect(self.screen, self.black_square_color, square)
            else:
                raise ValueError()
            if counted == self.board.height:
                counted = 1
            else:
                c = (c + 1) % 2
                counted += 1
    
    def draw_pieces(self):
        for square, piece in self.board.pieces.items():
            if piece is not None:
                try:
                    self.screen.blit(self.sprites[piece.piece_type], self.coord_to_region[square])
                except:
                    pass
                
    def update(self):
        #pygame.draw.rect(self.screen, (255,255,255), (0, self.size[0], 0, self.size[1]))
        self.draw_squares()
        self.draw_pieces()
        self.highlight_selected_square()
    
    def mouseUp(self, button, pos):
        clicked_squares = [s for s in self.squares if s.collidepoint(pos)]
        if len(clicked_squares) == 1:
            print clicked_squares[0], self.region_to_coord[(clicked_squares[0].x, clicked_squares[0].y)]
            if self.selected_square == clicked_squares[0]:
                self.selected_square = None
            else:
                self.selected_square = clicked_squares[0]
                