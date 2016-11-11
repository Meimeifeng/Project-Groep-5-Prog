
import sqlite3
con = sqlite3.connect('persoonsgegevens1.db')
cur = con.cursor()
#cur.execute("""CREATE TABLE Keywords (Url text, Word text, Freq int)""")
#cur.execute("""CREATE TABLE Keywords ( voornaam text, tussenvoegsel text, achternaam text, geboortedatum text, adres text, fietsnr int, code int)""")
#cur.execute("""INSERT INTO Keywords VALUES('Wessel','', 'Henkes', '29-9-1999', 'voorhavendijk 1', 1, 2468)""")

#voornaam, tussenvoegsel, achternaam, geboortedatum, adres, fietsnr, code = 'Wessel','', 'Henkes', '29-9-1999', 'voorhavendijk 1', 1, 2468
#cur.execute("""INSERT INTO Keywords VALUES(?, ?, ?, ?, ?, ?, ?)""",(voornaam, tussenvoegsel, achternaam, geboortedatum, adres, fietsnr, code))
#cur.execute("""INSERT INTO Keywords VALUES('one.html', 'Beijing', 3)""")
#url, word, freq = 'one.html', 'Paris', 5
#uur.execute("""INSERT INTO KEYWORDS VALUES(?, ?, ?)""", (url, word, freq))
cur.execute('SELECT * FROM KEYWORDS')
x = cur.fetchall()
print(x)
y = x[0]
y = str(y)
y = y.replace('(', '')
y = y.replace(')', '')
y = y.replace("'", '' )
q = y.strip()
q = q.split(',')
a = q[2]
b = a.strip()
print(b)
