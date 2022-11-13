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

from expanded_float import expanded_form

class testExpandedForm1(unittest.TestCase):
    def test_standard_use(self):
        self.assertEqual(expanded_form(807.304), "800 + 7 + 3/10 + 4/1000")
        self.assertEqual(expanded_form(1.24), "1 + 2/10 + 4/100")
        self.assertEqual(expanded_form(7.304), "7 + 3/10 + 4/1000")
        self.assertEqual(expanded_form(0.04), "4/100")
if __name__ == '__main__':
    unittest.main()