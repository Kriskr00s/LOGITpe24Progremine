 
# kirjuta programm mis
# küsib kasutajalt kui suur ta põrand on
# (selle jaoks on vaja ristküliku valemit kasutada, ning küsida kasutajalt a ja b külg sentimeetrites)
# küsib kasutajalt milliseid põrandaplaate ta tahab
# kasutajale antakse 6 ascii näidet, ja kasutaja sisestab numbri milline muster talle meeldib
#
# ██░░ ║┌─┐ ▀▄░░
# ░░██ ║└─┘ ░░▀▄ (muid mustreid saab välja mõelda kas tähtedest või start -> character map abiga)
# (ülejäänud kolm mustrit mõtle ise)
# väljasta kasutajale ekraan mustriga koos hinnaarvutusega.
# (esimene muster on odavaim, viimane kalleim, tehe on pindala*mustriväärtus)
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind

print("Kui suur on teie põrand? Kui mõõtsid ära kirjuta ok")
ok = input()
print("Ütle pikkus")
pikkus = int(input())
print("Ütle laius")
laius = int(input())
pindala = pikkus*laius
print("Teie põranda pindala on" ,pindala)
print("Milliseid põranda plaate te tahate?")
print ("valige 1-6")
print(" 1 ")
print(" ██░░ ")
print(" 2 ")
print(" ║┌─┐ ")
print(" 3 ")
print(" ▀▄░░ ")
print(" 4 ")
print(" ░░██ ")
print(" 5 ")
print(" ║└─┘ ")
print(" 6 ")
print(" ░░▀▄ ")
input == 1
print (" ██░░ ")




