from tkinter import *

win = Tk()
win.geometry('500x300')
win.title('Smart Pugger')
win.configure(bg ='lightskyblue')

l1 = Label(win, text = 'Me smart calaculator', width =20, padx=3)
l1.place(x=150,y=10)
l2 = Label(win, text = 'Me name Pugger', padx=3)
l2.place(x=180,y=40)
l3 = Label(win, text = 'Me help you how ?', padx=3)
l3.place(x=176,y=130)


textin = StringVar()
e1 = Entry(win, width=300, textvariable=textin)
e1.place(x=100,y=160)