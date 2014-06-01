'''
Created on Jun 21, 2013

@author: nick
'''
from pieces import colors
from boards import SmallTestBoard, PawnAndKnightsTestBoard
from games import VanillaChess, VanillaStatisticsGatherer
from interfaces import CLI, GUI
from players import HumanPlayer, RandomAI, HalfLookAI, NegamaxAlphaBetaAI, NegascoutAI

if __name__ == '__main__':
    #white = NegamaxAlphaBetaAI('White', colors.WHITE)
    white = HumanPlayer('White', colors.WHITE)
    black = HumanPlayer('Black', colors.BLACK)
    #black = NegascoutAI('Black', colors.BLACK)
    #white.depth = 4
    #black.depth = 4
    #white.parallel = True

    game = VanillaChess(white, black)
    #game = VanillaStatisticsGatherer(white, black)
    game.board = SmallTestBoard()
    #game.board = PawnAndKnightsTestBoard()
    game.board.pretty_print = False
    #interface = CLI(game)
    interface = GUI(game)
    interface.start()