import tkinter
import random
canvas = tkinter.Canvas(width = 800, height = 800)
canvas.pack()
s = open("tvary.txt","w")
def riadocek():
    tvar = random.choice(["O","R","L"])
    sur = random.randint(3,797)
    sur1 = random.randint(3,797)
    sur2 = random.randint(3,797)
    sur3 = random.randint(3,797)
    farba = random.randint(0,255)
    farba1 = random.randint(0,255)
    farba2 = random.randint(0,255)
    print(tvar,sur,sur1,sur2,sur3,farba,farba1,farba2,file=s)
    
riadocek()
riadocek()
riadocek()
with open("tvary.txt", "r") as file:
    riadky = [riadok.strip() for riadok in file if riadok.strip()]

for r in riadky:
    riadok = r.split(" ")

    if riadok[0] == "R": canvas.create_rectangle(riadok[1], riadok[2], riadok[3], riadok[4], 
                                                 fill=f"#{int(riadok[5]):02x}{int(riadok[6]):02x}{int(riadok[7]):02x}")
    elif riadok[0] == "O": canvas.create_oval(riadok[1], riadok[2], riadok[3], riadok[4], 
                                              fill=f"#{int(riadok[5]):02x}{int(riadok[6]):02x}{int(riadok[7]):02x}")
    else: canvas.create_line(riadok[1],riadok[2], riadok[3], riadok[4], 
                                  fill=f"#{int(riadok[5]):02x}{int(riadok[6]):02x}{int(riadok[7]):02x}")
        
canvas.mainloop()

s.close()