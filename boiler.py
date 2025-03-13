# kirjuta programm mis
# küsib kasutajalt kas ta soovib osta boilerit
# (selle jaoks on vaja risttahuka valemit kasutada, ning küsida kasutajalt a ja b külg oõhjapindala jaoks sentimeetrites ja olevasoleva ala kõrguse h)
# olenevalt olemasolevast ruumalast
# - kui ruumala on liiga väike, öeldakse et meil ei ole pakkuda midagi sellises suuruses
# - kui ruumala on väike aga sobiv, pakutakse väikest boilerit väikese hinnaga
# - kui ruumala on paras, siis pakutakse väikest boilerit ja parajast boilerit
# - kui ruumala on suur, siis pakutakse väikest, parajast ja suurt boilerit.
# - kasutajalt küsitakse millist boilerit ta osta soovib NIMEPIDI, programm peab tuvastama õige nime kasutades .lower() või .upper() meetodeid
# väikese boileri maht arvutada a=35 b=35 h=70
# paraja boileri maht arvutada a=45 b=45 h=90
# suure boileri maht arvutada a=60 b=60 h=210
# hinnad mõtlete ise välja
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind
 
tahadboilerit = input("Kas soovid osta boilerit? jah/ei")
if tahadboilerit == "jah":
    põhjakülgA = int(input("Sisesta oma boileriruumi esimese külje pikkus"))
    põhjakülgB = int(input("Sisesta oma boileriruumi teise külje pikkus"))
    kõrgusH = int(input("Sisesta oma boileriruumi kõrgus"))
    kasutajaRuum = põhjakülgA*põhjakülgB*kõrgusH
    boiler1 = 35*35*70
    boiler2 = 45*45*90
    boiler3 = 60*60*210
    boiler1price = 100
    boiler2price = 200
    boiler3price = 300
    kasutajaValik = ""
    summa = 0
    if (kasutajaRuum < boiler1):
        print("Kahjuks ei ole meil teie ruumi pakkuda ühtegi boilerit. Teie ruum on liiga väike.")
    elif (kasutajaRuum < boiler2):
        print("Teie ruumi sobib meie valikust väike boiler Whirlpool")
        kasutajaValik = input("Kirjuta nimeliselt millist soovid:")
    elif (kasutajaRuum < boiler3):
        print("Saame teile pakkuda väikest boilerit Whirlpool ja keskmist boilerit Bosch.")
        kasutajaValik = input("Kirjuta nimeliselt millist soovid:")
    else:
        print("Teie valik on lai, saate valida väikest boilerit Whirlpool, keskmist boilerit Bosch ja suurt boilerit Beko.")
        kasutajaValik = input("Kirjuta nimeliselt millist soovid:")
if (kasutajaValik.lower() == "whirlpool"):
    summa = boiler1price
elif (kasutajaValik.lower() == "bosch"):
    summa = boiler2price
else:
    summa = boiler3price
if (summa != 0):
    print("Kas soovid maksta? hind on "+str(summa)+" eurot. jah/ei")
    kasmaksab = input()
if (kasmaksab.lower() == "jah"):
    Print("Aitäh ostu eest, siin on teie boiler!")
else:
    summa *= 0.9
    print("-10% hinnast, kas soovid nüüd maksta? hind on "+str(summa)+" eurot. jah/ei")
    kasmaksab = input()
if (kasmaksab.lower() == "jah"):
    Print("Aitäh ostu eest, siin on teie boiler!")
else:
    summa *= 0.9
    print("tegime veel -10% hinnast, see on viimane pakkumine. hind on "+str(summa)+" eurot. jah/ei")
    kasmaksab = input()
if (kasmaksab.lower() == "jah"):
    print("Aitäh ostu eest, siin on teie boiler!")
else:
    print("Väga kahju, tulge teinekord jälle.")
else:
    print("Tulge jälle teinekordki!")