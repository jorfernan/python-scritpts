import os
import sys
import unittest

# Getting the name of the directory
# Where the this file is present.
currentDir = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
# where the current directory is present.
parentDir = os.path.dirname(currentDir)
# Adding the parent directory to
# the sys.path.
sys.path.append(parentDir)

from order import order_sentence


class testYourOrder(unittest.TestCase):
    
    def test_standard_use(self):
        self.assertEqual(order_sentence("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(order_sentence("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
    
    def test_empty_string(self):
        self.assertEqual(order_sentence(""), "")

if __name__ == '__main__':
    unittest.main()