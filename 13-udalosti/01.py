import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def pajton():
    x = random.randint(50,330)
    y = random.randint(20,240)
    canvas.create_text(x,y,text = "Python")
tlacidlo = tkinter.Button(command = pajton,text = ("Semka klikaj"))
tlacidlo.pack()





tkinter.mainloop()