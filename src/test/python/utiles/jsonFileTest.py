##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

os.chdir(os.path.join(os.getcwd().split("Jeu_de_la_vie")[0], "Jeu_de_la_vie", "src", "main"))

import json
import tempfile
import unittest

from src.main.python.utiles.jsonFile import JSONFile


##############################################################################################
### Class ####################################################################################
##############################################################################################

class JSONFileTests(unittest.TestCase):
    """
    Test suite for JSONFile utility functions.

    This class contains unit tests for reading from and writing to JSON files using the JSONFile utility.
    It tests both valid and invalid paths and data to ensure robust error handling and correct functionality.
    """

    def test_read_json_file_valid_path(self):
        """
        Test reading from a JSON file with a valid path.

        Ensures that the JSONFile.read_json_file function correctly reads data from a valid file path.
        """
        data = {"key": "value"}
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
            json.dump(data, temp_file)
            temp_file_path = temp_file.name

        result = JSONFile.read_json_file(temp_file_path)
        os.remove(temp_file_path)
        self.assertEqual(result, data)

    def test_write_json_file_valid_data(self):
        """
        Test writing to a JSON file with valid data.

        Ensures that the JSONFile.write_json_file function correctly writes data to a file and that
        the data can be read back accurately.
        """
        data = {"key": "value"}
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
            temp_file_path = temp_file.name

        JSONFile.write_json_file(temp_file_path, data)
        with open(temp_file_path, "r", encoding='utf-8') as file:
            result = json.load(file)
        os.remove(temp_file_path)
        self.assertEqual(result, data)

    def test_read_json_file_invalid_path(self):
        """
        Test reading from a JSON file with an invalid path.

        Ensures that the JSONFile.read_json_file function raises a FileNotFoundError when attempting
        to read from a non-existent file path.
        """
        with self.assertRaises(FileNotFoundError):
            JSONFile.read_json_file("non_existent_file.json")

    def test_write_json_file_invalid_path(self):
        """
        Test writing to a JSON file with an invalid path.

        Ensures that the JSONFile.write_json_file function raises a FileNotFoundError when attempting
        to write to a non-existent directory.
        """
        data = {"key": "value"}
        with self.assertRaises(FileNotFoundError):
            JSONFile.write_json_file("/invalid_path/file.json", data)

##############################################################################################
### End : src/test/python/utiles/jsonFileTest.py #############################################
##############################################################################################
