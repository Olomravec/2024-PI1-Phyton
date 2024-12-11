import tkinter
width = 1000
height = 520
canvas = tkinter.Canvas(height = height, width = width)
canvas.pack()
x = 10
y = 10
dlzka = 100
farba = "red"
def dom(x,y,dlzka,farba):
    canvas.create_polygon(x,y + dlzka/2, x+dlzka/2,y, x + dlzka, y+dlzka/2 ,fill= "black")
    canvas.create_rectangle(x,y+dlzka/2,x+dlzka, y+dlzka/2+dlzka,fill = farba)
    canvas.create_rectangle(x + dlzka/4, y + dlzka/4*3, x + dlzka/4 *3 ,y + dlzka+ dlzka/4,fill= "light blue" )
    canvas.create_line(x+dlzka/2 , y + dlzka/4+dlzka, x + dlzka/2,y +dlzka/4*3 )
    canvas.create_line(x + dlzka/4,y + dlzka, x+dlzka/4*3,y + dlzka )

def ulica(x,y,dlzka,pocet):
    farba1,farba2 = "red","blue"
    for i in range(pocet):
        dom(x,y,dlzka,farba1)
        x = x+ dlzka + 10
        farba1 , farba2 = farba2,farba1

def dedina(dlzka):
    y =10
    ulicu = height // (dlzka + dlzka//2+10)
    domy = width //(dlzka+10)
    for i in range(ulicu):
        ulica(x,y,dlzka,domy)
        y = y + dlzka/2*3 + 5
dedina(50)



    

tkinter.mainloop()