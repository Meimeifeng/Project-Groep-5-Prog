import csv
nietbeschikbaar = 0
file = open('fietsen.csv', 'r', newline='')
tekst = csv.reader(file)
for regel in tekst:
    nietbeschikbaar = nietbeschikbaar + 1
beschikbaar = 12 - nietbeschikbaar

if beschikbaar > 0:
    print('er zijn '+ str(beschikbaar)+ 'plekken beschikbaar')
else:
    print('er zijn geen plekken meer vrij')
