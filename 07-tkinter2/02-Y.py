import tkinter
canvas = tkinter.Canvas(width = 600, height = 600 )
canvas.pack()
def ycko(x , y):# vrch
    canvas.create_rectangle(x, y,x+10, y+10)
    canvas.create_rectangle(x, y+10,x+10, y+20)
    canvas.create_rectangle(x+10, y+20,x+20, y+30)
    canvas.create_rectangle(x+20, y+30,x+30, y+40)

    canvas.create_rectangle(x+30, y+20,x+40, y+30)
    canvas.create_rectangle(x+40, y+10,x+50, y+20)
    canvas.create_rectangle(x+40, y, x+50, y+10)
    # spodek
    canvas.create_rectangle(x+20, y+40,x+30, y+50)
    canvas.create_rectangle(x+20, y+50,x+30, y+60)
    canvas.create_rectangle(x+20, y+60,x+30, y+70)
    
ycko(10,10)


tkinter.mainloop