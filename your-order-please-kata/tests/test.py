import unittest
import sys
import os

# Getting the name of the directory
# Where the this file is present.
currentDir = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
# where the current directory is present.
parentDir = os.path.dirname(currentDir)
# Adding the parent directory to
# the sys.path.
sys.path.append(parentDir)

import order


class testYourOrder(unittest.TestCase):
    
    def standarUse(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
    
    def emptyString(self):
        self.assertEqual(order(""), "")

if __name__ == '__main__':
    unittest.main()