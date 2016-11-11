import sqlite3
print('1: Informatie over de fietsen in de stalling\n2: uw persoonsgegevens opvragen en waar uw fiets in de stalling staat')



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
    fietsnr = input('wat is uw fietsnummer')
    cur.execute('')
    for x in cur
    print()
