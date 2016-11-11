import os
import sqlite3

def plekken():    #aantal vrije kluizen
    con = sqlite3.connect('persoonsgegevens.db')                       #maakt verbinding met sqlite3 en de database
    cur = con.cursor()
    cur.execute('SELECT fietsnr FROM KEYWORDS WHERE fietsnr != 0')     #selecteert alle informatie uit de database
    x = cur.fetchall()                                                  #koppelt de lijst uit de database aan x
    nietbeschikbaar = len(x)
    plaatsen = 12                                                       #verander dit nummer om het aantal plekken te veranderen
    beschikbaar = plaatsen - nietbeschikbaar
    return(beschikbaar)



while True:

    print('welkom bij deze fietsenstalling. er zijn nog', plekken(),'plekken vrij.')

    print('\n1: Je fiets voor de eerste keer registreren\n2: Je fiets stallen\n3: Je fiets ophalen\n4: Informatie van je fiets of van de stalling\n5: Ik wil stoppen')
    try:
        nummer = int(input('geef het nummer van uw keuze '))
    except:
        print('kies uit 1 t/m 5')
        continue
    if nummer == 1:
        os.system('Registreren.py')
    elif nummer == 2:
        os.system('Stallen.py')
    elif nummer == 3:
        os.system('Ophalen.py')
    elif nummer == 4:
        os.system('Info.py')
    elif nummer == 5:
        break
    else:
        print('kies uit 1 t/m 6')
