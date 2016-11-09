import os
from tkinter import *
import sys

root = Tk()

def plekken():
    os.system('plekken.py')

def close():
    sys.exit()

while True:
    label = Label(master=root,
            text='Informatie opvragen',
            background='yellow',
            foreground='blue',
            font=('Helvetica', 20, 'bold'),
            anchor=N,
            width=35,
            height=11,)
    label.pack()

    button1 = Button(master=root, text='Beschikbare plekken', font=('Helvetica', 16, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=plekken)
    button1.place(x=40, y=50)
    button2 = Button(master=root, text='Menu', font=('Helvetica', 16, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=close)
    button2.place(x=40, y=300)

    root.mainloop()
