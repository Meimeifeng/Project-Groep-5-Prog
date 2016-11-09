import csv
from tkinter import *
import sys

root = Tk()

def close():
    sys.exit()

nietbeschikbaar = 0
file = open('fietsen.csv', 'r', newline='')
tekst = csv.reader(file)
for regel in tekst:
    nietbeschikbaar = nietbeschikbaar + 1
beschikbaar = 12 - nietbeschikbaar

if beschikbaar > 0:
    message1 = Label(master=root,
                    text='Beschikbare plekken \n\n\nEr zijn nog {} plekken beschikbaar'.format(beschikbaar),
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 20, 'bold'),
                    anchor=N,
                    width=35,
                    height=11,)
    message1.pack()
    button1 = Button(master=root, text='Menu', font=('Helvetica', 20, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=close)
    button1.place(x=40, y=300)
else:
    message2 = Label(master=root,
                    text='Beschikbare plekken \n\n\nEr zijn momenteel geen plekken meer vrij',
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 20, 'bold'),
                    anchor=N,
                    width=35,
                    height=11,)
    message2.pack()
    button2 = Button(master=root, text='Menu', font=('Helvetica', 20, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=close)
    button2.place(x=40, y=300)


root.mainloop()
