'''
Created on Jun 21, 2013

@author: nick
'''
from pieces import colors
from games import VanillaChess
from interfaces import CLI, GUI
from players import HumanPlayer, RandomAI

if __name__ == '__main__':
    #game = VanillaChess(HumanPlayer('White', colors.WHITE), HumanPlayer('Black', colors.BLACK))
    game = VanillaChess(HumanPlayer('White', colors.WHITE), RandomAI('Black', colors.BLACK))
    game.board.pretty_print = False
    #interface = CLI(game)
    interface = GUI(game)
    interface.start()