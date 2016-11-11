
import sqlite3
con = sqlite3.connect('persoonsgegevens.db')
cur = con.cursor()

cur.execute("""CREATE TABLE Keywords ( voornaam text, tussenvoegsel text, achternaam text, geboortedatum text, adres text, fietsnr int, code int)""")
con.commit()
