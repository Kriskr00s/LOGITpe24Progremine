from turtle import *
from random import randint
bgcolor("grey")


värv = ""

randomarv = randint(0,2)

if (randomarv == 0):
    värv = "blue"
elif (randomarv == 1):
    värv = "black"
else:
    värv = "white"
    
begin_fill()
circle(100)
end_fill()

exitonclick()
