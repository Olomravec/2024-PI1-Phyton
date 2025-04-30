import tkinter

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