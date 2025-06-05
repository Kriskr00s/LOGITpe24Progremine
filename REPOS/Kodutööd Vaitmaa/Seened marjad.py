   
# NB! kõik küsimised on tsüklis mis kontrollitud tsüklimuutujaga (mitte True ja break)
# NB! kõik sisendud töödeldakse standardkujule
# NB! programmi järjendi sisu väljastamine for-tsükliga
#
# Kirjuta ülesanne mis:
# - küsib kasutajalt kas ta otsib mingit seent või marja
# - küsimine toimub tsükli sees
# - - kui seent, siis programm esitab talle seente järjendi sisu. (seal on seened mida te panna otsustasite)
# - - - siis küsib kasutajalt millise seene kohta ta lugeda tahab, ning teisest - sisujärjendist - kuvatakse
# kasutajale seene kohta tekst
# - - - - Kasutajale antakse koos seeneloendiga ka üks alati esinev valikuvõimalus - "lisa juurde"
# Lisa juurde valikuga lisatakse seentejärjendile otsa uus element, mille sisend küsitakse kasutajalt
# - - - - sama tehakse ka sisujärjendiga kuhu küsitakse otsa uue sisestatud seene juurde ka selle seene kirjelduslikm info.
# - - kui marja, siis programm esitab talle marjade järjendi sisu. (seal on marjad mida te panna otsustasite)
# - - - siis küsib kasutajalt millise marja kohta ta lugeda tahab, ning teisest - sisujärjendist - kuvatakse
# kasutajale marja kohta tekst
# - - - - Kasutajale antakse koos marjaloendiga ka üks alati esinev valikuvõimalus - "lisa juurde"
# Lisa juurde valikuga lisatakse marjajärjendile otsa uus element, mille sisend küsitakse kasutajalt
# - - - - sama tehakse ka sisujärjendiga kuhu küsitakse otsa uue sisestatud marja juurde ka selle marja kirjelduslikm info.
# - pärast seda küsib programm uuesti kas ta tahab lugeda veel millegi kohta, ning programm läheb algusesse tagasi
# 29.04.2025

seened = ["pilvik", "kõrvetis", "kukeseen"]
seene_info = [
    "Pilvik on suur ja ümar seen, mida süüakse pärast korralikku kuumutamist.",
    "Kõrvetis on mürgine ja tuleks ära tunda.",
    "Kukeseen on kollakas ja hea söögiseen."
]

marjad = ["maasikas", "mustikas", "pohl"]
marja_info = [
    "Maasikas on punane ja magus marja, mida süüakse värskelt.",
    "Mustikas on väike ja tume marja, rikas antioksüdantide poolest.",
    "Pohl on hapukas marja, mida kasutatakse moosides."
]

jookseb = "jah"

while jookseb == "jah":
    otsus = input("Kas otsid seent või marja? (väljasta 'seene', 'marja' või 'välju'): ").strip().lower()

    if otsus == "seene":
        seen_valib = "jah"
        while seen_valib == "jah":
            print("\nSeened, mida tead: ")
            for i, s in enumerate(seened):
                print(f"{i+1}. {s}")
            print(f"{len(seened)+1}. lisa juurde")
           
            valik = input("Millise seene kohta tahad lugeda? (vali number või kirjuta 'tagasi'): ").strip().lower()

            if valik == "tagasi":
                seen_valib = "ei"
            elif valik.isdigit():
                valik_num = int(valik)
                if valik_num == len(seened) + 1:
                    uus_seen = input("Sisesta uue seene nimi: ").strip().lower()
                    uus_info = input(f"Sisesta info seene '{uus_seen}' kohta: ").strip()
                    seened.append(uus_seen)
                    seene_info.append(uus_info)
                    print(f"Seen '{uus_seen}' lisatud.\n")
                elif 1 <= valik_num <= len(seened):
                    print(f"\n{seened[valik_num-1].capitalize()}: {seene_info[valik_num-1]}\n")
                else:
                    print("Valik pole sobiv, proovi uuesti.\n")
            else:
                print("Palun sisesta number või 'tagasi'.\n")

    elif otsus == "marja":
        marja_valib = "jah"
        while marja_valib == "jah":
            print("\nMarjad, mida tead: ")
            for i, m in enumerate(marjad):
                print(f"{i+1}. {m}")
            print(f"{len(marjad)+1}. lisa juurde")
           
            valik = input("Millise marja kohta tahad lugeda? (vali number või kirjuta 'tagasi'): ").strip().lower()

            if valik == "tagasi":
                marja_valib = "ei"
            elif valik.isdigit():
                valik_num = int(valik)
                if valik_num == len(marjad) + 1:
                    uus_marja = input("Sisesta uue marja nimi: ").strip().lower()
                    uus_info = input(f"Sisesta info marja '{uus_marja}' kohta: ").strip()
                    marjad.append(uus_marja)
                    marja_info.append(uus_info)
                    print(f"Marja '{uus_marja}' lisatud.\n")
                elif 1 <= valik_num <= len(marjad):
                    print(f"\n{marjad[valik_num-1].capitalize()}: {marja_info[valik_num-1]}\n")
                else:
                    print("Valik pole sobiv, proovi uuesti.\n")
            else:
                print("Palun sisesta number või 'tagasi'.\n")

    elif otsus == "välju":
        jookseb = "ei"
        print("Programm lõpetab töö.")
    else:
        print("Palun vali 'seene', 'marja' või 'välju'.\n")
