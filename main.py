"""
Module to simulate the game of life
"""

import enum
import locale
import secrets
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
            "Blinker": "Clignotant",
            "Glider": "Planeur",
            "Glider_Generator": "Générateur de planeurs",
            "Circle": "Cercle",
            "Vertical": "Vertical",
            "Horizontal": "Horizontal",
            "square": "Carré",
            "Full": "Total",
            "Checkerboard": "Damier",
            "Random": "Aléatoire"
        },
        "Dim": {
            "Title": "Dimensions",
            "Height": "Hauteur",
            "Width": "Largeur",
            "Validate": "Valider",
            "Cancel": "Annuler",
            "Default": "Défaut",
            "MaxDim": "MaxDim",
            "change_dim": "Changer les dimensions"
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
            "Blinker": "Blinker",
            "Glider": "Glider",
            "Glider_Generator": "Glider generator",
            "Circle": "Circle",
            "Vertical": "Vertical",
            "Horizontal": "Horizontal",
            "square": "Square",
            "Full": "Full",
            "Checkerboard": "Checkerboard",
            "Random": "Random"
        },
        "Dim": {
            "Title": "Dimensions",
            "Height": "Height",
            "Width": "Width",
            "Validate": "Validate",
            "Cancel": "Cancel",
            "Default": "Default",
            "MaxDim": "MaxDim",
            "change_dim": "Change the dimensions"
        }
    }
}

Dimensions: dict = {
    "Interface": {
        "Height": 500,
        "Width": 500
    },
    "Interface_Default": {
        "Height": 500,
        "Width": 500
    },
    "Interface_Min": {
        "Height": 160,
        "Width": 370
    },
}


class DimensionsWindows(tk.Toplevel):
    """
    Dimensions of the windows
    """
    components_dim: int = 10  # Dimensions of the components
    language: Languages  # Language of the application
    text_area_height: tk.Text  # Text area height
    text_area_width: tk.Text  # Text area width

    def __init__(self, lang: Languages) -> None:
        """
        Constructor of the class
        """
        super().__init__()
        self.language = lang
        self.title(Dictionary[self.language.value]["Dim"]["Title"])
        self.create_widgets()
        self.resizable(False, False)

    def create_widgets(self) -> None:
        """
        Create the widgets of the application
        :return: None
        """

        row = 0
        column = 0

        label_1 = tk.Label(
            self, font=("Arial", 10),
            text=f"{Dictionary[self.language.value]['Dim']['Height']}"
        )
        label_1.grid(
            row=row, column=column, sticky="nsew"
        )

        column += 1

        self.text_area_height = tk.Text(self, height=1, width=1)
        self.text_area_height.insert(tk.END, Dimensions["Interface"]["Height"])
        self.text_area_height.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        label_2 = tk.Label(
            self, font=("Arial", 10),
            text=f"* {Dictionary[self.language.value]['Dim']['Width']}"
        )
        label_2.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        self.text_area_width = tk.Text(self, height=1, width=1)
        self.text_area_width.insert(tk.END, Dimensions["Interface"]["Width"])
        self.text_area_width.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        row += 1
        column = 0

        default = tk.Button(
            self, command=self.default,
            text=f"{Dictionary[self.language.value]['Dim']['Default']}"
        )
        default.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        max_dim = tk.Button(
            self, command=self.max_dim,
            text=f"{Dictionary[self.language.value]['Dim']['MaxDim']}"
        )
        max_dim.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        validate = tk.Button(
            self, command=self.validate,
            text=f"{Dictionary[self.language.value]['Dim']['Validate']}"
        )
        validate.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

        column += 1

        cancel = tk.Button(
            self, command=self.cancel,
            text=f"{Dictionary[self.language.value]['Dim']['Cancel']}"
        )
        cancel.grid(
            row=row, column=column, sticky="nsew",
            padx=self.components_dim / 10,
            pady=self.components_dim / 10
        )

    def validate(self) -> None:
        """
        Validate the dimensions
        :return: None
        """
        try:
            Dimensions["Interface"]["Height"] = int(self.text_area_height.get("1.0", tk.END))
            Dimensions["Interface"]["Width"] = int(self.text_area_width.get("1.0", tk.END))
        except ValueError:
            pass
        self.destroy()

    def cancel(self) -> None:
        """
        Cancel the dimensions
        :return: None
        """
        self.destroy()

    def default(self) -> None:
        """
        Set the default dimensions
        :return: None
        """
        Dimensions["Interface"]["Height"] = Dimensions["Interface_Default"]["Height"]
        Dimensions["Interface"]["Width"] = Dimensions["Interface_Default"]["Width"]
        self.destroy()

    def max_dim(self) -> None:
        """
        Set the max dimensions
        :return: None
        """
        Dimensions["Interface"]["Height"] = self.winfo_screenheight()
        Dimensions["Interface"]["Width"] = self.winfo_screenwidth()
        self.destroy()


