import csv
import random
from collections import defaultdict

columns = defaultdict(list)
text = open('fietsen.csv')
tekst = csv.reader(text, delimiter=';')
for regel in tekst:
    for (a, b) in enumerate(regel):
        columns[a].append(b)
kluizengebruikt = columns[0]
for y in kluizengebruikt:
    kluizengebruikt[kluizengebruikt.index(y)] = int(y)



def Ophalen():    #kluis openen
    text = open('fietsen.csv')
    tekst = csv.reader(text, delimiter=';')
    for regel in tekst:
        for (a, b) in enumerate(regel):
            columns[a].append(b)
    codes = columns[1]
    plek = columns[0]
    x = True
    while x == True:

        wachtwoord = input('wat is je code')
        fietsnr = input('wat is het nummer van je fiets')
        if wachtwoord in codes:
            for i in codes:
                if i == wachtwoord:

                    print('je kluisnummer is '+ str(plek[codes.index(i)]) + 'wordt geopend')
                    x = False
                    break
        else:
            print('dit is geen goede code')
Ophalen()
