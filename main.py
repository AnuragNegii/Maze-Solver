from Window import window 
from Maze import Maze


def main():
    num_rows = 10
    num_cols = 10
    margin = 20
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win ,1)
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()   

if __name__ == "__main__":
    main()
