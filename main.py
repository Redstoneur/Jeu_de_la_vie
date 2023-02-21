import tkinter as tk
import numpy as np


class GameOfLife:
    master: tk.Tk
    N: int
    grid: np.ndarray
    canvas: tk.Canvas
    init_button: tk.Button
    start_button: tk.Button
    stop_button: tk.Button
    pattern_menu: tk.OptionMenu
    running: bool

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.N = 50
        self.grid = np.zeros((self.N, self.N), dtype=int)
        self.create_widgets(width=500, height=500)

    def create_widgets(self, width: int = 500, height: int = 500) -> None:
        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.toggle_cell)

        self.init_button = tk.Button(self.master, text='Réinitialiser', command=self.init_grid)
        self.init_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.start_button = tk.Button(self.master, text='Démarrer', command=self.start_animation)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(self.master, text='Arrêter', command=self.stop_animation)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.pattern_menu = tk.OptionMenu(self.master, tk.StringVar(), 'Aucun', 'Planeur', 'Clignotant',
                                          'Navire spatial léger', 'Full', 'Damier', 'Random',
                                          command=self.select_pattern)
        self.pattern_menu.pack(side=tk.LEFT, padx=10, pady=10)

    def init_grid(self) -> None:
        self.grid = np.zeros((self.N, self.N), dtype=int)
        self.draw_grid()

    def start_animation(self) -> None:
        self.running = True
        while self.running:
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
        if pattern == 'Planeur':
            # planeur dans le coin supérieur gauche qui se déplace vers le bas
            self.grid[0, 1] = 1
            self.grid[1, 2] = 1
            self.grid[2, 0:3] = 1
        elif pattern == 'Clignotant':
            # clignotant dans le coin supérieur droit
            self.grid[1:3, 1] = 1
            self.grid[1:3, 2] = 1
        elif pattern == 'Navire spatial léger':
            # navire spatial léger dans le coin supérieur droit qui se déplace vers le bas
            # TODO: à compléter
            pass
        elif pattern == 'Damier':
            self.grid[::2, ::2] = 1
            self.grid[1::2, 1::2] = 1
        elif pattern == 'Random':
            self.grid = np.random.randint(0, 2, (self.N, self.N))
        elif pattern == 'Full':
            self.grid = np.ones((self.N, self.N), dtype=int)
        elif pattern == 'Aucun':
            pass
        self.draw_grid()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Jeu de la vie')
    game = GameOfLife(root)
    root.mainloop()
