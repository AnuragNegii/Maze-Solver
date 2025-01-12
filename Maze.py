from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, canvas=None,seed=None):
        self.seed = seed
        if seed != None:
            self.seed = random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.canvas = canvas
        self.cells = []
        self.create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def create_cells(self):
        for col in range(self.num_cols):
            col_cells = []
            for row in range(self.num_rows):
                col_cells.append(Cell(self.canvas))
            self.cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cells(i, j)
                
    def _draw_cells(self, i, j):
        if self.canvas is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.canvas is None:
            return
        self.canvas.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
        self.cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cells(self.num_cols - 1, self.num_rows - 1)               

    def _break_walls_r(self, i ,j):
        self.cells[i][j].visited = True
        while True:
            to_visit = []
#left
            if i > 0 and self.cells[i -1][j].visited == False:
                to_visit.append((i-1, j))
#right
            if i < self.num_cols - 1 and self.cells[i+1][j].visited == False:
                to_visit.append((i+1, j))
#up
            if j > 0 and self.cells[i][j - 1].visited == False:
                to_visit.append((i, j-1))
#down
            if j < self.num_rows - 1 and self.cells[i][j+1].visited == False:
                to_visit.append((i, j+1))

            if len(to_visit) == 0:
                self._draw_cells(i, j)
                return

            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]

            #right
            if next_index[0] == i+ 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
            #left
            if next_index[0] == i -1:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
            #up
            if next_index[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
            #down
            if next_index[1] == j+1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False

            self._break_walls_r(next_index[0], next_index[1])

