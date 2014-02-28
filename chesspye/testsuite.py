'''
Created on Jun 22, 2013

@author: nick
'''

import unittest

from tests.boardtests import *
from tests.gametests import *
from tests.ruletests import *

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=1).run()