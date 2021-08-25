from tkinter import Tk, NORMAL, HIDDEN, Canvas

win = Tk()

c = Canvas(win, width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0)

c.body_color ='SkyBlue'

body = c.create_oval(35,20,365,350,outline=c.body_color, fill=c.body_color)
foot_left = c.create_oval(65 ,320,145,360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250 ,320,330,360, outline=c.body_color, fill=c.body_color)

ear-left = c.create_polygon(75,80,75,10,165,70,outline=c.body_color, fill=c.body_color)
ear-right = c.create_polygon(255,45,325,10,320,70,outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(130,110,160,170, outline=c.white, fill=c.white)
c.pack()

win.mainloop()