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
if plekken()>1:
    print('er zijn nog',plekken(),'plaatsen beschikbaar')
elif plekken()== 0:
    print('er zijn geen plaatsen beschikbaar')
elif plekken() == 1:
    print('er is nog 1 plaats beschikbaar')
