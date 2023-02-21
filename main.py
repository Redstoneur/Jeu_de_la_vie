import tkinter as tk
import numpy as np


class GameOfLife:
    def __init__(self, master):
        self.master = master
        self.N = 50
        self.grid = np.zeros((self.N, self.N), dtype=int)
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.toggle_cell)
        self.init_button = tk.Button(self.master, text='Initialiser', command=self.init_grid)
        self.init_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.start_button = tk.Button(self.master, text='Démarrer', command=self.start_animation)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.stop_button = tk.Button(self.master, text='Arrêter', command=self.stop_animation)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

    def init_grid(self):
        self.grid = np.zeros((self.N, self.N), dtype=int)
        self.draw_grid()

    def start_animation(self):
        self.running = True
        while self.running:
            self.simulate_generation()
            self.draw_grid()
            self.master.update()

    def stop_animation(self):
        self.running = False

    def simulate_generation(self):
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
        # attendre 100 ms
        self.master.after(20)
        self.grid = new_grid

    def toggle_cell(self, event):
        row = int(event.y / 10)
        col = int(event.x / 10)
        self.grid[row, col] = 1 - self.grid[row, col]
        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete(tk.ALL)
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i, j] == 1:
                    self.canvas.create_rectangle(j * 10, i * 10, j * 10 + 10, i * 10 + 10, fill='black')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Jeu de la vie')
    game = GameOfLife(root)
    root.mainloop()
