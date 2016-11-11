# je krijgt een plek en een code. op die plek zet je je fiets neer en de code onthoud je voor als je fiets komt ophalen ook krijgt je fiets
# een nummer deze heb je met je code nodig om je fiets te hale
# ook moeten je persoonsgegevens worden gevraagt en dit word aan je fiets gelinkt en fiets moet een fietsnr krijgen dit moet nog!!!!!


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
    code = 'NULL'

    print('uw naam is:', voornaam, tussenvoegsel, achternaam, ', u bent geboren op', geboortedatum, ', uw adres is', adres, 'en de code om uw fiets op te halen is:', code, 'uw fietsnummer is',fietsnr)
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
