import os
from tkinter import *
import sys

root = Tk()


def registreren():
    os.system('Registreren.py')

def stallen():
    os.system('Stallen.py')

def ophalen():
    os.system('Ophalen.py')

def info():
    os.system('Info.py')

def plekken():
    os.system('Plekken.py')

def close():
    sys.exit()



while True:
    label = Label(master=root,
            text='Welkom bij de NS fietsenstalling',
            background='yellow',
            foreground='blue',
            font=('Helvetica', 20, 'bold'),
            anchor=N,
            width=35,
            height=11,)
    label.pack()

    button1 = Button(master=root, text='Nieuwe fiets registeren', font=('Helvetica', 16, 'bold'), borderwidth=0,  background='yellow', foreground='blue', command=registreren)
    button1.place(x=40, y=50)
    button2 = Button(master=root, text='Stallen', font=('Helvetica', 16, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=stallen)
    button2.place(x=40, y=95)
    button3 = Button(master=root, text='Fiets ophalen', font=('Helvetica', 16, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=ophalen)
    button3.place(x=40, y=140)
    button4 = Button(master=root, text='Informatie opvragen', font=('Helvetica', 16, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=info)
    button4.place(x=40, y=185)
    button5 = Button(master=root, text='Beschikbare plekken', font=('Helvetica', 16, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=plekken)
    button5.place(x=40, y=230)
    button6 = Button(master=root, text='Sluiten', font=('Helvetica', 16, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=close)
    button6.place(x=40, y=300)

    root.mainloop()
