##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

if os.getcwd().endswith("test\\python"):
    # Attempt to change the working directory to 'src/main/'
    # Adjust the path as necessary based on the actual structure
    os.chdir(os.path.join(os.getcwd(), "..", "..", "main"))

import unittest

from src.test.python.model.languagesTest import LanguagesTests
from src.test.python.utiles.jsonFileTest import JSONFileTests
from src.test.python.views.dimensionsWindowsTest import DimensionsWindowsTests
from src.test.python.views.gameOfLifeTest import GameOfLifeTests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LanguagesTests))
    suite.addTest(unittest.makeSuite(JSONFileTests))
    suite.addTest(unittest.makeSuite(DimensionsWindowsTests))
    suite.addTest(unittest.makeSuite(GameOfLifeTests))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
