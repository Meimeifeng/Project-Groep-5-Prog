# je krijgt een plek en een code. op die plek zet je je fiets neer en de code onthoud je voor als je fiets komt ophalen ook krijgt je fiets
# een nummer deze heb je met je code nodig om je fiets te hale
# ook moeten je persoonsgegevens worden gevraagt en dit word aan je fiets gelinkt en fiets moet een fietsnr krijgen dit moet nog!!!!!

import csv
import random
from collections import defaultdict
import os
#3

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

def Plekken():    #aantal vrije kluizen
    nietbeschikbaar = 0
    file = open('fietsen.csv', 'r', newline='')
    tekst = csv.reader(file)
    for regel in tekst:
        nietbeschikbaar = nietbeschikbaar + 1
    beschikbaar = 12 - nietbeschikbaar
    return(int(beschikbaar))

def www():
    rand1 = random.choice('123456789')
    rand2 = random.choice('123456789')
    rand3 = random.choice('123456789')
    rand4 = random.choice('123456789')
    ww = str(rand1+rand2+rand3+rand4)
    return(ww)


def Registreren():
    text = open('fietsen.csv')
    tekst = csv.reader(text,delimiter=';')

    for regel in tekst:
        for (a, b) in enumerate(regel):
            columns[a].append(b)
    if int(Plekken()) > 0:
        for x in range(1,13):
            plekkenbezet = columns[0]
            if str(x) not in plekkenbezet:
                openkluis = x
                ww = www()
                message1 = Label(master=root,
                    text='Registreren \n\n\nDe plek nummer van uw fiets is: {}\n Uw ophaal code is: {}'.format(openkluis,ww),
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 20, 'bold'),
                    anchor=N,
                    width=35,
                    height=11,)
                message1.pack()
                button1 = Button(master=root, text='Menu', font=('Helvetica', 20, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=close)
                button1.place(x=40, y=300)

                text1 = open('fietsen.csv', 'a', newline='')
                tekst1 = csv.writer(text1, delimiter=';')
                tekst1.writerow((openkluis, ww))
                break
    else:
        message2 = Label(master=root,
                    text='Registreren \n\n\n Er zijn geen plekken meer beschikbaar',
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 20, 'bold'),
                    anchor=N,
                    width=35,
                    height=11,)
        message2.pack()
        button2 = Button(master=root, text='Menu', font=('Helvetica', 20, 'bold'), borderwidth=0, background='yellow', foreground='blue', command=close)
        button2.place(x=40, y=300)

Registreren()
root.mainloop()
