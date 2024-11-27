import random
import tkinter

dlzka = int(input("Zadaj dĺžku štvorca: "))
pocet = int(input("Zadaj počet: "))

canvas = tkinter.Canvas(height = 400,width = 500)
canvas.pack()


farba1 = "red"
for i in range(pocet):
    x = random.randint(3,500-dlzka-3)
    y = random.randint(3,400-dlzka-3)
    canvas.create_rectangle(x,y,x+dlzka,y+dlzka,fill=random.choice(["red","green","blue"]))
    


tkinter.mainloop()