from tkinter import *


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a > b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L

        L +=1

def hcf(a,b):
    H = a if a < b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H -= 1


win = Tk()
win.geometry('500x300')
win.title('Smart Pugger')
win.configure(bg ='lightskyblue')

l1 = Label(win, text = 'Me smart calculator', width=20, padx=3)
l1.place(x=150,y=10)
l2 = Label(win, text = 'Me name Pugger', padx=3)
l2.place(x=180,y=40)
l3 = Label(win, text = 'Me help you how ?', padx=3)
l3.place(x=176,y=130)


textin = StringVar()
e1 = Entry(win, width=30, textvariable=textin)
e1.place(x=100,y=160)

b1 =Button(win, text = 'Just this')
b1.place(x=210, y=200)

list = Listbox(win, width=20, height=3)
list.place(x=150, y= 230)