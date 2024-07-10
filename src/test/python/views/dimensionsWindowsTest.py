##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

if os.getcwd()!= os.path.dirname(os.path.abspath(__file__)):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Change the working directory to 'src/main/' if the current working directory ends with 'test\\python'
if os.getcwd().endswith("test\\python"):
    # Attempt to change the working directory to 'src/main/'
    # Adjust the path as necessary based on the actual structure
    os.chdir(os.path.join(os.getcwd(), "..", "..", "main"))

import unittest
from unittest.mock import patch, MagicMock

from src.main.python.models import Languages
from src.main.python.utiles import Dimensions
from src.main.python.views.dimensionsWindows import DimensionsWindows


##############################################################################################
### Class ####################################################################################
##############################################################################################

class DimensionsWindowsTests(unittest.TestCase):
    """
    Test suite for the DimensionsWindows class.

    This class tests the functionality of the DimensionsWindows class, including the validation,
    default setting, maximization, and cancellation of window dimensions.
    """

    def setUp(self):
        """
        Set up the test environment.

        Retrieves the system language to be used in creating DimensionsWindows instances.
        """
        self.lang = Languages.get_system_language()

    @patch('src.main.python.views.dimensionsWindows.DimensionsWindows.destroy')
    def test_dimensionsAreValidatedCorrectly(self, destroy_mock):
        """
        Test that valid dimensions are correctly validated and set.

        Ensures that when valid dimensions are input, they are correctly validated and set,
        and the window is destroyed.
        """
        window = DimensionsWindows(self.lang)
        window.text_area_height.delete("1.0", "end")
        window.text_area_height.insert("end", "300")
        window.text_area_width.delete("1.0", "end")
        window.text_area_width.insert("end", "150")
        window.validate()
        self.assertEqual(Dimensions["Interface"]["Height"], 300)
        self.assertEqual(Dimensions["Interface"]["Width"], 150)
        destroy_mock.assert_called_once()

    @patch('src.main.python.views.dimensionsWindows.DimensionsWindows.destroy')
    def test_dimensionsAreSetToDefaultCorrectly(self, destroy_mock):
        """
        Test that dimensions are correctly reset to default values.

        Ensures that the default method correctly resets the dimensions to their default values,
        and the window is destroyed.
        """
        window = DimensionsWindows(self.lang)
        window.default()
        self.assertEqual(Dimensions["Interface"]["Height"], 500)
        self.assertEqual(Dimensions["Interface"]["Width"], 500)
        destroy_mock.assert_called_once()

    @patch('src.main.python.views.dimensionsWindows.DimensionsWindows.destroy')
    def test_dimensionsAreSetToMaxCorrectly(self, destroy_mock):
        """
        Test that dimensions are correctly maximized.

        Ensures that the max_dim method correctly sets the dimensions to the maximum screen size,
        and the window is destroyed.
        """
        window = DimensionsWindows(self.lang)
        window.winfo_screenheight = MagicMock(return_value=1080)
        window.winfo_screenwidth = MagicMock(return_value=1920)
        window.max_dim()
        self.assertEqual(Dimensions["Interface"]["Height"], 1080)
        self.assertEqual(Dimensions["Interface"]["Width"], 1920)
        destroy_mock.assert_called_once()

    @patch('src.main.python.views.dimensionsWindows.DimensionsWindows.destroy')
    def test_invalidDimensionsAreIgnored(self, destroy_mock):
        """
        Test that invalid dimensions are ignored.

        Ensures that when invalid dimensions are input, they are ignored and do not affect the
        current dimensions, and the window is destroyed.
        """
        window = DimensionsWindows(self.lang)
        window.text_area_height.delete("1.0", "end")
        window.text_area_height.insert("end", "invalid")
        window.text_area_width.delete("1.0", "end")
        window.text_area_width.insert("end", "invalid")
        window.validate()
        self.assertNotEqual(Dimensions["Interface"]["Height"], "invalid")
        self.assertNotEqual(Dimensions["Interface"]["Width"], "invalid")
        destroy_mock.assert_called_once()

    @patch('src.main.python.views.dimensionsWindows.DimensionsWindows.destroy')
    def test_cancelDoesNotChangeDimensions(self, destroy_mock):
        """
        Test that cancelling does not change the dimensions.

        Ensures that the cancel method does not alter the current dimensions and destroys the window.
        """
        original_height = Dimensions["Interface"]["Height"]
        original_width = Dimensions["Interface"]["Width"]
        window = DimensionsWindows(self.lang)
        window.cancel()
        self.assertEqual(Dimensions["Interface"]["Height"], original_height)
        self.assertEqual(Dimensions["Interface"]["Width"], original_width)
        destroy_mock.assert_called_once()

##############################################################################################
### End : src/test/python/views/dimensionsWindowsTest.py #####################################
##############################################################################################