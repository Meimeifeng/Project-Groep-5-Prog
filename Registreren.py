import csv
import random
from collections import defaultdict
import os

columns = defaultdict(list)
text = open('fietsen.csv')
tekst = csv.reader(text, delimiter=';')
for regel in tekst:
    for (a, b) in enumerate(regel):
        columns[a].append(b)
kluizengebruikt = columns[0]
for y in kluizengebruikt:
    kluizengebruikt[kluizengebruikt.index(y)] = int(y)


def www():
    rand1 = random.choice('123456789')
    rand2 = random.choice('123456789')
    rand3 = random.choice('123456789')
    rand4 = random.choice('123456789')
    ww = str(rand1+rand2+rand3+rand4)
    return(ww)


def Registreren():              # je krijgt een plek en een code. op die plek zet je je fiets neer en de code onthoud je voor als je fiets komt ophalen ook krijgt je fiets een nummer deze heb je met je code nodig om je fiets te halen
    text = open('fietsen.csv')
    tekst = csv.reader(text,delimiter=';')
    for regel in tekst:
        for (a, b) in enumerate(regel):
            columns[a].append(b)
    if int(os.system('Plekken.py')) > 0:
        for x in range(1,13):
            plekkenbezet = columns[0]
            if str(x) not in plekkenbezet:
                openkluis = x
                ww = www()
                text1 = open('fietsen.csv', 'a', newline='')
                tekst1 = csv.writer(text1, delimiter=';')
                tekst1.writerow((openkluis, ww))
                print('jouw plek is nummer '+ str(openkluis) + ' en de code voor het ophalen is: ' + str(ww))
                break
    else:
        print('er zijn geen plekken meer beschikbaar')
Registreren()
