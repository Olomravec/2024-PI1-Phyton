import tkinter

canvas = tkinter.Canvas() #vytvorenie plátna a jeho priradenie do premennej canvas
canvas.pack()   #umiestnenie plátna do okna

canvas.create_text(100, 75, text="Ahoj")
#   vypíše text"Ahoj" na pozícii x=100 a y=100
# suradnice zadavame vzdy v poradi x,y
# x rastie smerom doprava
# y rastie smerom dole

canvas.create_rectangle(50, 50, 150, 100)
#vykreslenie stvorca (obdlznika)
#prve dve cisla urcuju poziciu zaciatocneho bodu
#dalsie dve urcuju poziciu koncoveho bodu

canvas.create_oval(50, 50, 150, 100)
#vykreslenie kruhu (oválu)

tkinter.mainloop()  #aby zostao okno otvorene, aby sa nezavrelo