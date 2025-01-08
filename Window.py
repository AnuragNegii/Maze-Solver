

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

    def close(self):
        self.window_running = False 


