import sqlite3
con = sqlite3.connect("fietsgegevens.db")
cur = con.cursor()
con.commit()

3cur.execute("""CREATE TABLE Keywords (Pleknr int, fietsnr int, bezet text, datum text)""")
#cur.execute("""INSERT INTO Keywords VALUES(2, 0, "True","27/11/2018" )""")
#for x in range(0, 13):
#    pleknr, fietsnr, bezet, datum = x, 0, "Nee", "-"
#    cur.execute("""INSERT INTO Keywords VALUES(?, ?, ?, ?)""", (pleknr, fietsnr, bezet, datum))
#con.commit()
def test():
    print(x)
    y = x[0]
    y = str(y)
    y = y.replace('(', '')
    y = y.replace(')', '')
    y = y.replace("'", '' )
    q = y.strip()
    q = q.split(',')
    print(q)
    #a = q[2]
    #b = a.strip()
    #print(b)



cur.execute('SELECT * FROM Keywords')
for x in cur:
    print(x[0],x[1],x[2],x[3])

