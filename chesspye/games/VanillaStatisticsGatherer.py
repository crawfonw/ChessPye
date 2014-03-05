'''
Created on Mar 5, 2015

@author: Nick Crawford
'''

import datetime
import time

import os

from VanillaChess import VanillaChess
from players import player_types
from pieces import colors

class VanillaStatisticsGatherer(VanillaChess):

    def __init__(self, white_player, black_player):
        super(VanillaStatisticsGatherer, self).__init__(white_player, black_player)
        self.start = datetime.datetime.now()
        self.stat_file = 'stats' + os.sep + (str(self.start).split('.')[0]).replace(' ', '_').replace(':', '-') + '.txt'
        self.move_count = 0
        self.avg_computing_time = {self.players[0].name:0, self.players[1].name:0}
        self.positions_analysed = {self.players[0].name:0, self.players[1].name:0}
        
        self.print_game_info_to_file()
    
    def print_game_info_to_file(self):
        f = open(self.stat_file, 'w')
        f.write('Game at %s\n' % self.start)
        for player in self.players:
            if player.color == colors.WHITE:
                f.write('White player: %s (type=%s)\n' % (player, player.type))
            else:
                f.write('Black player: %s (type=%s)\n' % (player, player.type))
            if player.type == player_types.AI:
                f.write('\tAI type: %s\n' % type(player))
                f.write('\tScoring function: %s.%s\n' % (player.scoring_f.__module__, player.scoring_f.func_name))
                f.write('\tSearch Depth: %s\n' % player.depth)
                f.write('\tParallel = %s\n' % player.parallel)
        f.write('\n')
        f.close()
    
    def get_move_for_player(self, player):
        if self.active_player().type == player_types.AI:
            t1 = time.time()
            move = self.active_player().move()
            t2 = time.time()            
            f = open(self.stat_file, 'w')
            deltaT = float(t2 - t1)
            f.write("%s's move: %s\n" % self.board.coordinate_to_algebraic_move(move[0], move[1]))
            f.write('\t%s positions anaylzed for this move\n' % self.active_player().last_nodes_expanded)
            f.write('\tTime taken: %s seconds\n' % deltaT)
            self.avg_computing_time[self.active_player().name] += deltaT
            self.positions_analysed[self.active_player().name] += self.active_player().last_nodes_expanded
            f.close()
            return move 
        elif self.active_player().type == player_types.HUMAN:
            move = self.interface.offer_move_to_human(self.active_player())
            f = open(self.stat_file, 'w')
            f.write("%s's move: %s\n" % self.board.coordinate_to_algebraic_move(move[0], move[1]))
            f.close()
            return move
        else:
            raise TypeError()
        
    def play_turn(self, move):
        message = super(VanillaStatisticsGatherer, self).play_turn(move)
        if message != 'invalid':
            f = open(self.stat_file, 'w')
            f.write('%s moves played\n' % self.move_count)
            f.close()
            self.move_count += 1
        return message
    
    def end_of_game(self, color):
        result = self.rules.is_game_over(color, self.board, self.positions)
        if result:
            for player in players:
                if player.type == player_types.AI:
                    f = open(self.stat_file, 'w')
                    f.write('Player %s stats:\n' % player)
                    num_moves = self.move_count / 2
                    if player.color == colors.WHITE:
                        if self.move_count % 2 != 0:
                            num_moves += 1
                    f.write('Total moves: %s\n' % num_moves) #want to round down for black
                    f.write('Avg. computation time: %s sec\n' % self.avg_computing_time[player.name] / num_moves)
                    f.write('Total number of positions analyzed: %s\n' % self.positions_analysed[player.name])
            return result
        return False