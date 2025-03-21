# kirjuta programm mis
# küsib kasutajalt tsükli sees kui vana ta on (tühja sisestuse puhul küsitakse uuesti niikaua kuni kasutaja on midagi kirjutanud)
# - kui kasutaja on noorem kui 3 aastat, ütle kasutajale et on liiga noor, ning kujundit ei joonistata
# küsib kasutajalt tsükli sees mis on ta lemmikvärv x
# - Valikusse pange(punane oranz kollane roheline helesinine tumesinine lilla roosa must valge pruun tumerohline ja teal) x
# - kasutajasisend tuleb standardiseerida sõnetöötlusmeetoditega x
# - kui kasutaja ei sisesta midagi mis on valikus, töötab tsükkel niikaua kuni kasutaja sisestab midagi mis on 	x
# - kasutajasisend tõlgitakse turtle jaoks inglise keelde ifide abil
# küsib kasutajalt tsükli sees mis on ta lemmikkujund
# - Valikusse pange(ring, ruut, võrdhaarne kolmnurk, kuusnurk)
# - kasutajasisend tuleb standardiseerida sõnetöötlusmeetoditega
# - kui kasutaja ei sisesta midagi mis on valikus, töötab tsükkel niikaua kuni kasutaja sisestab midagi mis on
# Põhinedes kasutajalt saadud andmetele, joonista kasutaja lemmikvärviga tema lemmikkujund.
# Siis tagasta konsooli sõnum "Palun <nimi>, siin on sinu <värv> <kujund>!"
from turtle import*

valik = ""
valikk = ""

print(" Mis on sinu nimi")
nimi = input()

print (" Kui vana oled?")
vanus = int(input())

if ( vanus <= 3):
    print(" Oled liiga noor, et kujundid joonistada")
if ( vanus >= 3):
    print (" Mis on teie lemmikvärv valikus on")
    print (" red ehk punane")
    print (" orange ehk oranz")
    print (" yellow ehk kollane")
    print (" green ehk roheline")
    print (" light blue ehk helesinine")
    print (" dark blue ehk tumesinine")
    print (" purple ehk lilla")
    print (" pink ehk roosa")
    print (" black ehk must")
    print (" white ehk valge")
    print (" brown ehk pruun")
    print (" dark green ehk tumeroheline")
    
    
            
    while (valik == ""):
        print (" Proovi jälle")
        valik = input()
        
        if (valik == "punane"):
            color ("red")
        if (valik == "oranz"):
            color ("orange")
        if (valik == "kollane"):
            color ("yellow")
        if (valik == "roheline"):
            color ("green")
        if (valik == "helesinine"):
            color ("light blue")
        if (valik == "tumesinine"):
            color ("dark blue")
        if (valik == "lilla"):
            color ("purple")
        if (valik == "roosa"):
            color ("pink")
        if (valik == "must"):
            color ("black")
        if (valik == "valge"):
            color ("white")
        if (valik == "punane"):
            color ("red")
        if (valik == "pruun"):
            color ("brown")
        if (valik == "tumeroheline"):
            color ("dark green")
        
        

        
        print (" Mis on teie lemmikkujund?")
        print ("ring")
        print (" ruut ")
        print ("võrdhaarne kolmnurk")
        print ("kuusnurk")
        
    while (valikk == ""):
        print (" Proovi jälle")
        valikk = input()
        
    if (valikk == "ruut"):
        
        begin_fill()
        forward (100)
        left (90)
        forward (100)
        left (90)
        forward (100)
        left (90)
        forward (100)
        left (90)
        end_fill()
        
    if (valikk == "võrdhaarne kolmnurk"):
        begin_fill()
        forward (100)
        left (120)
        forward (100)
        left (120)
        forward (100)
        end_fill()
    
    if (valikk == "ring"):
        
        begin_fill()
        circle(100)
        end_fill()
    
    if (valikk == "kuusnurk"):
        
        begin_fill()
        fd(100)
        lt(60)
        fd(100)
        lt(60)
        fd(100)
        lt (60)
        fd (100)
        lt(60)
        fd(100)
        lt(60)
        fd(100)
        end_fill()
        
        
    print (" Tere ",nimi,"ja teie valitud värv oli",valik,"ja kujund oli",valikk,)
        
exitonclick()
