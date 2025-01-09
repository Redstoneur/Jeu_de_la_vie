##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

os.chdir(os.path.join(os.getcwd().rpartition("Jeu_de_la_vie")[0], "Jeu_de_la_vie", "src", "main"))

# import locale
import unittest

from src.main.python.models import Languages
from src.main.python.utiles import JSONFile, ResourcesPath


##############################################################################################
### Class ####################################################################################
##############################################################################################

class LanguagesTests(unittest.TestCase):
    """
    A test suite for the Languages model.

    This class contains unit tests for the Languages model, which tests language identification,
    dictionary retrieval based on language, and language retrieval based on locale codes.
    """

    def test_language_name(self):
        """
        Test the string representation of Languages enum members.
        """
        self.assertEqual(str(Languages.FR), "fr")
        self.assertEqual(str(Languages.EN), "en")

    def test_get_dictionary(self):
        """
        Test the retrieval of language dictionaries through the get_dictionary method.
        """
        self.assertEqual(Languages.FR.get_dictionary(),
                         Languages.get_dictionary_language(Languages.FR))
        self.assertEqual(Languages.EN.get_dictionary(),
                         Languages.get_dictionary_language(Languages.EN))

    def test_get_languages_french(self):
        """
        Test the retrieval of the French language enum based on different French locale codes.
        """
        self.assertEqual(Languages.get_languages("fr_FR"), Languages.FR)
        self.assertEqual(Languages.get_languages("fr_BE"), Languages.FR)
        self.assertEqual(Languages.get_languages("fr_CA"), Languages.FR)
        self.assertEqual(Languages.get_languages("fr_CH"), Languages.FR)
        self.assertEqual(Languages.get_languages("fr_LU"), Languages.FR)

    def test_get_languages_english(self):
        """
        Test the retrieval of the English language enum based on English and German locale codes.
        """
        self.assertEqual(Languages.get_languages("en_US"), Languages.EN)
        self.assertEqual(Languages.get_languages("en_GB"), Languages.EN)
        # This line seems to incorrectly map German locale to English language, possibly a mistake
        # or a placeholder for a test scenario.
        self.assertEqual(Languages.get_languages("de_DE"), Languages.EN)

    # def test_get_system_language(self):
    #     """
    #     Test the retrieval of the system language.
    #     """
    #     locale.setlocale(locale.LC_ALL, 'en_US')
    #     self.assertEqual(Languages.get_system_language(), Languages.EN)
    #     locale.setlocale(locale.LC_ALL, 'fr_FR')
    #     self.assertEqual(Languages.get_system_language(), Languages.FR)

    def test_get_dictionary_language(self):
        """
        Test the retrieval of dictionaries for French and English languages from JSON files.
        """
        self.assertEqual(
            Languages.get_dictionary_language(Languages.FR),
            JSONFile.read_json_file(
                os.path.join(ResourcesPath, "languages", f"{Languages.FR}.json"))
        )
        self.assertEqual(
            Languages.get_dictionary_language(Languages.EN),
            JSONFile.read_json_file(
                os.path.join(ResourcesPath, "languages", f"{Languages.EN}.json"))
        )

##############################################################################################
### End : src/test/python/model/languagesTest.py #############################################
##############################################################################################
