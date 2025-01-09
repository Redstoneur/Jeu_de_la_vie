##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

os.chdir(os.path.join(os.getcwd().split("Jeu_de_la_vie")[0], "Jeu_de_la_vie", "src", "main"))

import unittest

from src.test.python.model.languagesTest import LanguagesTests
from src.test.python.utiles.jsonFileTest import JSONFileTests
from src.test.python.views.dimensionsWindowsTest import DimensionsWindowsTests
from src.test.python.views.gameOfLifeTest import GameOfLifeTests


##############################################################################################
### Suite Function ###########################################################################
##############################################################################################

def suite():
    """
    Create and return a test suite.

    Combines tests from LanguagesTests, JSONFileTests, DimensionsWindowsTests, and GameOfLifeTests
    into a single test suite, allowing for the grouped execution of tests across different modules.
    """
    sequence = unittest.TestSuite()
    sequence.addTest(unittest.makeSuite(LanguagesTests))
    sequence.addTest(unittest.makeSuite(JSONFileTests))
    sequence.addTest(unittest.makeSuite(DimensionsWindowsTests))
    sequence.addTest(unittest.makeSuite(GameOfLifeTests))
    return sequence


##############################################################################################
### Main Execution ##########################################################################
##############################################################################################

if __name__ == '__main__':
    # Main execution block.
    #
    # If this script is executed as the main program, it creates a test runner and runs the test
    # sequence defined by the suite() function, allowing for the execution of all included unit
    # tests.

    runner = unittest.TextTestRunner()
    runner.run(suite())
