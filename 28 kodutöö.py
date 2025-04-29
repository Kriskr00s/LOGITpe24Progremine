# NB! kõik küsimised on tsüklis mis kontrollitud tsüklimuutujaga (mitte True ja break)
# NB! kõik sisendud töödeldakse standardkujule
#kirjuta programm mis
#
# küsib kasutajalt kas tal on perekonnaliikmeid
# - kui jah, siis küsib nende kõikide liikmete lemmikloomanimesid
# - kui ei, siis küsib kas kasutajal on lemmikloomi
# - - kui jah, siis küsib kõiki nimesid
# - - kui ei, siis ütleb kahju, pesaleidjas on palju kasse kes tahaksid kodu.
# programm väljastab lause, kus loetletakse kõik lemmikloomad, lemmikloomade puudumisel seda sammu ei tehta

nimed =[]
vastus = "0"
i = "suva"

while i == "suva":
    perekond = input("kas teil on perekonnaliikmed (jah/ei): ")
    if perekond == "jah":
        while vastus != "":
            vastus = input("sisestage oma perekonnaliikmete looma nimed: ")
            i = "kartul"
            nimed.append(vastus)

    elif perekond == "ei":
        while i != "kartul":
            bro = input("kas teil on lemmikloom?(jah/ei): ")
            if bro == "jah":
                while vastus != "":
                    vastus = input("sisestage oma lemmiklooma nimi: ")
                    i = "kartul"
                    nimed.append(vastus)
            elif bro == "ei":
                i = "kartul"
                print("mine nuta")
for nimi in nimed:
    print(nimi)
