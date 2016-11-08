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
    if int(d()) > 0:
        for x in range(1,13):
            kluizenbezet = columns[0]
            if str(x) not in kluizenbezet:
                openkluis = x
                ww = www()
                text1 = open('fietsen.csv', 'a', newline='')
                tekst1 = csv.writer(text1, delimiter=';')
                tekst1.writerow((openkluis, ww))
                print('jouw kluisje is nummer '+ str(openkluis) + ' en de code voor de kluis is ' + str(ww))
                break
    else:
        print('er zijn geen kluisjes meer beschikbaar')

def Stallen():    #kluis openen
    text = open('fietsen.csv')
    tekst = csv.reader(text, delimiter=';')
    for regel in tekst:
        for (a, b) in enumerate(regel):
            columns[a].append(b)
    codes = columns[1]
    kluisnummers = columns[0]
    x = True
    while x == True:
        wachtwoord = input('wat is je code')
        if wachtwoord in codes:
            for i in codes:
                if i == wachtwoord:

                    print('je kluisnummer is '+ str(kluisnummers[codes.index(i)]) + 'wordt geopend')
                    x = False
                    break
        else:
            print('dit is geen goede code')

def Ophalen():    #ik ben klaar met mijn kluis
    print('deze optie werkt nog niet')

def Plekken():    #aantal vrije kluizen
    nietbeschikbaar = 0
    file = open('fietsen.csv', 'r', newline='')
    tekst = csv.reader(file)
    for regel in tekst:
        nietbeschikbaar = nietbeschikbaar + 1
    beschikbaar = 12 - nietbeschikbaar
    return(int(beschikbaar))
def Info():
    print('er zijn ' + str(plekken()) + ' kluisjes vrij')

while True:
    print('\n1: Je fiets voor de eerste keer registreren\n2: Je fiets stallen\n3: Je fiets ophalen\n4: Informatie van je fiets ophalen\n5: Antal vrije plaatsen\n6: Ik wil stoppen')
    try:
        nummer = int(input('geef het nummer van uw keuze '))
    except:
        print('kies uit 1 t/m 5')
        continue
    if nummer == 1:
        Registreren()
    elif nummer == 2:
        Stallen()
    elif nummer == 3:
        Ophalen()
    elif nummer == 4:
        Info()
    elif nummer == 5:
        Plekken()
    elif nummer == 6:
        break
    else:
        print('kies uit 1 t/m 6')
