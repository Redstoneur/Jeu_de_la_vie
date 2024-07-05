##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

if os.getcwd().endswith("test\\python"):
    # Attempt to change the working directory to 'src/main/'
    # Adjust the path as necessary based on the actual structure
    os.chdir(os.path.join(os.getcwd(), "..", "..", "main"))

import unittest
from tkinter import Tk, Event
from unittest.mock import MagicMock

import numpy as np

from src.main.python.models.languages import Languages
from src.main.python.views.gameOfLife import GameOfLife


##############################################################################################
### Class ####################################################################################
##############################################################################################

class GameOfLifeTests(unittest.TestCase):

    def setUp(self):
        self.lang = Languages.EN  # Assuming ENGLISH is a valid enum in Languages
        self.game = GameOfLife(self.lang)
        self.game.master = MagicMock(spec=Tk)  # Mock Tk to avoid GUI operations during tests

    def grid_initially_empty(self):
        expected_grid = np.zeros((50, 50), dtype=int)
        np.testing.assert_array_equal(self.game.grid, expected_grid)

    def init_grid_resets_to_empty(self):
        self.game.grid[10, 10] = 1  # Make a change
        self.game.init_grid()
        expected_grid = np.zeros((50, 50), dtype=int)
        np.testing.assert_array_equal(self.game.grid, expected_grid)

    def start_animation_updates_grid(self):
        self.game.wait_time = 0  # Set wait time to 0 to speed up the test
        self.game.running = True
        self.game.grid[1, 2] = 1
        self.game.grid[2, 3] = 1
        self.game.grid[3, 1] = 1
        self.game.grid[3, 2] = 1
        self.game.grid[3, 3] = 1
        self.game.start_animation()
        self.game.running = False  # Stop the animation
        self.assertNotEqual(np.sum(self.game.grid), 5)  # Grid should have changed

    def stop_animation_stops_updates(self):
        self.game.running = True
        self.game.stop_animation()
        self.assertFalse(self.game.running)

    def toggle_cell_changes_state(self):
        self.game.toggle_cell(MockEvent(10, 10))
        self.assertEqual(self.game.grid[1, 1], 1)
        self.game.toggle_cell(MockEvent(10, 10))
        self.assertEqual(self.game.grid[1, 1], 0)

    def count_alive_cells_correct(self):
        self.game.grid[10, 10] = 1
        self.game.grid[20, 20] = 1
        self.assertEqual(self.game.count_alive_cells(), 2)

    def select_wait_updates_wait_time(self):
        self.game.select_wait(100)
        self.assertEqual(self.game.wait_time, 100)

    def change_dim_window_updates_dimensions(self):
        original_dim_h = self.game.dim_h
        original_dim_w = self.game.dim_w
        # Assuming DimensionsWindows modifies Dimensions["Interface"]["Height"] and Width
        self.game.change_dim_window()
        self.assertNotEqual(self.game.dim_h, original_dim_h)
        self.assertNotEqual(self.game.dim_w, original_dim_w)


class MockEvent(Event):
    def __init__(self, x, y):
        self.x = x
        self.y = y


##############################################################################################
### Execution ################################################################################
##############################################################################################

if __name__ == '__main__':
    # Attempt to change the working directory to 'src/main/'
    # Adjust the path as necessary based on the actual structure
    os.chdir(os.path.join(os.getcwd(), "..", "..", "main"))

    unittest.main()

##############################################################################################
### End : src/test/python/views/gameOfLifeTest.py ############################################
##############################################################################################
