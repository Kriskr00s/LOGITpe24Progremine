# NB! kõik küsimised on tsüklis mis kontrollitud tsüklimuutujaga (mitte True ja break)
# NB! kõik sisendud töödeldakse standardkujule
# kirjuta programm mis
#
# küsib kasutajalt tema lemmikfilme (mitmus = järjend)
# programm küsib ainsana tema aegade kõige lemmikumat filmi (ainsus = muutuja)
# programm kontrollib et tema kõige lemmikum film oleks ka lemmikfilmide järjendis
# - kui on siis öeldakse kasutajale Ossa, oled oma <lemmikfilmi> isegi kaks korda pannud
# - kui ei ole, siis küsitakse aga kus on sinu <lemmikfilm>?
# programm küsib kasutajalt kas talle meeldib <programmeerija lemmikfilm>?
# - kui jah, siis lisatakse film lemmikfilmide järjendisse
# - kui ei, programm vingub "aga miks? see on ju hea"
# kui programm tuvastab et üks filmidest lemmikfilmide järjendis on Terminator siis öeldakse kasutajale et "youll be back"
# kui programm tuvastab et üks filmidest lemmikfilmide järjendis on Vanamehe Film, siis öeldakse "aga kuš šu šnikurš on šiiš?"
# kõige lõpuks loendab programm kokku mitu filmi on tema lemmikfilmide järjendis, ning
# - kui arv on 5 või vähem, öeldakse, sa ei vaata väga palju filme vist.
# - kui arv on 10 või vähem aga rohkem kui 5, "käid tihti kinos?"
# - kui arv on rohkem kui 10, "siis, pole mul siin midagi öelda härra movieguru, headaega"
# 29.04.2025

lemmikfilmid = []
print("Sisesta oma lemmikfilmid (ühe korraga). Kirjuta tühjusse ja vajuta Enter kui lõpetad.")
sisestamine_jookseb = "jah"
while sisestamine_jookseb == "jah":
    film = input("Sisesta lemmikfilm: ").strip().lower()
    if film == "":
        sisestamine_jookseb = "ei"
    else:
        lemmikfilmid.append(film)

kõige_lemmikum = input("Mis on su kõige lemmikum film? ").strip().lower()

if kõige_lemmikum in lemmikfilmid:
    print("Ossa, oled oma '" + kõige_lemmikum + "' isegi kaks korda pannud")
else:
    print("Kus on sinu '" + kõige_lemmikum + "'?")

programmeerija_lemmik = "inception"
vastus = input("Kas sulle meeldib '" + programmeerija_lemmik + "'? (jah/ei) ").strip().lower()

if vastus == "jah":
    if programmeerija_lemmik not in lemmikfilmid:
        lemmikfilmid.append(programmeerija_lemmik)
else:
    print("Aga miks? See on ju hea.")

terminator_leitud = False
i = 0
while i < len(lemmikfilmid) and not terminator_leitud:
    if "terminator" in lemmikfilmid[i]:
        terminator_leitud = True
    i += 1

if terminator_leitud:
    print("youll be back")
   
vanamehe_leitud = False
i = 0
while i < len(lemmikfilmid) and not vanamehe_leitud:
    if "vanamehe film" in lemmikfilmid[i]:
        vanamehe_leitud = True
    i += 1

if vanamehe_leitud:
    print("aga kuš šu šnikurš on šiiš?")

filmide_arv = len(lemmikfilmid)
print("Sul on lemmikfilmide järjendis kokku " + str(filmide_arv) + " filmi.")

if filmide_arv <= 5:
    print("Sa ei vaata väga palju filme vist.")
elif filmide_arv <= 10:
    print("Käid tihti kinos?")
else:
    print("Siis, pole mul siin midagi öelda härra movieguru, headaega.")