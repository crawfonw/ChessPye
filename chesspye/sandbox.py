'''
Created on Jun 21, 2013

@author: nick
'''
from pieces import colors
from boards import SmallTestBoard, PawnAndKnightsTestBoard
from games import VanillaChess
from interfaces import CLI, GUI
from players import HumanPlayer, RandomAI, HalfLookAI, NegamaxAI

if __name__ == '__main__':
    white = NegamaxAI('White', colors.WHITE)
    black = HumanPlayer('Black', colors.BLACK)
    white.depth = 4
    white.parallel = True

    game = VanillaChess(white, black)
    game.board = SmallTestBoard()
    game.board.pretty_print = False
    #interface = CLI(game)
    interface = GUI(game)
    interface.start()