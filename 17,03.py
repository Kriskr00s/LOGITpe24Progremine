# kirjuta programm mis
# küsib kasutajalt tsükli abil tema nime, tsükkel ei tohi katkeda:✅
# - kui kasutaja ei sisesta midagi
# - kui kasutaja sisestab rohkem kui 25 tähte
# - - siis öeldakse ka kasutajale, et 25 tähte on maksimaalne nime pikkus
# küsib kasutajalt tsüklis tema saadetise pikkust, laiust, kõrgust ja raskust. tsükkel ei tohi katkeda:
# - kui kasutaja paneb vastusteks 0
# - kui kasutaja paneb vastusteks mitte midagi
# küsib kasutajalt sihtriiki, tsükkel ei tohi katkeda:
# - kui kasutaja ei sisesta midagi
# - kui kasutaja sisestab rohkem kui 25 tähte
# Arvutab kasutaja saadetise ruumala.
# Arvutab kasutajale saadetise maksumuse. (ruumala * raskus)
# Küsib kasutajalt tsükli abil kas ta maksab, tsükkel ei tohi katkeda:
# - kui kasutaja ei sisesta midagi
# - kui kasutaja sisestab midagi muud kui jah/ei
# - - Kui kasutaja on ei öelnud rohkem kui 5 korda, muutub kasutajale esitatav küsimus ähvardavamaks
# - kui kasutaja ütleb jah, siis öeldakse kasutajale et "<nimi>, teie saadetis on teel <sihtriik>i"
 
# kasuta while tsüklit

name = ""
while((name == "") or (len(name) > 25) or (name == " ")):
    if len(name) > 25:
        print("Nimi on liiga pikk")
    name = input("Palun sisesta oma nimi: ")
print(name)
while((pikkus == 0.0) or (laius == 0.0 or

if (laius == 0.0):
    laius = float(input("Kui lai on sinu saadetis?: "))
if (kõrgus == 0.0):
    kõrgus = float(input("Kui kõrge on sinu saadetis?: "))
if (raskus == 0.0):
    raskus = float(input("Kui palju kaalub sinu saadetis?: "))

maksumuseArvutus = (pikkus * laius * kõrgus) * raskus

while(sihtriik == "" or (len(sihtriik) > 25) or (sihtriik == " ")):
    if len(sihtriik) > 25:
        print("Riigi nimi on liiga pikk, 25 tähte on maksimaalne pikkus.")
    sihtriik = input("Palun sisesta sihtriik: ")
# print(sihtriik)

kasMaksab = ""
mituKordaKüsitudOn = 0
positiivneVastus = False
while(((kasMaksab == "") or (kasMaksab.lower() != "ei") or (kasMaksab.lower() != "jah") or 
       (kasMaksab.lower() == "ei")) and (positiivneVastus == False)):
    mituKordaKüsitudOn += 1
    if (kasMaksab.lower() == "jah"):
        positiivneVastus = True
        print("name+, teie saadetis on teel "+sihtriik)
    if (mituKordaKüsitudOn > 5):
        kasMaksab = input("Olete kindel et soovite külma arvet teha, rsk? (jah/ei): ")
    else:
        kasMaksab = input("Kas soovite maksta? (jah/ei): ")