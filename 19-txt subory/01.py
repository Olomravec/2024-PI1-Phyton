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

s.close()