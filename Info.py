import sqlite3
print('1: informatie over de fietsen in de stalling')


def plekken():    #aantal vrije kluizen
    con = sqlite3.connect('persoonsgegevens.db')                       #maakt verbinding met sqlite3 en de database
    cur = con.cursor()
    cur.execute('SELECT * FROM KEYWORDS')                               #selecteert alle informatie uit de database
    x = cur.fetchall()                                                  #koppelt de lijst uit de database aan x
    nietbeschikbaar = len(x)
    plaatsen = 12                                                       #verander dit nummer om het aantal plekken te veranderen
    beschikbaar = plaatsen - nietbeschikbaar

    return(int(beschikbaar))

try:
    nummer = int(input('geef het nummer van uw keuze '))
except:
    print('kies uit 1 t/m 5')

if nummer == 1:
    if plekken()>1:
        print('er zijn nog',plekken(),'plaatsen beschikbaar')
    elif plekken()== 0:
        print('er zijn geen plaatsen beschikbaar')
    elif plekken() == 1:
        print('er is nog 1 plaats beschikbaar')

    con = sqlite3.connect("fietsgegevens.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM Keywords')
    a, b, c, d = 'Plaats', 'Fietsnummer', 'Bezet', 'De fiets staat er sinds'
    print('{0:6} {1:6}  {2:3}  {3:6}'.format(a, b, c, d))
    for x in cur:
        print('{0:3} {1:6}          {2:6} {3:6}'.format(x[0], x[1], x[2], x[3]))
