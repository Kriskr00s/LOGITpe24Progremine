from tkinter import *

raam = Tk()
raam.title("empty tahvel")

tahvel = Canvas(raam, width=600, height=600)

tahvel.create_line(50,50,100,50)
tahvel.create_line(200,200,200,300,300,300,200,200, width=2, fill="green", arrow = LAST)
    
tahvel.create_rectangle(50,100,100,300, width=2, outline="orange", fill="yellow")

tahvel.create_polygon(200,400,200,500,300,500, width=2, outline="black", fill="cyan")

tahvel.create_oval(400,200,500,300, width=7, outline="red", fill="orange")
tahvel.create_oval(500,200,600,500, width=7, outline="red", fill="orange")

tahvel.create_text(300,300, text="hello worwrio", fill="blue")

tahvel.pack()

raam.mainloop()