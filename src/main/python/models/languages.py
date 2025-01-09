##############################################################################################
### Import ###################################################################################
##############################################################################################

import os
import enum
import locale

from src.main.python.utiles import JSONFile, ResourcesPath


##############################################################################################
### Class ####################################################################################
##############################################################################################

class Languages(enum.Enum):
    """
    Languages of the application
    """
    FR = "fr"  # French
    EN = "en"  # English

    def __str__(self) -> str:
        """
        Return the language name
        :return: The language name
        """
        return self.value

    def get_dictionary(self) -> dict:
        """
        Return the dictionary of the language.
        :return: The dictionary of the language
        """
        return Languages.get_dictionary_language(self)

    @staticmethod
    def get_languages(system_language: str) -> 'Languages':
        """
        Return the languages of the application
        :param system_language: The system language
        :return: The languages of the application
        """
        if system_language in ["fr_FR", "fr_BE", "fr_CA", "fr_CH", "fr_LU"]:
            return Languages.FR
        return Languages.EN

    @staticmethod
    def get_system_language() -> 'Languages':
        """
        Return the system language
        :return: The system language
        """
        return Languages.get_languages(locale.getdefaultlocale()[0])

    @staticmethod
    def get_dictionary_language(language: 'Languages') -> dict:
        """
        Return the dictionary of the language.
        :param language: The language
        :return: The dictionary of the language
        """
        try:
            return JSONFile.read_json_file(
                os.path.join(ResourcesPath, "languages", f"{language}.json")
            )
        except FileNotFoundError:
            return JSONFile.read_json_file(
                os.path.join(ResourcesPath, "languages", f"{Languages.EN}.json")
            )
        except Exception as e:
            print(f"Erreur inattendue: {e}")
            return {}

##############################################################################################
### End : src/main/models/languagesTest.py ########################################################
##############################################################################################
