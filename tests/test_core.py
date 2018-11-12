'''
Created on Nov 12, 2018

@author: yangzh
'''
from .context import OS_Script

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(OS_Script.saySomething())


if __name__ == '__main__':
    unittest.main()