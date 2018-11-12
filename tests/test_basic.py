'''
Created on Nov 12, 2018

@author: yangzh
'''
from .context import OS_Script

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()