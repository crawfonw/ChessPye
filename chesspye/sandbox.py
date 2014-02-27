'''
Created on Jun 21, 2013

@author: nick
'''
from chesspye.board.pieces import colors
from chesspye.game.games import VanillaChess
from chesspye.interfaces.cli import CLI
from chesspye.players.players import HumanPlayer

if __name__ == '__main__':
    g = VanillaChess(HumanPlayer(colors.WHITE), HumanPlayer(colors.BLACK), CLI())
    g.board.pretty_print = False
    g.play_game()