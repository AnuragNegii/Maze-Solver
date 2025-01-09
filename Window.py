

from tkinter import Tk, BOTH, Canvas



class window:
    def __init__(self, width, height) -> None:
        self.root_widget = Tk() 
        self.root_widget.title("Maze-Solver")
        self.canvas = Canvas(self.root_widget, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) :
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fillcolour="black"):
        line.draw(self.canvas, fillcolour)

    def close(self):
        self.window_running = False 


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fillcolour):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y ,fill= fillcolour, width=2)

