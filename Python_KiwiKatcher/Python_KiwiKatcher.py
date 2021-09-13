from itertools import cycle
from random import randrange
from tkinter import Tk, Canvas, messagebox, font

canvas_width = 800
canvas_height = 400

win = Tk()
 
c = Canvas(win, width = canvas_width, height = canvas_height, background = 'deep sky blue')
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill = 'sea green', width=0)


win.mainloop()