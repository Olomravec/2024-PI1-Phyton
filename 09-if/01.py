import tkinter,random

l = int(input("Šírka plátna: "))
v = int(input("Výška plátna: "))
canvas=tkinter.Canvas(width = 500,height = 400)
canvas.pack()

for i in range (100):
    a =random.randint(1,30)
    x = random.randint(3,l-3-a)
    y = random.randint(3,v-3-a)
    if a < 10 :
        farba="green"
    elif a < 20:
        farba="blue"
    else:
        farba="green"
    canvas.create_rectangle(x,y,x+a,y+a,fill=farba, width=0)
tkinter.mainloop()
