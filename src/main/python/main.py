##############################################################################################
### Import ###################################################################################
##############################################################################################

import os

## récupérer le répertoire courant du fichier main.py sans os.get
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__" and os.path.basename(os.getcwd()) == "python":
    # Attempt to change the working directory to 'src/main/'
    # Adjust the path as necessary based on the actual structure
    os.chdir(os.path.join(os.getcwd(), ".."))

from src.main.python.models import Languages
from src.main.python.views import GameOfLife


##############################################################################################
### Function #################################################################################
##############################################################################################

def main():
    """
    Main function
    """
    game = GameOfLife(Languages.get_system_language())
    game.show()


##############################################################################################
### Execution ################################################################################
##############################################################################################

if __name__ == "__main__":
    main()

##############################################################################################
### End : src/main/python/main.py ############################################################
##############################################################################################
