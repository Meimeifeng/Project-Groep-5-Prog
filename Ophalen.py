import os, random, string
import pynma #importeert de API
import sqlite3

def fietsnr():
    global Fietsnr
    Fietsnr = int(input('wat is je fietsnr '))

    con = sqlite3.connect("fietsgegevens.db")
    cur = con.cursor()
    plek = cur.execute('SELECT Fietsnr, Pleknr FROM Keywords')
    for a in plek:
        global pleknr
        pleknr = a[0]
        fietsnr = a[1]
        if fietsnr == Fietsnr:
            gen()
            break
    else:
        print('dit fietsnr komt niet voor in uw code ')
        fietsnr()


def naam():
    con = sqlite3.connect("persoonsgegevens.db")
    cur = con.cursor()
    cur.execute('SELECT fietsnr, voornaam, tussenvoegsel, achternaam FROM Keywords')
    x = cur.fetchall()
    global Fietsnr

    for y in x:
        if Fietsnr == int(y[0]):
            global naam
            naam = (y[1],y[2],y[3])
            break


def gen():#generator
    length = 6
    chars = string.ascii_uppercase + string.digits
    random.seed = (os.urandom(1024))
    global verificatiecode
    verificatiecode = (''.join(random.choice(chars) for i in range(length)))

    print("Uw fietsnummer:", Fietsnr)
    print("Verificatie code verzenden...")

    print("Verificatie code verzonden!")


def verzenden():
    p = pynma.PyNMA("e1e405e067b7d0080552d39362dd255a19b6faae969871f4") #is de koppeling aan de mobiel DE CODE TUSSEN AANHALINGS TEKENS MOET U VERANDEREN ZOALS STAAT IN DE HANDLIJDING!!!
    global naam
    application=('naam') #naam mobiel
    event=( "Notificeren ophalen fiets") #welk event
    global verificatiecode
    description=("Uw random code: " + verificatiecode) #tekst
    p.push(application, event, description,) #daadwerkelijke push


def check():
    verificatie = input("Wat is uw verificatie code? ")
    global verificatiecode
    if verificatie == verificatiecode:
        print("Uw fiets is klaar om opgehaald te worden!")
        Bezet = 'Nee'
        Datum = '-'
        Fietsnr = 0
        con = sqlite3.connect("fietsgegevens.db")
        cur = con.cursor()
        cur.execute("""UPDATE Keywords SET  Fietsnr = ?, Bezet = ?, Datum = ? WHERE Pleknr = ?""", (Fietsnr, Bezet, Datum, pleknr))
        con.commit()
        con.close()
        quit
    else:
        print("Foutieve code")
        check()

fietsnr()
check()



