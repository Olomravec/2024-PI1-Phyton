import tkinter
canvas = tkinter.Canvas()
canvas.pack()
farba = "red"
canvas.create_rectangle(10,10,20,110,fill = farba)
canvas.create_rectangle(20,10,50,20,fill = farba)
canvas.create_rectangle(50,20,40,50,fill = farba)
canvas.create_rectangle(50,50,20,60,fill = farba)
canvas.create_rectangle(70,100,80,60,fill = farba)
canvas.create_rectangle(70,60,110,50,fill = farba)
canvas.create_rectangle(110,50,120,100,fill = farba)
canvas.create_rectangle(120,100,70,110,fill = farba)
canvas.create_rectangle(140,110,150,50,fill = farba)
canvas.create_rectangle(150,50,180,60,fill = farba)
canvas.create_rectangle(200,110,210,50,fill = farba)
canvas.create_rectangle(210,60,220,70,fill = farba)
canvas.create_rectangle(220,70,230,80,fill = farba)
canvas.create_rectangle(230,80,240,90,fill = farba)
canvas.create_rectangle(240,90,250,100,fill = farba)
canvas.create_rectangle(250,110,260,50,fill = farba)
canvas.create_rectangle(280,110,290,50,fill = farba)
canvas.create_rectangle(290,50,320,60,fill = farba)
canvas.create_rectangle(320,50,330,110,fill = farba)
canvas.create_rectangle(330,100,290,110,fill = farba)

tkinter.mainloop()