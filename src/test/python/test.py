##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

## récupérer le répertoire courant du fichier main.py sans os.get
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Change the working directory to 'src/main/' if the current working directory ends with 'test\\python'
if os.getcwd().endswith("test\\python"):
    # Attempt to change the working directory to 'src/main/'
    # Adjust the path as necessary based on the actual structure
    os.chdir(os.path.join(os.getcwd(), "..", "..", "main"))

print(os.getcwd())

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
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LanguagesTests))
    suite.addTest(unittest.makeSuite(JSONFileTests))
    suite.addTest(unittest.makeSuite(DimensionsWindowsTests))
    suite.addTest(unittest.makeSuite(GameOfLifeTests))
    return suite

##############################################################################################
### Main Execution ##########################################################################
##############################################################################################

if __name__ == '__main__':
    """
    Main execution block.

    If this script is executed as the main program, it creates a test runner and runs the test suite
    defined by the suite() function, allowing for the execution of all included unit tests.
    """
    runner = unittest.TextTestRunner()
    runner.run(suite())