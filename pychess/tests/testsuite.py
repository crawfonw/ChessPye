'''
Created on Jun 22, 2013

@author: nick
'''

import unittest

if __name__ == '__main__':
    suites = map(unittest.TestLoader().loadTestsFromTestCase, [])
    alltests = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=1).run(alltests)