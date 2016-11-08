nietbeschikbaar = 0
file = open('fietsen.csv', 'r', newline='')
tekst = csv.reader(file)
for regel in tekst:
    nietbeschikbaar = nietbeschikbaar + 1
beschikbaar = 12 - nietbeschikbaar
print(int(beschikbaar))
