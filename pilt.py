from tkinter import *
raam = Tk()
raam.title("Pildid")
tahvel = Canvas(raam, width=500, height=700, background="white")
tahvel.grid()

pilt1 = PhotoImage(file="Pilt 1.gif")
img = tahvel.create_image(200, 150, image=pilt1)

pilt2 = PhotoImage(file="Pilt 2.gif")
img = tahvel.create_image(50, 300, image=pilt2, activeimage=pilt2, anchor=NW)

raam.mainloop()