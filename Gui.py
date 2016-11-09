#Temp Gui
from tkinter import *
root = Tk()

label = Label(master=root,
                text='Welkom bij de NS fietsenstalling',
                background='yellow',
                foreground='blue',
                font=('Helvetica', 16, 'bold'),
                anchor=N,
                width=30,
                height=8,)
label.pack()

button1 = Button(master=root, text='Nieuwe fiets registeren', background='yellow', foreground='blue')
button1.place(x=130, y=50)
button2 = Button(master=root, text='Stallen', background='yellow', foreground='blue')
button2.place(x=165, y=85)
button3 = Button(master=root, text='Informatie opvragen', background='yellow', foreground='blue')
button3.place(x=130, y=120)


root.mainloop()
