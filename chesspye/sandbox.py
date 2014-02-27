'''
Created on Jun 21, 2013

@author: nick
'''
from chesspye.pieces import colors
from chesspye.games import VanillaChess
from chesspye.interfaces import CLI
from chesspye.players import HumanPlayer, RandomAI

if __name__ == '__main__':
    #g = VanillaChess(HumanPlayer('White', colors.WHITE), HumanPlayer('Black', colors.BLACK), CLI())
    g = VanillaChess(HumanPlayer('White', colors.WHITE), RandomAI('Black', colors.BLACK), CLI())
    g.board.pretty_print = False
    g.play_game()