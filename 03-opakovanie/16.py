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
