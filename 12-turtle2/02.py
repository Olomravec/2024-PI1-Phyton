import turtle
t = turtle.Turtle()


t.shape("turtle")
t.shapesize(5,5,8)
t.color("#ff00ff", "pink")
t.pencolor("black")

pozicia = 50
t.pu() # skratka pre t.penup()
t.setpos(-400,250)
dlzka = 100
def domcek():
    def korytnacka(dlzka):
        for i in range(4):
            t.forward(dlzka)
            t.right(90)

    t.fillcolor("red")
    t.begin_fill()
    korytnacka(100)
    t.end_fill()

    def strecha():
        t.left(45)
        t.forward(71)
        t.right(90)
        t.forward(71)

    t.fillcolor("black")
    t.begin_fill()
    strecha()
    t.end_fill()

    def okno():
        t.penup()
        t.right(45)
        t.forward(33)
        t.right(90)
        t.forward(33)
        t.pendown()
        def okienko():
            for i in range(4):
                t.forward(33)
                t.left(90)
        
        t.fillcolor("white")
        t.begin_fill()
        okienko()
        t.end_fill()

        t.forward(16)
        t.left(90)
        t.forward(33)
        for i in range(3):
            t.left(90)
            t.forward(16)
        t.forward(15)
        t.penup()
        t.right(180)
        t.forward(66)
        t.left(90)
        t.forward(49)
        t.right(90)
        t.forward(20)
    okno()

for i in range(7):
    domcek()
t.setpos(-400,75)
for i in range(7):
    domcek()
t.setpos(-400,-100)
for i in range(7):
    domcek()
t.setpos(-400,-275)
for i in range(7):
    domcek()




turtle.exitonclick()