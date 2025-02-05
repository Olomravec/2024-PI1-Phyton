import tkinter 
canvas = tkinter.Canvas()
canvas.pack()
def akcia():
    label.config(text = textbox.get())
label = tkinter.Label(canvas,text = "Som label")
label.pack()
textbox = tkinter.Entry(canvas)
textbox.pack()
button = tkinter.Button(canvas, text = "SOM TLAČIDLO",command = akcia)
button.pack()

tkinter.mainloop()
