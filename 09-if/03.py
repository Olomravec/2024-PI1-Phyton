import tkinter,random
canvas_width = int(input("Zadaj sirku"))
r = int(input("Zadaj vysku"))
canvas=tkinter.Canvas(width = canvas_width,height = r)
canvas.pack()
for i in range(1000):
    x = random.randint(1,canvas_width)
    y = random.randint(1,r)

    if x < canvas_width / 2:
        if y < r /2:
            farba= "blue"
            if y > r/4 and x > canvas_width/4:
                farba="black"
            if y > r/4 and x < canvas_width/4:
                farba = "black"
        else:
            farba = "green"
    else:
        if y < r /2:
            farba ="red"
        else :
            farba = "yellow"

    canvas.create_oval(x,y,x+10,y+10,fill=farba,width=0)

tkinter.mainloop()