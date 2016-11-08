# je krijgt een plek en een code. op die plek zet je je fiets neer en de code onthoud je voor als je fiets komt ophalen ook krijgt je fiets
# een nummer deze heb je met je code nodig om je fiets te hale
# ook moeten je persoonsgegevens worden gevraagt en dit word aan je fiets gelinkt en fiets moet een fietsnr krijgen dit moet nog!!!!!
#voornaam, tussenvoegsel, achternaam, geboortedatum, adres, code = 'Wessel','', 'Henkes', '29-9-1999', 'voorhavendijk 1', 2468

import sqlite3


def vragen():
    con = sqlite3.connect('persoonsgegevens1.db')                       #maakt verbinding met sqlite3 en de database
    cur = con.cursor()
    cur.execute('SELECT * FROM KEYWORDS')                               #selecteert alle informatie uit de database
    x = cur.fetchall()                                                  #koppelt de lijst uit de database aan x
    fietsnr = len(x)+1                                                  #geeft fietsnr de waarde hoelang x is plus 1
    print('om uw fiets te registreren moet u een aantal vragen beandwoorden.\n')
    voornaam = str(input('wat is uw voornaam? '))
    tussenvoegsel = str(input('wat is uw tussenvoegsel? '))
    achternaam = str(input('wat is uw achternaam? '))
    geboortedatum = str(input('wat is uw geboorte datum? '))
    adres = str(input('wat is uw adres? '))
    code = input('welke vier cijferige code wilt u gebruiken als u uw fiets komt ophalen? ')

    if len(str(code)) != 4:                                             #checkt of de code die is ingevuld ook echt 4 cijfers bevat en niet meer of minder
        print('deze code was niet goed ')
        code = input('welke vier cijferige code wilt u gebruiken als u uw fiets komt ophalen? ')

    print('uw naam is:', voornaam, tussenvoegsel, achternaam, ', u bent geboren op', geboortedatum, ', uw adres is', adres, 'en de code om uw fiets op te halen is:', code)
    bevesteging = input('kloppen deze gegevens? vul in: ja/nee ')       #vraagt de persoon of zijn/haar gegevens kloppen.

    if bevesteging  == 'ja':                                            #geeft de gegevens door aan de database
        cur.execute("""INSERT INTO Keywords VALUES(?, ?, ?, ?, ?, ?, ?)""", (voornaam, tussenvoegsel, achternaam, geboortedatum, adres, fietsnr, code))
        con.commit()
        con.close()
        print('u heeft u sucessvol geregistreerd.')
    else:
        print('u heeft aangegeven dat uw gegevens niet kloppen. u kunt deze nu opieuw invoeren.')
        vragen()

vragen()
