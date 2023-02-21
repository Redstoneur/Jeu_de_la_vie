import locale
import enum
import tkinter as tk
import numpy as np


class Languages(enum.Enum):
    FR = "fr"
    EN = "en"

    def __str__(self) -> str:
        return self.value


Language_Appli = Languages.FR

Dictionary: dict = {
    "fr": {
        "title": "Jeu de la vie",
        "init": "Réinitialiser",
        "start": "Démarrer",
        "stop": "Arrêter",
        "patterns": {
            "None": "Aucun",
            "Glider": "Planeur",
            "Blinker": "Clignotant",
            "Lightweight spaceship": "Navire spatial léger",
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
            "Lightweight spaceship": "Lightweight spaceship",
            "Full": "Full",
            "Checkerboard": "Checkerboard",
            "Random": "Random"
        }
    }
}


class GameOfLife:
    Wait_Time: int = 0
    Language: Languages
    master: tk.Tk
    N: int
    grid: np.ndarray
    canvas: tk.Canvas
    init_button: tk.Button
    start_button: tk.Button
    stop_button: tk.Button
    pattern_menu: tk.OptionMenu
    wait_between_generations: tk.OptionMenu
    running: bool

    def __init__(self, lang: Languages) -> None:

        self.Language = lang

        self.master = tk.Tk()
        self.master.title(Dictionary[self.Language.value]["title"])

        self.N = 50
        self.grid = np.zeros((self.N, self.N), dtype=int)
        self.create_widgets(width=500, height=500)

    def create_widgets(self, width: int = 500, height: int = 500) -> None:
        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.toggle_cell)

        self.init_button = tk.Button(self.master, text=Dictionary[self.Language.value]["init"], command=self.init_grid)
        self.init_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.start_button = tk.Button(self.master, text=Dictionary[self.Language.value]["start"],
                                      command=self.start_animation)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(self.master, text=Dictionary[self.Language.value]["stop"],
                                     command=self.stop_animation)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.pattern_menu = tk.OptionMenu(self.master, tk.StringVar(),
                                          Dictionary[self.Language.value]["patterns"]["None"],
                                          Dictionary[self.Language.value]["patterns"]["Glider"],
                                          Dictionary[self.Language.value]["patterns"]["Blinker"],
                                          Dictionary[self.Language.value]["patterns"]["Lightweight spaceship"],
                                          Dictionary[self.Language.value]["patterns"]["Full"],
                                          Dictionary[self.Language.value]["patterns"]["Checkerboard"],
                                          Dictionary[self.Language.value]["patterns"]["Random"],
                                          command=self.select_pattern)
        self.pattern_menu.pack(side=tk.LEFT, padx=10, pady=10)

        self.wait_between_generations = tk.OptionMenu(self.master, tk.IntVar(),
                                                      0, 10, 25, 50, 100, 250, 500, 1000,
                                                      command=self.select_wait)
        self.wait_between_generations.pack(side=tk.LEFT, padx=10, pady=10)

    def init_grid(self) -> None:
        self.grid = np.zeros((self.N, self.N), dtype=int)
        self.draw_grid()

    def start_animation(self) -> None:
        self.running = True
        while self.running:
            self.master.after(self.Wait_Time)
            self.simulate_generation()
            self.draw_grid()
            self.master.update()

    def stop_animation(self) -> None:
        self.running = False

    def simulate_generation(self) -> None:
        new_grid = np.zeros((self.N, self.N), dtype=int)
        for i in range(self.N):
            for j in range(self.N):
                # Compter le nombre de voisins vivants
                nb_neighbors = np.sum(self.grid[max(0, i - 1):min(self.N, i + 2), max(0, j - 1):min(self.N, j + 2)]) - \
                               self.grid[i, j]
                # Appliquer les règles du jeu de la vie
                if self.grid[i, j] == 1 and nb_neighbors in [2, 3]:
                    new_grid[i, j] = 1
                elif self.grid[i, j] == 0 and nb_neighbors == 3:
                    new_grid[i, j] = 1
        self.grid = new_grid

    def toggle_cell(self, event: tk.Event) -> None:
        row = int(event.y / 10)
        col = int(event.x / 10)
        self.grid[row, col] = 1 - self.grid[row, col]
        self.draw_grid()

    def draw_grid(self) -> None:
        self.canvas.delete(tk.ALL)
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i, j] == 1:
                    self.canvas.create_rectangle(j * 10, i * 10, j * 10 + 10, i * 10 + 10, fill='black')

    def select_pattern(self, pattern: str) -> None:
        self.init_grid()

        if pattern == Dictionary[self.Language.value]["patterns"]["Glider"]:
            # Glider in the upper right corner that moves down
            self.grid[0, 1] = 1
            self.grid[1, 2] = 1
            self.grid[2, 0:3] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Blinker"]:
            # Blinker
            self.grid[1:3, 1] = 1
            self.grid[1:3, 2] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Lightweight spaceship"]:
            # Lightweight spaceship in the upper right corner that moves down
            # TODO: to complete
            pass
        elif pattern == Dictionary[self.Language.value]["patterns"]["Checkerboard"]:
            # Checkerboard
            self.grid[::2, ::2] = 1
            self.grid[1::2, 1::2] = 1
        elif pattern == Dictionary[self.Language.value]["patterns"]["Random"]:
            # Random
            self.grid = np.random.randint(0, 2, (self.N, self.N))
        elif pattern == Dictionary[self.Language.value]["patterns"]["Full"]:
            # Full cells
            self.grid = np.ones((self.N, self.N), dtype=int)
        elif pattern == Dictionary[self.Language.value]["patterns"]["None"]:
            # None
            pass
        else:
            # None
            pass

        self.draw_grid()

    def select_wait(self, wait: int) -> None:
        self.Wait_Time = wait

    def show(self):
        self.master.mainloop()


if __name__ == '__main__':
    # get the language of the system
    if locale.getdefaultlocale()[0] in ["fr_FR", "fr_BE", "fr_CA", "fr_CH", "fr_LU"]:
        Language_Appli = Languages.FR
    else:
        Language_Appli = Languages.EN

    game = GameOfLife(Language_Appli)
    game.show()
