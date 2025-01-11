from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, canvas,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.canvas = canvas
        self.cells = []
        self.create_cells()

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
                

       
