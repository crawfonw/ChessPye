'''
Created on Jun 21, 2013

@author: nick
'''
from pieces import colors
from boards import SmallTestBoard
from games import VanillaChess
from interfaces import CLI, GUI
from players import HumanPlayer, RandomAI, HalfLookAI, NegamaxAI

if __name__ == '__main__':
    #game = VanillaChess(HumanPlayer('White', colors.WHITE), HumanPlayer('Black', colors.BLACK))
    #game = VanillaChess(RandomAI('White', colors.WHITE), NegamaxAI('Black', colors.BLACK))
    #game = VanillaChess(HumanPlayer('White', colors.WHITE), NegamaxAI('Black', colors.BLACK))
    #game = VanillaChess(NegamaxAI('Black', colors.BLACK), HumanPlayer('White', colors.WHITE))
    game = VanillaChess(NegamaxAI('White', colors.WHITE), HumanPlayer('Black', colors.BLACK))
    game.board = SmallTestBoard()
    game.board.pretty_print = False
    #interface = CLI(game)
    interface = GUI(game)
    interface.start()