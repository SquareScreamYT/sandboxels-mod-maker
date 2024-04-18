# Created by sqec aka SquareScreamYT
# https://youtube.com/@sqec
# Test of Falling Sand Game
# Very buggy

import customtkinter
import random

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

CELL_SIZE = 10
GRID_WIDTH = 60
GRID_HEIGHT = 40 

# Cell types
EMPTY = 0
SAND = 1
WATER = 2
WALL = 3

class FallingSandGame(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        # Create grid
        self.grid = [[EMPTY] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_tool = "sand"
        
        # GUI
        self.title("Falling Sand")
        self.geometry("480x350")
        self.resizable(False, False)
        
        # Toolbar
        toolbar = customtkinter.CTkFrame(self)
        toolbar.pack(side="top", fill="x")
        
        self.sand_button = customtkinter.CTkButton(toolbar, text="Sand", text_color="black", fg_color="yellow", hover_color="#cc0", command=self.set_sand)
        self.sand_button.pack(side="left")

        self.water_button = customtkinter.CTkButton(toolbar, text="Water", text_color="black", fg_color="blue", hover_color="darkblue", command=self.set_water)
        self.water_button.pack(side="left")

        self.wall_button = customtkinter.CTkButton(toolbar, text="Wall", text_color="black", fg_color="gray", hover_color="dimgray", command=self.set_wall)
        self.wall_button.pack(side="left")

        self.eraser_button = customtkinter.CTkButton(toolbar, text="Eraser", text_color="black", fg_color="white", hover_color="lightgray", command=self.set_erase)
        self.eraser_button.pack(side="left")

        # Canvas
        self.canvas = customtkinter.CTkCanvas(self, width=GRID_WIDTH*CELL_SIZE, height=GRID_HEIGHT*CELL_SIZE)
        self.canvas.pack(side="top", fill="both", expand=True)
        
        # Mouse events
        self.canvas.bind("<Button-1>", self.place_cell)
        self.canvas.bind("<B1-Motion>", self.place_cell)
        
        # Simulation loop
        self.simulate()
        
    def simulate(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT-1, -1, -1):
                cell = self.grid[y][x]
                if cell == SAND:
                    if y < GRID_HEIGHT-1 and self.grid[y+1][x] == EMPTY:
                        self.grid[y+1][x] = SAND
                        self.grid[y][x] = EMPTY
                    elif random.random() < 0.5 and y < GRID_HEIGHT-1 and x < GRID_WIDTH-1 and self.grid[y+1][x+1] == EMPTY:
                        self.grid[y+1][x+1] = SAND
                        self.grid[y][x] = EMPTY
                    elif y < GRID_HEIGHT-1 and x > 1 and self.grid[y+1][x-1] == EMPTY:
                        self.grid[y+1][x-1] = SAND
                        self.grid[y][x] = EMPTY
                    else:
                        pass
                elif cell == WATER:
                    if y < GRID_HEIGHT-1 and self.grid[y+1][x] == EMPTY:
                        self.grid[y+1][x] = WATER
                        self.grid[y][x] = EMPTY
                    elif random.random() < 0.5 and y < GRID_HEIGHT-1 and x < GRID_WIDTH-1 and self.grid[y+1][x+1] == EMPTY:
                        self.grid[y+1][x+1] = WATER
                        self.grid[y][x] = EMPTY
                    elif y < GRID_HEIGHT-1 and x > 1 and self.grid[y+1][x-1] == EMPTY:
                        self.grid[y+1][x-1] = WATER
                        self.grid[y][x] = EMPTY
                    elif random.random() < 0.5 and x < GRID_WIDTH-1 and self.grid[y][x+1] == EMPTY:
                        self.grid[y][x+1] = WATER
                        self.grid[y][x] = EMPTY
                    elif x > 1 and self.grid[y][x-1] == EMPTY:
                        self.grid[y][x-1] = WATER
                        self.grid[y][x] = EMPTY
                    else:
                        pass
                elif cell == WALL:
                    pass
        self.update()
        self.after(1, self.simulate)
            
    def update(self):
        self.canvas.delete("all")
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                cell = self.grid[y][x]
                if cell == SAND:
                    color = "#C2B280" 
                elif cell == WATER:
                    color = "#6193BC"
                elif cell == WALL:
                    color = "#aaaaaa"
                else:
                    color = "#000000"
                    
                self.canvas.create_rectangle(x*CELL_SIZE, y*CELL_SIZE, (x+1)*CELL_SIZE, (y+1)*CELL_SIZE, fill=color)
    
    def place_cell(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        if self.current_tool == "sand":
            self.grid[y][x] = SAND
        elif self.current_tool == "water":
            self.grid[y][x] = WATER
        elif self.current_tool == "wall":
            self.grid[y][x] = WALL
        elif self.current_tool == "erase":
            self.grid[y][x] = EMPTY
        
            
    def set_sand(self):
        self.current_tool = "sand"

    def set_water(self):
        self.current_tool = "water"
        
    def set_wall(self):
        self.current_tool = "wall"
        
    def set_erase(self):
        self.current_tool = "erase"
        
app = FallingSandGame()
app.mainloop()
