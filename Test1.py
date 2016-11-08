#test2
            while True:
                Fietsnr = input('wat is jou fietsnummer ')
                wachtwoord = input('wat is jou code ')
                plek = input('op welke plek stond jou fiets ')
                joufiets = False
                con = sqlite3.connect('persoonsgegevens1.db')                       #maakt verbinding met sqlite3 en de database
                cur = con.cursor()
                cur.execute('SELECT Fietsnr, code FROM KEYWORDS')                               #selecteert alle informatie uit de database
                a = cur.fetchall()
                for b in a:

                    if b[0] == int(Fietsnr) and b[1] == int(wachtwoord) :
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

                print('Dit was niet de goede combinatie code. Probeer opnieuw')
