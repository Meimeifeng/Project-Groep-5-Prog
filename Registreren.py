# je krijgt een plek en een code. op die plek zet je je fiets neer en de code onthoud je voor als je fiets komt ophalen ook krijgt je fiets
# een nummer deze heb je met je code nodig om je fiets te hale
# ook moeten je persoonsgegevens worden gevraagt en dit word aan je fiets gelinkt en fiets moet een fietsnr krijgen dit moet nog!!!!!


import sqlite3


def vragen():
    con = sqlite3.connect('persoonsgegevens.db')                       #maakt verbinding met sqlite3 en de database
    cur = con.cursor()
    cur.execute('SELECT * FROM KEYWORDS')                               #selecteert alle informatie uit de database
    x = cur.fetchall()                                                  #koppelt de lijst uit de database aan x
    fietsnr = len(x)+1                                                  #geeft fietsnr de waarde hoelang x is plus 1
    print('om uw fiets te registreren moet u een aantal vragen beandwoorden.\n')
    voornaam = str(input('wat is uw voornaam? '))
    tussenvoegsel = str(input('wat is uw tussenvoegsel?(heeft u die niet voer een streep in) '))
    achternaam = str(input('wat is uw achternaam? '))
    geboortedatum = str(input('wat is uw geboorte datum? bijvoorbeeld 07-03-1987 '))
    adres = str(input('wat is uw adres en huisnummer? '))
    code = 'NULL'

    print('uw naam is:', voornaam, tussenvoegsel, achternaam, '\nu bent geboren op', geboortedatum, '"\nuw adres is', adres)
    bevesteging = input('kloppen deze gegevens? vul in: ja/nee ')       #vraagt de persoon of zijn/haar gegevens kloppen.

    if bevesteging  == 'ja':                                            #geeft de gegevens door aan de database
        cur.execute("""INSERT INTO Keywords VALUES(?, ?, ?, ?, ?, ?, ?)""", (voornaam, tussenvoegsel, achternaam, geboortedatum, adres, fietsnr, code))
        con.commit()
        con.close()
        print('u heeft u sucessvol geregistreerd.')
        print('uw fietsnummer is',fietsnr, '\nondhoud dit nummer goed. deze heeft u nodig als u uw fiets wilt stallen of ophalen')
    else:
        print('u heeft aangegeven dat uw gegevens niet kloppen. u kunt deze nu opieuw invoeren.')
        vragen()

vragen()
