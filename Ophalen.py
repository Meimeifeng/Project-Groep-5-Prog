import os, random, string
#import pynma #importeert de API
import sqlite3

def plekken():    #aantal vrije plekken
    con = sqlite3.connect('persoonsgegevens.db')                       #maakt verbinding met sqlite3 en de database
    cur = con.cursor()
    cur.execute('SELECT * FROM KEYWORDS')                               #selecteert alle informatie uit de database
    x = cur.fetchall()                                                  #koppelt de lijst uit de database aan x
    nietbeschikbaar = len(x)
    plaatsen = 12                                                       #verander dit nummer om het aantal plekken te veranderen
    beschikbaar = plaatsen - nietbeschikbaar

    return(int(beschikbaar))
# vraag om fietsnr
# stuur code
# check code

def ophalen():
    while True:
        pass
    #     con = sqlite3.connect("fietsgegevens.db")
    #      cur = con.cursor()
    #       cur.execute('SELECT pleknr, bezet, fietsnr FROM KEYWORDS')
    # x = cur.fetchall()
    #  Fietsnr = input('wat is jou fietsnummer ')
    #   wachtwoord = input('wat is jou code ')
    #    plek = input('op welke plek stond jou fiets ')
    #     for y in x:
    #          print(y)
    #           if y[3] == int(Fietsnr):
    #                goedefiets = True
    #   con = sqlite3.connect('persoonsgegevens.db')                       #maakt verbinding met sqlite3 en de database
    #  cur = con.cursor()
    # cur.execute('SELECT Fietsnr, code FROM KEYWORDS')                               #selecteert alle informatie uit de database
    #a = cur.fetchall()




    else:
        print('Dit was niet de goede combinatie code. Probeer opnieuw')


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


def gen():#generator
    length = 6
    chars = string.ascii_uppercase + string.digits
    random.seed = (os.urandom(1024))
    global verificatiecode
    verificatiecode = (''.join(random.choice(chars) for i in range(length)))

    print("Uw fietsnummer:", Fietsnr)
    print("Verificatie code verzenden...")
    print("Uw random code: ", verificatiecode)
    verzenden()
    print("Verificatie code verzonden!")


def verzenden():
    print('')
    #p = pynma.PyNMA( "e1e405e067b7d0080552d39362dd255a19b6faae969871f4") #is de koppeling aan de mobiel
    #application=("Mobiel klant") #naam mobiel
    #event=( "Notificeren ophalen fiets") #welk event
    #description=("Uw random code: " + global verificatiecode) #tekst
    #p.push(application, event, description,) #daadwerkelijke push

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



