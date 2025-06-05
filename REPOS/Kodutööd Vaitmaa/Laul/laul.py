  
# kirjuta programm mis
# loeb failist laulusõnu (ise valid laulu)
# kuvab välja kõik sõnad
# arvutab kokku mitu täishäälikut on (aeiouõäöüy)
# kuvab välja kõik sõnad mis on pikemad kui 7 tähte
# laseb kasutajal kirjutada ise ühe värsi (4 rida) juurde
#05.05.2025

fail = open("laul.txt", "r", encoding="utf-8")
tekst = fail.read()
fail.close()

print("Sõnad failis:")
sõnad = tekst.split()
for sõna in sõnad:
    print(sõna)

täishäälikud = "aeiouõäöüyAEIOUÕÄÖÜY"
arv = 0
for täht in tekst:
    if täht in täishäälikud:
        arv += 1
print("Täishäälikuid on:", arv)

print("Pikad sõnad (7):")
for sõna in sõnad:
    if len(sõna) > 7:
        print(sõna)

print("Kirjuta 4 rida juurde:")
uued_read = []
for i in range(4):
    rida = input("Rida " + str(i+1) + ": ")
    uued_read.append(rida)

fail = open("laul.txt", "a", encoding="utf-8")
for rida in uued_read:
    fail.write("\n" + rida)
fail.close()

print("Rohkem ridasi pole vaja.")