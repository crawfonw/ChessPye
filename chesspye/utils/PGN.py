'''
Created on Mar 1, 2014

@author: Nick Crawford
'''

import pgn
    
def get_list_of_moves_from_pgn(pgn_path): #includes comments & W/L/D result
    pgn_text = open(pgn_path).read()
    pgn_games = pgn.loads(pgn_text)
    return [game.moves for game in pgn_games]