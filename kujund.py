# kirjuta programm mis
# küsib kasutajalt tema lemmikvärvi
# küsib kasutajalt tema lemmikkujundit (ruut, ring, ristkülik, võrdhaarne kolmnurk, täisnurkne kolmnurk)
# joonistab kasutajale vastava kujundi tema lemmikvärviga
from turtle import *
from random import randint
värv = input("Mis on teie lemmikvärv? Inglise keeles palun")
kujund = input("Mis on teie lemmikkujund? ruut/ring/ristkülik/võrdhaarne kolmnurk/täisnurkne kolmnurk")


 
if kujund == ("ruut"):
    color (värv)
    fd(90)
    lt(90)
    fd(90)
    lt(90)
    fd(90)
    lt(90)
    fd(90)
    lt(90)
elif kujund == ("ring"):
    color (värv)
    circle(100)
elif kujund == ("ristkülik"):
    color (värv)
    fd(200)
    lt(90)
    fd(100)
    lt(90)
    fd(200)
    lt(90)
    fd(100)
elif kujund == ("võrdhaarne kolmnurk"):
    color (värv)
    fd(100)
    lt(120)
    fd(100)
    lt(120)
    fd(100)
elif kujund == ("täisnurkne kolmnurk"):
    color (värv)
    fd(100)
    rt(120)
    fd(200)
    rt(150)
    fd(180)
    
    

    
    

exitonclick()