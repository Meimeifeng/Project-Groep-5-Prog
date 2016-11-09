import csv
import random
from collections import defaultdict
from tkinter import *
import sys
root = Tk()

def close():
    sys.exit()

columns = defaultdict(list)
text = open('fietsen.csv')
tekst = csv.reader(text, delimiter=';')
for regel in tekst:
    for (a, b) in enumerate(regel):
        columns[a].append(b)
kluizengebruikt = columns[0]
for y in kluizengebruikt:
    kluizengebruikt[kluizengebruikt.index(y)] = int(y)

root.configure(background='yellow')


button1 = Button(master=root, text='Menu', font=('Helvetica', 20, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=close)
button1.pack(anchor=NW)

message = Label(master=root,
                    text='Fiets ophalen',
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 20, 'bold'),
                    anchor=N,
                    width=35,)
message.pack()
fietscd1 = Label(master=root,
                    text='\nVul uw fiets code in: ',
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 16, 'bold'),
                    width=46,)
fietscd1.pack()
fietscd2 = Entry(root, bd=5, background='blue', foreground='yellow',)
fietscd2.pack()
fietsnum1 = Label(master=root,
                    text='\nVul uw fiets plaats nummer in: ',
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 16, 'bold'),
                    width=46,)
fietsnum1.pack()
fietsnum2 = Entry(root, bd=5, background='blue', foreground='yellow',)
fietsnum2.pack()

def Ophalen():    #kluis openen
    text = open('fietsen.csv')
    tekst = csv.reader(text, delimiter=';')
    for regel in tekst:
        for (a, b) in enumerate(regel):
            columns[a].append(b)
    codes = columns[1]
    plek = columns[0]
    x = True
    fietsnr = fietsnum2.get()
    wachtwoord = fietscd2.get()
    while x == True:
        if wachtwoord in codes:
            for i in codes:
                if i == wachtwoord:
                    fiets1 = Label(master=root,
                        text='\nUw kluisnummer {} word geopend'.format(plek[codes.index(i)]),
                        background='yellow',
                        foreground='blue',
                        font=('Helvetica', 16, 'bold'),
                        width=46,)
                    fiets1.pack()
                    x = False
                    break
        else:
            fiets2 = Label(master=root,
                        text='\nOnbekende combinatie, probeer het a.u.b. opnieuw',
                        background='yellow',
                        foreground='blue',
                        font=('Helvetica', 16, 'bold'),
                        width=46,)
            fiets2.pack()
            break


submit = Button(root, text ="\nControleren", font=('Helvetica', 15, 'bold'), borderwidth=0, background='yellow', foreground='blue', command = Ophalen)
submit.pack()


root.mainloop()

Ophalen()
