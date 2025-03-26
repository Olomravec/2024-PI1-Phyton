import tkinter,random
canvas = tkinter.Canvas(width = 800 , height = 600)
canvas.pack()
for i in range(500):
    x =  random.randint(3,700)
    y = random.randint(3,500)
    farba = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"
    print(farba)
    canvas.create_rectangle(x,y,x+40,y+40, fill=farba)
tkinter.mainloop()