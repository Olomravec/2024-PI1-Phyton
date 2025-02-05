<<<<<<< HEAD
import tkinter, random
l = int(input("Zadaj šírku: "))
p = int(input("Zadaj výšku: "))
s = int(input("Zadaj počet kruhov: "))
canvas = tkinter.Canvas(width= l, height = p)
canvas.pack()
for i in range(s):
    a = random.randint(1,30)
    x = random.randint(1,l)
    y = random.randint(1,p)
    if x < l/2: 
        if y < p/2:
            farba = "blue"
            if x > l/4 and y > p/4:
                farba = "black"
    if  x < l/2:
        if y > p/2:
            farba = "green"
            if x > l/4 and y < p/1.4:
                    farba = "black"
    if x > l/2: 
        if y < p/2:
            farba = "gray"
            if x < l/1.25 and y >p/4:
                farba = "black"
                
    if x > l/2: 
        if y > p/2:
            farba = "pink"
            if x < l/1.25 and y < p/1.4:
                    farba = "black"
    canvas.create_oval(x,y,x+a,y+a,fill = farba,width = 0)

tkinter.mainloop()
=======
n = int(input("Zadaj n:"))
pocet = 0
for i in range(n):#n znazorni tu hodnotu co sme hore napisali a i pocita od 0 az po n-1 lebo posledne nepocita
    pocet = pocet + i
print("Súčet čísel je:",pocet)

>>>>>>> b9679ba2a4c7fa5dafb4753b26491685f50fce0c
