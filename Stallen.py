import sqlite3
import datetime

def plekken():    #aantal vrije kluizen
    con = sqlite3.connect('persoonsgegevens.db')                       #maakt verbinding met sqlite3 en de database
    cur = con.cursor()
    cur.execute('SELECT * FROM KEYWORDS')                               #selecteert alle informatie uit de database
    x = cur.fetchall()                                                  #koppelt de lijst uit de database aan x
    nietbeschikbaar = len(x)
    plaatsen = 12                                                       #verander dit nummer om het aantal plekken te veranderen
    beschikbaar = plaatsen - nietbeschikbaar

    return(int(beschikbaar))

def Registreren():
    if plekken() > 0:
        Fietsnr = input('wat is jou fietsnummer ')
        con = sqlite3.connect("fietsgegevens.db")
        cur = con.cursor()

        cur.execute('SELECT pleknr, bezet FROM KEYWORDS')

        x = cur.fetchall()
        for y in x:
            Plek = y[0]
            Bezet = y[1]
            if Bezet == 'Nee':
                print('jouw plek is nummer ', str(Plek))
                Bezet = 'Ja'
                Datum = datetime.datetime.today().strftime("%a %d %b %Y, %H:%M:%S")
                con = sqlite3.connect("fietsgegevens.db")
                cur = con.cursor()
                cur.execute("""UPDATE Keywords SET  Fietsnr = ?, Bezet = ?, Datum = ? WHERE Pleknr = ?""", (Fietsnr, Bezet, Datum, Plek))
                con.commit()
                con.close()
                break
    else:
        print('er zijn geen plekken meer beschikbaar')


Registreren()
