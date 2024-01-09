import enum
import locale
import random as rd
import tkinter as tk

import numpy as np


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


Language_Appli: Languages = Languages.FR  # Default language

Dictionary: dict = {  # Dictionary of all the words used in the application
    "fr": {
        "title": "Jeu de la vie",
        "init": "Réinitialiser",
        "start": "Démarrer",
        "stop": "Arrêter",
        "patterns": {
            "None": "Aucun",
            "Glider": "Planeur",
            "Blinker": "Clignotant",
            "Circle": "Cercle",
            "Vertical": "Vertical",
            "Horizontal": "Horizontal",
            "square": "Carré",
            "Full": "Total",
            "Checkerboard": "Damier",
            "Random": "Aléatoire"
        }
    },
    "en": {
        "title": "Game of Life",
        "init": "Reset",
        "start": "Start",
        "stop": "Stop",
        "pattern": "None",
        "patterns": {
            "None": "None",
            "Glider": "Glider",
            "Blinker": "Blinker",
            "Circle": "Circle",
            "Vertical": "Vertical",
            "Horizontal": "Horizontal",
            "square": "Square",
            "Full": "Full",
            "Checkerboard": "Checkerboard",
            "Random": "Random"
        }
    }
}


class GameOfLife:
    """
    Game of life class
    """
    Wait_Time: int = 0  # Time between each generation
    Language: Languages  # Language of the application
    master: tk.Tk  # Main window
    grid: np.ndarray  # Grid of the game
    canvas: tk.Canvas  # Canvas of the grid
    label_wait: tk.Label  # Label of the wait time
    label_count: tk.Label  # Label of the generation count
    label_data: tk.Label
    running: bool  # Is the animation running
    dimh: int = 0
    dimw: int = 0
    nh: int = 50
    nw: int = 50

    def __init__(self, lang: Languages) -> None:
        """
        Constructor of the class
        :param lang: The language of the application
        """

        self.Language = lang
        self.master = tk.Tk()
        self.master.title(Dictionary[self.Language.value]["title"])

        self.N = 50
        self.grid = np.zeros((self.nh, self.nw), dtype=int)
        self.create_widgets(width=500, height=500)

    def create_widgets(self, width: int = 500, height: int = 500) -> None:
        """
        Create the widgets of the application
        :param width:
        :param height:
        :return: None
        """
        # Create a menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # Add a menu item
        menu_bar.add_command(label=Dictionary[self.Language.value]["init"], command=self.init_grid)
        menu_bar.add_command(label=Dictionary[self.Language.value]["start"], command=self.start_animation)
        menu_bar.add_command(label=Dictionary[self.Language.value]["stop"], command=self.stop_animation)

        # Create a Patterns menu
        pattern_menu = tk.Menu(menu_bar, tearoff=0)
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["None"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["None"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["Glider"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["Glider"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["Blinker"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["Blinker"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["Circle"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["Circle"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["Vertical"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["Vertical"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["Horizontal"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["Horizontal"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["square"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["square"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["Full"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["Full"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["Checkerboard"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["Checkerboard"]))
        pattern_menu.add_command(label=Dictionary[self.Language.value]["patterns"]["Random"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.Language.value]["patterns"]["Random"]))

        # Add the Patterns menu to the menu bar
        menu_bar.add_cascade(label="Patterns", menu=pattern_menu)

        # Create a wait between generations menu
        wait_between_generations = tk.Menu(menu_bar, tearoff=0)
        wait_between_generations.add_command(label="0 ms", command=lambda: self.select_wait(0))
        wait_between_generations.add_command(label="10 ms", command=lambda: self.select_wait(10))
        wait_between_generations.add_command(label="25 ms", command=lambda: self.select_wait(25))
        wait_between_generations.add_command(label="50 ms", command=lambda: self.select_wait(50))
        wait_between_generations.add_command(label="100 ms", command=lambda: self.select_wait(100))
        wait_between_generations.add_command(label="250 ms", command=lambda: self.select_wait(250))
        wait_between_generations.add_command(label="500 ms", command=lambda: self.select_wait(500))
        wait_between_generations.add_command(label="1000 ms", command=lambda: self.select_wait(1000))

        # Add the wait between generations menu to the menu bar
        menu_bar.add_cascade(label="Wait between generations", menu=wait_between_generations)

        # Create a wait between generations menu
        dimcontrolh = tk.Menu(menu_bar, tearoff=0)
        dimcontrolh.add_command(label="+1", command=lambda: self.change_dim("h", "+", 10))
        dimcontrolh.add_command(label="+10", command=lambda: self.change_dim("h", "+", 100))
        dimcontrolh.add_command(label="+100", command=lambda: self.change_dim("h", "+", 1000))
        dimcontrolh.add_command(label="-1", command=lambda: self.change_dim("h", "-", 10))
        dimcontrolh.add_command(label="-10", command=lambda: self.change_dim("h", "-", 100))
        dimcontrolh.add_command(label="-100", command=lambda: self.change_dim("h", "-", 1000))

        # add height/wild control
        menu_bar.add_cascade(label="dim h", menu=dimcontrolh)

        # Create a wait between generations menu
        dimcontrolw = tk.Menu(menu_bar, tearoff=0)
        dimcontrolw.add_command(label="+1", command=lambda: self.change_dim("w", "+", 10))
        dimcontrolw.add_command(label="+10", command=lambda: self.change_dim("w", "+", 100))
        dimcontrolw.add_command(label="+100", command=lambda: self.change_dim("w", "+", 1000))
        dimcontrolw.add_command(label="-1", command=lambda: self.change_dim("w", "-", 10))
        dimcontrolw.add_command(label="-10", command=lambda: self.change_dim("w", "-", 100))
        dimcontrolw.add_command(label="-100", command=lambda: self.change_dim("w", "-", 1000))

        # add height/wild control
        menu_bar.add_cascade(label="dim w", menu=dimcontrolw)

        # Create a canvas
        self.canvas = tk.Canvas(self.master, width=width, height=height, bg="white", borderwidth=1, relief="groove")
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.toggle_cell)

        self.dimh = height
        self.dimw = width

        # print Count of alive cells
        self.label_count = tk.Label(self.master, text="Count of alive cells : " + str(self.count_alive_cells()))
        self.label_count.pack()

        # print time wait between generations
        self.label_wait = tk.Label(self.master, text="Wait between generations : " + str(self.Wait_Time) + " ms")
        self.label_wait.pack()

        # print the wild/height of the interface
        self.label_data = tk.Label(self.master, text="dim: " + str(self.dimh) + "/" + str(self.dimw) + " case: " + str(
            self.nh) + "*" + str(self.nw))
        self.label_data.pack()

    def init_grid(self) -> None:
        """
        Initialize the grid
        :return: None
        """
        self.grid = np.zeros((self.nh, self.nw), dtype=int)
        self.draw_grid()
        self.update_count()

    def start_animation(self) -> None:
        """
        Start the animation
        :return: None
        """
        self.running = True
        self.master.after(self.dimh)
        while self.running:
            self.update_count()
            self.master.after(self.Wait_Time)
            self.simulate_generation()
            self.draw_grid()
            self.master.update()

    def stop_animation(self) -> None:
        """
        Stop the animation
        :return: None
        """
        self.running = False
        self.update_count()

    def simulate_generation(self) -> None:
        """
        Simulate a generation
        :return: None
        """
        new_grid = np.zeros((self.nh, self.nw), dtype=int)
        for i in range(self.nh):
            for j in range(self.nw):
                # Compter le nombre de voisins vivants
                nb_neighbors = np.sum(self.grid[max(0, i - 1):min(self.nh, i + 2), max(0, j - 1):min(self.nw, j + 2)]) \
                               - self.grid[i, j]
                # Appliquer les règles du jeu de la vie
                if self.grid[i, j] == 1 and nb_neighbors in [2, 3]:
                    new_grid[i, j] = 1
                elif self.grid[i, j] == 0 and nb_neighbors == 3:
                    new_grid[i, j] = 1
        self.grid = new_grid

    def toggle_cell(self, event: tk.Event) -> None:
        """
        Toggle the state of a cell
        :param event: Event
        :return: None
        """
        row = int(event.y / 10)
        col = int(event.x / 10)
        self.grid[row, col] = 1 - self.grid[row, col]
        self.draw_grid()

    def draw_grid(self) -> None:
        """
        Draw the grid
        :return: None
        """
        self.canvas.delete(tk.ALL)
        for i in range(self.nh):
            for j in range(self.nw):
                if self.grid[i, j] == 1:
                    self.canvas.create_rectangle(j * 10, i * 10, j * 10 + 10, i * 10 + 10, fill='black')

    def select_pattern(self, pattern: str) -> None:
        """
        Select a pattern
        :param pattern: the pattern
        :return: None
        """
        self.init_grid()
        if pattern == Dictionary[self.Language.value]["patterns"]["Glider"]:
            # Glider in the upper right corner that moves down
            self.grid[0, 1] = 1
            self.grid[1, 2] = 1
            self.grid[2, 0:3] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Blinker"]:
            # Blinker
            if rd.randint(0, 1) == 0:
                self.grid[4:4 + 3, 4] = 1
            else:
                self.grid[4, 4:4 + 3] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Checkerboard"]:
            # Checkerboard
            self.grid[::2, ::2] = 1
            self.grid[1::2, 1::2] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Random"]:
            # Random
            self.grid = np.random.randint(0, 2, (self.nh, self.nw))
        elif pattern == Dictionary[self.Language.value]["patterns"]["Circle"]:
            # Circle
            self.grid = np.zeros((self.nh, self.nw), dtype=int)
            for i in range(self.nh):
                for j in range(self.nw):
                    if (i - self.N / 2) ** 2 + (j - self.N / 2) ** 2 < (self.N / 2) ** 2:
                        self.grid[i, j] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Horizontal"]:
            # Horizontal
            self.grid = np.zeros((self.nh, self.nw), dtype=int)
            self.grid[0, :] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Vertical"]:
            # Vertical
            self.grid = np.zeros((self.nh, self.nw), dtype=int)
            self.grid[:, 0] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["square"]:
            # Diagonal from top left to bottom right corner to bottom left to top right corner
            self.grid = np.zeros((self.nh, self.nw), dtype=int)
            self.grid[0, :] = 1
            self.grid[:, 0] = 1
            self.grid[:, -1] = 1
            self.grid[-1, :] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Full"]:
            # Full cells
            self.grid = np.ones((self.nh, self.nw), dtype=int)
        elif pattern == Dictionary[self.Language.value]["patterns"]["None"]:
            # None
            pass
        else:
            # None
            pass
        self.draw_grid()
        self.update_count()

    def count_alive_cells(self) -> int:
        """
        Count the number of alive cells
        :return: Number of alive cells
        """
        return int(np.sum(self.grid))

    def update_count(self) -> None:
        """
        Update the count of alive cells
        :return: None
        """
        self.label_count.config(text="Count of alive cells : " + str(self.count_alive_cells()))

    def select_wait(self, wait: int) -> None:
        """
        Select the wait time between generations
        :param wait: Wait time
        :return: None
        """
        self.Wait_Time = wait
        self.label_wait.config(text="Wait between generations : " + str(self.Wait_Time) + " ms")

    def show(self):
        """
        Show the window
        :return: None
        """
        self.master.mainloop()

    def change_dim(self, target: str, action: str, length: int) -> None:
        """
        Change the dimension of the grid
        :param target: the target to change
        :param action: the action to do
        :param length: the length to add or remove
        :return: None
        """
        if target == "h":
            out = self.dimh
            out2 = self.nh
            if length != -1:
                if action == "+":
                    out = self.dimh + length
                    out2 = int(self.nh + (length / 10))
                elif action == "-":
                    out = self.dimh - length
                    out2 = int(self.nh - (length / 10))
                else:
                    out = length
            self.dimh = out
            self.nh = out2
            self.canvas.config(height=self.dimh)
        if target == "w":
            out = self.dimw
            out2 = self.nw
            if length != -1:
                if action == "+":
                    out = self.dimw + length
                    out2 = int(self.nw + (length / 10))
                elif action == "-":
                    out = self.dimw - length
                    out2 = int(self.nw - (length / 10))
                else:
                    out = length
            self.dimw = out
            self.nw = out2
            self.canvas.config(width=self.dimw)
        self.init_grid()
        self.label_data.config(
            text="dim: " + str(self.dimh) + "/" + str(self.dimw) + " case: " + str(self.nh) + "*" + str(self.nw))


if __name__ == '__main__':
    # get the language of the system
    if locale.getdefaultlocale()[0] in ["fr_FR", "fr_BE", "fr_CA", "fr_CH", "fr_LU"]:
        Language_Appli = Languages.FR
    else:
        Language_Appli = Languages.EN

    game = GameOfLife(Language_Appli)
    game.show()
