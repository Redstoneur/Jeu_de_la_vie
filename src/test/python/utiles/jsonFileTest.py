##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

if os.getcwd().endswith("test\\python"):
    # Attempt to change the working directory to 'src/main/'
    # Adjust the path as necessary based on the actual structure
    os.chdir(os.path.join(os.getcwd(), "..", "..", "main"))

import json
import tempfile
import unittest

from src.main.python.utiles.jsonFile import JSONFile


##############################################################################################
### Class ####################################################################################
##############################################################################################

class JSONFileTests(unittest.TestCase):

    def test_read_json_file_valid_path(self):
        data = {"key": "value"}
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
            json.dump(data, temp_file)
            temp_file_path = temp_file.name

        result = JSONFile.read_json_file(temp_file_path)
        os.remove(temp_file_path)
        self.assertEqual(result, data)

    def test_write_json_file_valid_data(self):
        data = {"key": "value"}
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
            temp_file_path = temp_file.name

        JSONFile.write_json_file(temp_file_path, data)
        with open(temp_file_path, "r", encoding='utf-8') as file:
            result = json.load(file)
        os.remove(temp_file_path)
        self.assertEqual(result, data)

    def test_read_json_file_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            JSONFile.read_json_file("non_existent_file.json")

    def test_write_json_file_invalid_path(self):
        data = {"key": "value"}
        with self.assertRaises(FileNotFoundError):
            JSONFile.write_json_file("/invalid_path/file.json", data)

##############################################################################################
### End : src/test/python/utiles/jsonFileTest.py #############################################
##############################################################################################
