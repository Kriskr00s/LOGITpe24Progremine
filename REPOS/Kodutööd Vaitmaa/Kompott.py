# kirjuta programm mis
# küsib kasutajalt tsükli sees
# kas tal on hapukapsas
# - kui kasutajal ei ole, siis öeldakse et saab hautist
# kas tal on pott
# - kui kasutajal potti ei ole, siis öeldakse et suppi teha ei saa
# kas tal on vett
# - kui kasutajal vett ei ole, siis öeldakse et saab mulgikapsaid teha
# kas tal on kartulit
# kas tal on puljongit
# kas kasutajal on midagi muud kapis (ei/kasutajavastus)
# - kui kasutajal ei ole, siis öeldakse midagi eelnevatest sobivatest vastustest
# - kui kasutajal on, siis öeldakse et saab ühepajatoitu
# kogu arvutamine peab toimuma loogiliste tehetega
# 07.04.2025

while True:
    vastus = input("Kas sul on hapukapsast? (jah/ei): ")
    if vastus:
        hapukapsas = vastus == "jah"
        break
while True:
    vastus = input("Kas sul on pott? (jah/ei): ")
    if vastus:
        pott = vastus == "jah"
        break
while True:
    vastus = input("Kas sul on vett? (jah/ei): ")
    if vastus:
        vesi = vastus == "jah"
        break
while True:
    vastus = input("Kas sul on kartulit? (jah/ei): ")
    if vastus:
        kartul = vastus == "jah"
        break
while True:
    vastus = input("Kas sul on puljongit? (jah/ei): ")
    if vastus:
        puljong = vastus == "jah"
        break
while True:
    vastus = input("Kas sul on midagi muud kapis? (jah/ei): ")
    if vastus:
        midagi_muud = vastus == "jah"
        break
if hapukapsas and pott and vesi and kartul and puljong and not midagi_muud:
    print("Saab teha hapukapsasuppi.")
elif not hapukapsas and pott and vesi and kartul and puljong and not midagi_muud:
    print("Saab teha hautis.")
elif hapukapsas and not pott and vesi and kartul and puljong and midagi_muud:
    print("Mitte midagi ei saa teha.")
elif hapukapsas and pott and not vesi and kartul and puljong and not midagi_muud:
    print("Saab teha mulgikapsast.")
elif hapukapsas and pott and vesi and kartul and puljong and midagi_muud:
    print("Saab teha ühepajatoitu.")
else:
    print("Võib-olla saab teha midagi lihtsat või siis mitte midagi.")

