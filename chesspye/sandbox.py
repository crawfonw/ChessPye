'''
Created on Jun 21, 2013

@author: nick
'''
from pieces import colors
from boards import SmallTestBoard, PawnAndKnightsTestBoard
from games import VanillaChess
from interfaces import CLI, GUI
from players import HumanPlayer, RandomAI, HalfLookAI, NegamaxAI

import copy_reg
import types

def _pickle_method1(method):
    func_name = method.im_func.__name__
    obj = method.im_self
    cls = method.im_class
    return _unpickle_method, (func_name, obj, cls)

def _pickle_method(method):
    func_name = method.im_func.__name__
    obj = method.im_self
    cls = method.im_class
    if func_name.startswith('__') and not func_name.endswith('__'):
        cls_name = cls.__name__.lstrip('_')
    if cls_name:
        func_name = '_' + cls_name + func_name
    return _unpickle_method, (func_name, obj, cls)

def _unpickle_method(func_name, obj, cls):
    for cls in cls.mro():
        try:
            func = cls.__dict__[func_name]
        except KeyError:
            pass
        else:
            break
    return func.__get__(obj, cls)

if __name__ == '__main__':
    copy_reg.pickle(types.MethodType, _pickle_method1, _unpickle_method)
    #game = VanillaChess(HumanPlayer('White', colors.WHITE), HumanPlayer('Black', colors.BLACK))
    #game = VanillaChess(RandomAI('White', colors.WHITE), NegamaxAI('Black', colors.BLACK))
    game = VanillaChess(HumanPlayer('White', colors.WHITE), NegamaxAI('Black', colors.BLACK, False))
    #game = VanillaChess(NegamaxAI('Black', colors.BLACK), HumanPlayer('White', colors.WHITE))
    #game = VanillaChess(NegamaxAI('White', colors.WHITE), HumanPlayer('Black', colors.BLACK))
    game.board = PawnAndKnightsTestBoard()
    game.board.pretty_print = False
    #interface = CLI(game)
    interface = GUI(game)
    interface.start()