##############################################################################################
### Import ###################################################################################
##############################################################################################

import json

##############################################################################################
### Class ####################################################################################
##############################################################################################


class JSONFile:
    """
    JSON file
    """

    @staticmethod
    def read_json_file(file_path: str, encoding: str = "utf-8") -> dict:
        """
        Read a JSON file
        :param file_path: The file path
        :param encoding: The encoding
        :return: The JSON data
        """
        # affiche le repertoire courrant puis le fichier
        with open(file_path, "r", encoding=encoding) as file:
            return json.load(file)

    @staticmethod
    def write_json_file(file_path: str, data: dict, encoding: str = "utf-8"):
        """
        Write a JSON file
        :param file_path: The file path
        :param data: The JSON data
        :param encoding: The encoding
        """
        with open(file_path, "w", encoding=encoding) as file:
            json.dump(data, file, indent=4)

##############################################################################################
### End : src/main/python/utiles/jsonFile.py #################################################
##############################################################################################
