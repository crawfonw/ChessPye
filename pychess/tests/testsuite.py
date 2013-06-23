'''
Created on Jun 22, 2013

@author: nick
'''

import unittest

from boardtests import *

if __name__ == '__main__':
    test_classes = [TestBoard, TestClassicalBoard]
    suites = map(unittest.TestLoader().loadTestsFromTestCase, test_classes)
    alltests = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=1).run(alltests)