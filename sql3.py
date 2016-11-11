import os, random, string
#import pynma #importeert de API

def gen():#generator
    length = 6
    chars = string.ascii_uppercase + string.digits
    random.seed = (os.urandom(1024))
    global verificatiecode
    verificatiecode = (''.join(random.choice(chars) for i in range(length)))

    print("Uw fietsnummer:", fietsnr)
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
    verificatie = input("Wat is uw verificatie code?")
    if verificatie == verificatiecode:
        print("Uw fiets is klaar om opgehaald te worden!")
    else:
        print("Foutieve code")

gen()
check()

print("end of code")


