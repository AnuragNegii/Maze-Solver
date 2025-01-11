
from Window import Line, Point 


class Cell:
    def __init__(self, canvas= None) -> None:
        self.has_left_wall = True 
        self.has_right_wall= True 
        self.has_top_wall = True 
        self.has_bottom_wall = True 
        self._x1 = None 
        self._x2= None
        self._y1= None 
        self._y2 = None 
        self.canvas = canvas 
   
    def draw(self, x1, y1, x2, y2) -> None:
        if self.canvas is None:
            return 
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall :
            line = Line(Point(x1, y1), Point(x1, y2))
            self.canvas.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.canvas.draw_line(line, "white")
        if self.has_right_wall :
            line = Line(Point(x2, y1), Point(x2, y2))
            self.canvas.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.canvas.draw_line(line, "white")
        if self.has_top_wall :
            line = Line(Point(x1, y1), Point(x2, y1))
            self.canvas.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.canvas.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.canvas.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.canvas.draw_line(line, "white")        

    def draw_move(self, to_cell, undo=False):
        mid_point_self = [(self.x1 +self.x2)/2 , (self.y1 +self.y2)/2]
        to_cell_mid_point= [(to_cell.x1 + to_cell.x2)/2 , (to_cell.y1 +to_cell.y2)/2]
        fill_color = "red" 
        if undo:
            fill_color = "grey" 
        line = Line(Point(mid_point_self[0], mid_point_self[1]), Point(to_cell_mid_point[0], to_cell_mid_point[1]))
        if self.canvas != None:
            self.canvas.draw_line(line, fill_color)             
