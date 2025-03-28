# kirjuta programm mis
# küsib kasutajalt suvalist arvu vahemikus 1-20 küsimine toimub tsüklis
#

from turtle import *
from random import randint

suvalineArv = 0
while(suvalineArv < 1 or suvalineArv > 20):
    suvalineArv = int(input("Sisesta suvaline arv vahemikus 1-20"))
    juhuArv = randint(1,20)
    
    if(suvalineArv == 1 or suvalineArv == 6 or suvalineArv == 11 or suvalineArv == 16):
        if(juhuArv == suvalineArv):
            pencolor("black")
            fillcolor("red")
        else:
            color("red")
    elif(suvalineArv == 2 or suvalineArv == 7 or suvalineArv == 12 or suvalineArv == 17):
        if(juhuArv == suvalineArv):
            pencolor("black")
            fillcolor("yellow")
        else:
            color("yellow")
    elif(suvalineArv == 3 or suvalineArv == 8 or suvalineArv == 13 or suvalineArv == 18):
        if(juhuArv == suvalineArv):
            pencolor("black")
            fillcolor("green")
        else:
            color("green")
    elif(suvalineArv == 4 or suvalineArv == 9 or suvalineArv == 14 or suvalineArv == 19):
        if(juhuArv == suvalineArv):
            pencolor("black")
            fillcolor("blue")
        else:
            color("blue")
    elif(suvalineArv == 5 or suvalineArv == 10 or suvalineArv == 15 or suvalineArv == 20):
        if(juhuArv == suvalineArv):
            pencolor("gray")
            fillcolor("black")
        else:
            color("black")
    if(suvalineArv == 1