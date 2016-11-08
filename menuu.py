import os
while True:
    print('\n1: Je fiets voor de eerste keer registreren\n2: Je fiets stallen\n3: Je fiets ophalen\n4: Informatie van je fiets of van de stalling\n5: Antal vrije plaatsen\n6: Ik wil stoppen')
    try:
        nummer = int(input('geef het nummer van uw keuze '))
    except:
        print('kies uit 1 t/m 5')
        continue
    if nummer == 1:
        os.system('Registreren.py')
    elif nummer == 2:
        os.system('Stallen.py')
    elif nummer == 3:
        os.system('Ophalen.py')
    elif nummer == 4:
        os.system('Info.py')
    elif nummer == 5:
        os.system('Plekken.py')
    elif nummer == 6:
        break
    else:
        print('kies uit 1 t/m 6')
