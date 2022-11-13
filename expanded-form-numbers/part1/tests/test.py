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

from expanded import expanded_form

class testExpandedForm1(unittest.TestCase):
    
    def test_standard_use(self):
        self.assertEqual(expanded_form(12), '10 + 2');
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')
        self.assertEqual(expanded_form(12563), '10000 + 2000 + 500 + 60 + 3')
if __name__ == '__main__':
    unittest.main()