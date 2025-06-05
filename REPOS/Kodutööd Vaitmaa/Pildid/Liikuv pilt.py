    
#kirjuta programm mis
#kasutab time paketti
#kasutab tkinter paketti
#
# küsi kasutajalt milline objekt talle kõige rohkem meeldib (valikus on pall, ruubiku-kuubik, vihmavari, vape)
# programm otsib samast kaustast pildi selle nimega kas gif või png formaadis.
# kasutades time.sleep() ja tahvel.move() ning raam.update() käsklusi
# pane objekt ümber ekraani tsükli abil liikuma
# - kõigepealt edasi-tagasi
# - ja siis üles-alla
# - ning siis ürita tsüklid ringiminemise jaoks ühendada
# tahvel.coords() seab objektile uued koordinaadid (muutuja, uus x1, uus y1, uus x2, uus y2)
# tahvel.move() liigutab objekti, parameetrid: (muutuja, kui palju x muuta, kui palju y muuta)
# raam.update() värskendab akna sisu, vajalik enne ka tahvel.pack() teha
# time.sleep() pidurdab programmi tööd sekunditega
# raam.after() pidurdab raami uuendust millisekundites, 1000ms = 1s
# loe lisa siit: https://web.htk.tlu.ee/digitaru/programmeerimine/chapter/lisalugemine-funktsiooni-graafik-liikuvad-pildid/
 
# ülesande standardlahendus: objekt liigub ruudukujulise trajektooriga akna sees
# ülesande boonuslahendus: objekt liigub ringi trajektooriga akna sees
# 20.05.2025
import tkinter as tk
import time
import os

valik = ""
while valik not in ["pall", "ruubiku-kuubik", "vihmavari", "vape"]:
    valik = input("Vali objekt (pall, ruubiku-kuubik, vihmavari, vape): ").strip().lower()

failinimi = "C:/Users/opilane/Desktop/" + valik + ".png"

if not os.path.exists(failinimi):
    print(f"Fail {failinimi} ei ole leitud!")
    exit(1)

raam = tk.Tk()
raam.title("Liikuv objekt")
raam.geometry("711x400")

tahvel = tk.Canvas(raam, width=711, height=400)
tahvel.pack()
pilt = tk.PhotoImage(file=failinimi)
objekt = tahvel.create_image(50, 50, anchor=tk.NW, image=pilt)
raam.update()
while True:
    for _ in range(100):
        tahvel.move(objekt, 5, 0)
        raam.update()
        time.sleep(0.01)
    for _ in range(100):
        tahvel.move(objekt, 0, 5)
        raam.update()
        time.sleep(0.01)
    for _ in range(100):
        tahvel.move(objekt, -5, 0)
        raam.update()
        time.sleep(0.01)
    for _ in range(100):
        tahvel.move(objekt, 0, -5)
        raam.update()
        time.sleep(0.01)