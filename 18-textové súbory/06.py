import tkinter

<<<<<<< HEAD
canvas=tkinter.Canvas(width = 250, height = 320)
canvas.pack()

subor=open("body.txt")
for i in range(4):
    t=subor.readline()
    c=subor.readline()
    kordinacie=subor.readline()
    medzery=kordinacie.find(" ")
    x=int(kordinacie[:medzery])
    y=int(kordinacie[medzery+1:])
    if t.strip()=="o":
        canvas.create_oval(x-5,y-5,x+5,y+5, fill=c.strip())
    if t.strip()=="r":
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill=c.strip())
                         
tkinter.mainloop()
=======
canvas=tkinter.Canvas(width=500, height=500)
canvas.pack()

subor=open("body.txt")


# for i in range(3):
#     tvar=subor.readline()
#     if tvar=="o":
#         canvas.create_oval(x)


for i in range(4):
    tvar=subor.readline()
    farba=subor.readline()
    coord=subor.readline()
    medz=coord.find(" ")
    x=int(coord[:medz])
    y=int(coord[medz+1:])
    if tvar.strip()=="o":
        canvas.create_oval(x-5,y-5,x+5,y+5, fill=farba.strip())
    if tvar.strip()=="r":
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill=farba.strip())
                         
tkinter.mainloop()
>>>>>>> bcbd6342c22d0d2db2a028fbc9959b8cacb2a472
