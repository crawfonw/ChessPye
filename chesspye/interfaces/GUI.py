'''
Created on Jun 20, 2013

@author: nick
'''

import pygame

from Interface import Interface
from pygamehelper import PygameHelper

class GUI(Interface, PygameHelper):
    
    def __init__(self):
        #super(GUI, self).__init__()
        PygameHelper.__init__(self)
        self.board_width = -1
        self.board_height = -1
        self.selected_square = None
        
        self.squares = []
        self.region_to_coord = {}
        
        self.white_square_color = (247, 196, 145)
        self.black_square_color = (188, 123, 64)
        
    def setup(self, game_instance):
        self.board_width = game_instance.board.width
        self.board_height = game_instance.board.height
        self.title = game_instance.name
        self.create_squares()
        self.load_piece_images()
        
    def create_squares(self):
        unit_width = self.size[0] / self.board_width 
        unit_height = self.size[1] / self.board_height
        for i in range(self.board_width):
            for j in range(self.board_height):
                print 'Creating square: (%s, %s, %s, %s)' % (i * unit_width, j * unit_height, unit_width, unit_height)
                self.squares.append(pygame.Rect(i * unit_width, j * unit_height, unit_width, unit_height))
                self.region_to_coord[(i * unit_width, j * unit_height)] = ((self.board_width - j - 1), i)
                
    def load_piece_images(self):
        pass

    def highlight_selected_square(self):
        if self.selected_square() is not None:
            

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
            if counted == self.board_height:
                counted = 1
            else:
                c = (c + 1) % 2
                counted += 1
    
    def draw_pieces(self):
        pass
                
    def update(self):
        #pygame.draw.rect(self.screen, (255,255,255), (0, self.size[0], 0, self.size[1]))
        self.draw_squares()
        self.highlight_selected_square()
    
    def mouseUp(self, button, pos):
        clicked_squares = [s for s in self.squares if s.collidepoint(pos)]
        if len(clicked_squares) == 1:
            print clicked_squares[0], self.region_to_coord[(clicked_squares[0].x, clicked_squares[0].y)]