import tkinter,random
canvas_width = int(input("Zadaj sirku"))
r = int(input("Zadaj vysku"))
canvas=tkinter.Canvas(width = canvas_width,height = r)
canvas.pack()
for i in range(1000):
    x = random.randint(1,canvas_width)
    y = random.randint(1,r)
    # if  (x < s/2) and (y < r /2): #zložená podmienka tzn. testujeme viac vlastností 
    #     #medzi zložené podmienky vkladame logické operátory (and = a zároveň, or = alebo)
    #     farba = "red" 
    # elif  (x > s/2) and (y < r /2):
    #     farba = "blue"
    # elif  (x < s/2) and (y > r /2):
    #     farba = "green"
    # elif  (x > s/2) and (y > r /2):
    #     farba = "yellow"
    if x < canvas_width / 2:
        if y < r /2:
            farba= "blue"
        else:
            farba = "green"
    else:
        if y < r /2:
            farba ="red"
        else :
            farba = "yellow"

    canvas.create_oval(x,y,x+10,y+10,fill=farba,width=0)

tkinter.mainloop()



