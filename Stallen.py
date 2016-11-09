from tkinter import *
import sys
root = Tk()

def close():
    sys.exit()

message = Label(master=root,
                    text='Stallen \n\n\nDeze optie werkt nog niet',
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 20, 'bold'),
                    anchor=N,
                    width=35,
                    height=11,)
message.pack()
button1 = Button(master=root, text='Menu', font=('Helvetica', 20, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=close)
button1.place(x=40, y=300)

root.mainloop()
