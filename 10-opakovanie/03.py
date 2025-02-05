import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

pokus = 1

def cislo():
    moje_cislo = int(textbox.get())
    global pokus
    if moje_cislo < cisloPC:
        pokus = pokus+1
        label.config(text = " Dal si mensie cislo")
        
    elif moje_cislo > cisloPC:
        pokus = pokus+1
        label.config(text = " Dal si väčšie číslo")
        
    else :
        pokus = pokus+1
        label.config(text = f"uhadol si na {pokus} pokusov")
    

cisloPC = random.randint(0,9)

label = tkinter.Label()
label.pack()

cisloPC = random.randint(0,9)

textbox = tkinter.Entry(canvas)
textbox.pack()

button = tkinter.Button( text = "Hádaj", command = cislo)
button.pack()




tkinter.mainloop()


