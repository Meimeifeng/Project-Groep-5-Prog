import sqlite3
def plekken():    #aantal vrije kluizen
    con = sqlite3.connect('persoonsgegevens.db')                       #maakt verbinding met sqlite3 en de database
    cur = con.cursor()
    cur.execute('SELECT * FROM KEYWORDS')                               #selecteert alle informatie uit de database
    x = cur.fetchall()                                                  #koppelt de lijst uit de database aan x
    nietbeschikbaar = len(x)
    plaatsen = 12                                                       #verander dit nummer om het aantal plekken te veranderen
    beschikbaar = plaatsen - nietbeschikbaar

    return(int(beschikbaar))


def ophalen():
    while True:
        con = sqlite3.connect("fietsgegevens.db")
        cur = con.cursor()
        cur.execute('SELECT pleknr, bezet, fietsnr FROM KEYWORDS')
        x = cur.fetchall()
        Fietsnr = input('wat is jou fietsnummer ')
        wachtwoord = input('wat is jou code ')
        plek = input('op welke plek stond jou fiets ')
        for y in x:
            print(y)
            if y[3] == int(Fietsnr)   :
                goedefiets = True
        con = sqlite3.connect('persoonsgegevens1.db')                       #maakt verbinding met sqlite3 en de database
        cur = con.cursor()
        cur.execute('SELECT Fietsnr, code FROM KEYWORDS')                               #selecteert alle informatie uit de database
        a = cur.fetchall()
        for b in a:
            print(b)
            if b[0] == int(Fietsnr) and b[1] == int(wachtwoord)and goedefiets == True:
                print('ok')
                Plek = y[0]
                Bezet = 'Nee'
                Datum = '-'
                con = sqlite3.connect("fietsgegevens.db")
                cur = con.cursor()
                cur.execute("""UPDATE Keywords SET  Fietsnr = ?, Bezet = ?, Datum = ? WHERE Pleknr = ?""", (Fietsnr, Bezet, Datum, Plek))
                con.commit()
                con.close()
                quit
            else:
                print('Dit was niet de goede combinatie code. Probeer opnieuw')



ophalen()
