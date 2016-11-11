import sqlite3
print('1: Informatie over de fietsen in de stalling\n2: uw persoonsgegevens opvragen\n3: waar staat uw fiets in de stalling')

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
    print('kies uit 1 of 2')

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
elif nummer == 2:
    con = sqlite3.connect("persoonsgegevens.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM Keywords')
    voornaam, tussenvoegsel, achternaam, geboortedatum, adres, fietsnr, = 'voornaam', 'tussenvoegsel', 'achternaam', 'geboortedatum', 'adres', 'fietsnr'
    print('{0:6}   {1:6}    {2:3}    {3:6}    {4:6}            {5:6}'.format(voornaam, tussenvoegsel, achternaam, geboortedatum, adres, fietsnr,))
    for x in cur:
        print('{0:6}        {1:6}        {2:12}  {3:12}     {4:15}  {5:6}'.format(x[0], x[1], x[2], x[3], x[4], x[5]))

elif nummer == 3:
    con = sqlite3.connect("fietsgegevens.db")
    cur = con.cursor()
    fietsnr = input('wat is uw fietsnummer')
    cur.execute('SELECT fietsnr, pleknr FROM Keywords')
    for x in cur:
        if x[0] == int(fietsnr):
            print('uw fiets staat op plek', x[1])
