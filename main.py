
from Window import window, line, point
 
def main():
    win= window(800, 600)
    create_line = line(point(30, 40), point(50, 80))
    create_line2= line(point(90, 70), point(85, 10))
    create_line3= line(point(60, 100), point(50, 75))
    create_line.draw(win.canvas, fillcolour="red")
    create_line2.draw(win.canvas, fillcolour="red")
    create_line3.draw(win.canvas, fillcolour="red")
    win.wait_for_close()
    

if __name__ == "__main__":
    main()
    
