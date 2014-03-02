'''
Created on Jun 22, 2013

@author: nick
'''
import inspect
import sys
import unittest

import tests

if __name__ == '__main__':
    test_classes = []
    
    for i in inspect.getmembers(sys.modules[tests.boardtests.__name__], inspect.isclass):
        test_classes.append(i[1])
    for i in inspect.getmembers(sys.modules[tests.gametests.__name__], inspect.isclass):
        test_classes.append(i[1])
    for i in inspect.getmembers(sys.modules[tests.ruletests.__name__], inspect.isclass):
        test_classes.append(i[1])
    
    suites = map(unittest.TestLoader().loadTestsFromTestCase, test_classes)
    alltests = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=1).run(alltests)
    #unittest.TextTestRunner(verbosity=1).run()