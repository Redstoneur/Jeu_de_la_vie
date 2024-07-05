##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

if os.getcwd().endswith("test\\python"):
    # Attempt to change the working directory to 'src/main/'
    # Adjust the path as necessary based on the actual structure
    os.chdir(os.path.join(os.getcwd(), "..", "..", "main"))

# import locale
import unittest

from src.main.python.models import Languages
from src.main.python.utiles import JSONFile, ResourcesPath


##############################################################################################
### Class ####################################################################################
##############################################################################################

class LanguagesTests(unittest.TestCase):
    def test_language_name(self):
        self.assertEqual(str(Languages.FR), "fr")
        self.assertEqual(str(Languages.EN), "en")

    def test_get_dictionary(self):
        self.assertEqual(Languages.FR.get_dictionary(), Languages.get_dictionary_language(Languages.FR))
        self.assertEqual(Languages.EN.get_dictionary(), Languages.get_dictionary_language(Languages.EN))

    def test_get_languages_french(self):
        self.assertEqual(Languages.get_languages("fr_FR"), Languages.FR)
        self.assertEqual(Languages.get_languages("fr_BE"), Languages.FR)
        self.assertEqual(Languages.get_languages("fr_CA"), Languages.FR)
        self.assertEqual(Languages.get_languages("fr_CH"), Languages.FR)
        self.assertEqual(Languages.get_languages("fr_LU"), Languages.FR)

    def test_get_languages_english(self):
        self.assertEqual(Languages.get_languages("en_US"), Languages.EN)
        self.assertEqual(Languages.get_languages("en_GB"), Languages.EN)
        self.assertEqual(Languages.get_languages("de_DE"), Languages.EN)

    # def test_get_system_language(self):
    #     locale.setlocale(locale.LC_ALL, 'en_US')
    #     self.assertEqual(Languages.get_system_language(), Languages.EN)
    #     locale.setlocale(locale.LC_ALL, 'fr_FR')
    #     self.assertEqual(Languages.get_system_language(), Languages.FR)

    def test_get_dictionary_language(self):
        self.assertEqual(
            Languages.get_dictionary_language(Languages.FR),
            JSONFile.read_json_file(os.path.join(ResourcesPath, "languages", f"{Languages.FR}.json"))
        )
        self.assertEqual(
            Languages.get_dictionary_language(Languages.EN),
            JSONFile.read_json_file(os.path.join(ResourcesPath, "languages", f"{Languages.EN}.json"))
        )

##############################################################################################
### End : src/test/python/model/languagesTest.py #############################################
##############################################################################################
