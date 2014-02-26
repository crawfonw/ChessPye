'''
Created on Jun 22, 2013

@author: nick
'''

import unittest

from boardtests import *
from gametests import *
from ruletests import *

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=1).run()