class GameOfLife:
    """
    Game of life class
    """
    wait_time: int = 0  # Time between each generation
    language: Languages  # Language of the application
    master: tk.Tk  # Main window
    grid: np.ndarray  # Grid of the game
    canvas: tk.Canvas  # Canvas of the grid
    label_wait: tk.Label  # Label of the wait time
    label_count: tk.Label  # Label of the generation count
    label_data: tk.Label  # Label of the data
    button_dim: tk.Button  # Button to change the dimensions
    running: bool  # Is the animation running
    dim_h: int = 0
    dim_w: int = 0
    nh: int = 50
    nw: int = 50

    def __init__(self, lang: Languages) -> None:
        """
        Constructor of the class
        :param lang: The language of the application
        """

        self.language = lang
        self.master = tk.Tk()
        self.master.title(Dictionary[self.language.value]["title"])

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
        menu_bar.add_command(label=Dictionary[self.language.value]["init"], command=self.init_grid)
        menu_bar.add_command(
            label=Dictionary[self.language.value]["start"], command=self.start_animation
        )
        menu_bar.add_command(
            label=Dictionary[self.language.value]["stop"], command=self.stop_animation
        )
        menu_bar.add_command(
            label=Dictionary[self.language.value]['Dim']['change_dim'],
            command=self.change_dim_window
        )

        # Create a Patterns menu
        pattern_menu = tk.Menu(menu_bar, tearoff=0)
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["None"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["None"]))
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["Blinker"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["Blinker"]))
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["Glider"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["Glider"]))
        pattern_menu.add_command(
            label=Dictionary[self.language.value]["patterns"]["Glider_Generator"],
            command=lambda: self.select_pattern(
                Dictionary[self.language.value]["patterns"]["Glider_Generator"]
            )
        )
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["Circle"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["Circle"]))
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["Vertical"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["Vertical"]))
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["Horizontal"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["Horizontal"]))
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["square"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["square"]))
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["Full"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["Full"]))
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["Checkerboard"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["Checkerboard"]))
        pattern_menu.add_command(label=Dictionary[self.language.value]["patterns"]["Random"],
                                 command=lambda: self.select_pattern(
                                     Dictionary[self.language.value]["patterns"]["Random"]))

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
        wait_between_generations.add_command(
            label="1000 ms", command=lambda: self.select_wait(1000)
        )

        # Add the wait between generations menu to the menu bar
        menu_bar.add_cascade(label="Wait between generations", menu=wait_between_generations)

        # Create a canvas
        self.canvas = tk.Canvas(
            self.master, width=width, height=height,
            bg="white", borderwidth=1, relief="groove"
        )
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.toggle_cell)

        # Lier le changement de forme du pointeur à l'événement de survol du canevas
        self.canvas.bind("<Enter>", self.change_cursor_enter)
        self.canvas.bind("<Leave>", self.change_cursor_leave)

        self.dim_h = height
        self.dim_w = width

        # print Count of alive cells
        self.label_count = tk.Label(
            self.master, text="Count of alive cells : " + str(self.count_alive_cells())
        )
        self.label_count.pack()

        # print time wait between generations
        self.label_wait = tk.Label(
            self.master, text="Wait between generations : " + str(self.wait_time) + " ms"
        )
        self.label_wait.pack()

        # print the wild/height of the interface
        self.label_data = tk.Label(
            self.master,
            text="dim: " + str(self.dim_h) + "/" + str(self.dim_w) +
                 " case: " + str(self.nh) + "*" + str(self.nw)
        )
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
        self.master.after(self.dim_h)
        while self.running:
            self.update_count()
            self.master.after(self.wait_time)
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
                nb_neighbors = np.sum(
                    self.grid[max(0, i - 1):min(self.nh, i + 2), max(0, j - 1):min(self.nw, j + 2)]
                ) - self.grid[i, j]
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
                    self.canvas.create_rectangle(
                        j * 10, i * 10, j * 10 + 10, i * 10 + 10,
                        fill='black'
                    )

    def select_pattern(self, pattern: str) -> None:
        """
        Select a pattern
        :param pattern: the pattern
        :return: None
        """
        self.init_grid()
        if pattern == Dictionary[self.language.value]["patterns"]["Blinker"]:
            # Blinker
            self.pattern_blinker()
        elif pattern == Dictionary[self.language.value]["patterns"]["Glider"]:
            # Glider
            self.pattern_glider()
        elif pattern == Dictionary[self.language.value]["patterns"]["Glider_Generator"]:
            # Glider generator
            self.pattern_glider_generator()
        elif pattern == Dictionary[self.language.value]["patterns"]["Checkerboard"]:
            # Checkerboard
            self.pattern_Checkerboard()
        elif pattern == Dictionary[self.language.value]["patterns"]["Random"]:
            # Random
            self.pattern_Random()
        elif pattern == Dictionary[self.language.value]["patterns"]["Circle"]:
            # Circle
            self.pattern_circle()
        elif pattern == Dictionary[self.language.value]["patterns"]["Horizontal"]:
            # Horizontal
            self.pattern_horizontal()
        elif pattern == Dictionary[self.language.value]["patterns"]["Vertical"]:
            # Vertical
            self.pattern_vertical()
        elif pattern == Dictionary[self.language.value]["patterns"]["square"]:
            # Diagonal from top left to bottom right corner to bottom left to top right corner
            self.pattern_square()
        elif pattern == Dictionary[self.language.value]["patterns"]["Full"]:
            # Full cells
            self.pattern_full()
        elif pattern == Dictionary[self.language.value]["patterns"]["None"]:
            # None
            pass
        else:
            # None
            pass
        self.draw_grid()
        self.update_count()

    def pattern_blinker(self):
        """
        Pattern Blinker
        """
        init: int = 1
        if secrets.randbelow(2) == 0:
            self.grid[init:init + 3, init] = 1
        else:
            self.grid[init, init:init + 3] = 1

    def pattern_glider(self):
        """
        Pattern Glider in the upper right corner that moves down
        """
        init: int = 1
        self.grid[init, init + 1] = 1
        self.grid[init + 1, init + 2] = 1
        self.grid[init + 2, init:init + 3] = 1

    def pattern_glider_generator(self):
        """
        Pattern Glider Generator
        """
        mage: int = 1

        col: int = 1

        li: int = 5 + mage
        self.grid[li:li + 2, col] = 1

        col += 1

        li = 5 + mage
        self.grid[li:li + 2, col] = 1

        col += 9

        li = 5 + mage
        self.grid[li:li + 3, col] = 1

        col += 1

        li = 4 + mage
        self.grid[li, col] = 1
        li += 4
        self.grid[li, col] = 1

        col += 1

        li = 3 + mage
        self.grid[li, col] = 1
        li += 6
        self.grid[li, col] = 1

        col += 1

        li = 3 + mage
        self.grid[li, col] = 1
        li += 6
        self.grid[li, col] = 1

        col += 1

        li = 6 + mage
        self.grid[li, col] = 1

        col += 1

        li = 4 + mage
        self.grid[li, col] = 1
        li += 4
        self.grid[li, col] = 1

        col += 1

        li = 5 + mage
        self.grid[li:li + 3, col] = 1

        col += 1

        li = 6 + mage
        self.grid[li, col] = 1

        col += 3

        li = 3 + mage
        self.grid[li:li + 3, col] = 1

        col += 1

        li = 3 + mage
        self.grid[li:li + 3, col] = 1

        col += 1

        li = 2 + mage
        self.grid[li, col] = 1
        li += 4
        self.grid[li, col] = 1

        col += 2

        li = 1 + mage
        self.grid[li:li + 2, col] = 1
        li += 5
        self.grid[li:li + 2, col] = 1

        col += 10

        li = 3 + mage
        self.grid[li:li + 2, col] = 1

        col += 1

        li = 3 + mage
        self.grid[li:li + 2, col] = 1

    def pattern_Checkerboard(self):
        """
        Pattern Checkerboard
        """
        self.grid[::2, ::2] = 1
        self.grid[1::2, 1::2] = 1

    def pattern_Random(self):
        """
        Pattern Random
        """
        self.grid = np.random.randint(0, 2, (self.nh, self.nw))

    def pattern_circle(self):
        """
        Pattern Circle
        """
        self.grid = np.zeros((self.nh, self.nw), dtype=int)
        radius = min(self.nh, self.nw) // 4
        center_i, center_j = self.nh // 2, self.nw // 2

        for i in range(self.nh):
            for j in range(self.nw):
                if (i - center_i) ** 2 + (j - center_j) ** 2 < radius ** 2:
                    self.grid[i, j] = 1

    def pattern_horizontal(self):
        """
        Pattern Horizontal
        """
        self.grid = np.zeros((self.nh, self.nw), dtype=int)
        self.grid[0, :] = 1

    def pattern_vertical(self):
        """
        Pattern Vertical
        """
        self.grid = np.zeros((self.nh, self.nw), dtype=int)
        self.grid[:, 0] = 1

    def pattern_square(self):
        """
        Pattern Square
        """
        self.grid = np.zeros((self.nh, self.nw), dtype=int)
        self.grid[0, :] = 1
        self.grid[:, 0] = 1
        self.grid[:, -1] = 1
        self.grid[-1, :] = 1

    def pattern_full(self):
        """
        Pattern Full
        """
        self.grid = np.ones((self.nh, self.nw), dtype=int)


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
        self.wait_time = wait
        self.label_wait.config(text="Wait between generations : " + str(self.wait_time) + " ms")

    def show(self) -> None:
        """
        Show the window
        :return: None
        """
        self.master.mainloop()

    def change_dim_window(self) -> None:
        """
        Change the dimension by opening a new window
        :return: None
        """
        if (Dimensions["Interface"]["Height"] != self.dim_h or
                Dimensions["Interface"]["Width"] != self.dim_w):
            Dimensions["Interface"]["Height"] = self.dim_h
            Dimensions["Interface"]["Width"] = self.dim_w

        # Create an instance of Dimensions_Windows
        dimensions_window = DimensionsWindows(lang=self.language)
        dimensions_window.wait_window()

        if (Dimensions["Interface"]["Height"] != self.dim_h or
                Dimensions["Interface"]["Width"] != self.dim_w):
            if Dimensions["Interface"]["Height"] < Dimensions["Interface_Min"]["Height"]:
                Dimensions["Interface"]["Height"] = Dimensions["Interface_Min"]["Height"]
            if Dimensions["Interface"]["Width"] < Dimensions["Interface_Min"]["Width"]:
                Dimensions["Interface"]["Width"] = Dimensions["Interface_Min"]["Width"]

            if Dimensions["Interface"]["Height"] % 10 != 0:
                # arrondir au multiple de 10 le plus proche
                self.dim_h = int(Dimensions["Interface"]["Height"] / 10) * 10
            else:
                self.dim_h = Dimensions["Interface"]["Height"]
            if Dimensions["Interface"]["Width"] % 10 != 0:
                # arrondir au multiple de 10 le plus proche
                self.dim_w = int(Dimensions["Interface"]["Width"] / 10) * 10
            else:
                self.dim_w = Dimensions["Interface"]["Width"]

            self.nh = int(self.dim_h / 10)
            self.nw = int(self.dim_w / 10)
            self.canvas.config(height=self.dim_h, width=self.dim_w)
            self.init_grid()
            self.label_data.config(
                text="dim: " + str(self.dim_h) + "/" + str(self.dim_w) +
                     " case: " + str(self.nh) + "*" + str(self.nw))

    # noinspection PyUnusedLocal
    def change_cursor_enter(self, event: tk.Event) -> None:
        """
        Change the cursor shape
        @param event: Event
        @return: None
        """
        # Changer la forme du pointeur en "cross" lorsque la souris entre dans le canevas
        event.widget.config(cursor="plus")
        self.canvas.config(cursor="plus")

    # noinspection PyUnusedLocal
    def change_cursor_leave(self, event: tk.Event) -> None:
        """
        Change the cursor shape
        @param event: Event
        @return: None
        """
        # Changer la forme du pointeur en "arrow" lorsque la souris quitte le canevas
        event.widget.config(cursor="arrow")
        self.canvas.config(cursor="arrow")


if __name__ == '__main__':
    # get the language of the system
    if locale.getdefaultlocale()[0] in ["fr_FR", "fr_BE", "fr_CA", "fr_CH", "fr_LU"]:
        Language_Appli = Languages.FR
    else:
        Language_Appli = Languages.EN

    game = GameOfLife(Language_Appli)
    game.show()
