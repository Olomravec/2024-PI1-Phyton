import tkinter as tk
import random

class Pexeso:
    def __init__(self, root):
        self.root = root
        self.root.title("Pexeso s písmenami")
        self.buttons = []
        self.first = None
        self.lock = False

        letters = list("ABCDEFGHIJ") * 2
        random.shuffle(letters)
        self.values = [letters[i:i+4] for i in range(0, 16, 4)]

        self.revealed = [[False]*4 for _ in range(4)]

        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.root, text=" ", width=6, height=3,
                                font=("Arial", 18, "bold"),
                                command=lambda i=i, j=j: self.on_click(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def on_click(self, i, j):
        if self.revealed[i][j] or self.lock:
            return

        self.buttons[i][j]['text'] = self.values[i][j]
        self.buttons[i][j].update()

        if not self.first:
            self.first = (i, j)
        else:
            i1, j1 = self.first
            i2, j2 = i, j
            if self.values[i1][j1] == self.values[i2][j2]:
                print("Nájdený pár")
                self.revealed[i1][j1] = True
                self.revealed[i2][j2] = True
            else:
                self.lock = True
                self.root.after(1000, self.hide, i1, j1, i2, j2)
            self.first = None

    def hide(self, i1, j1, i2, j2):
        self.buttons[i1][j1]['text'] = " "
        self.buttons[i2][j2]['text'] = " "
        self.lock = False

root = tk.Tk()
game = Pexeso(root)
root.mainloop()