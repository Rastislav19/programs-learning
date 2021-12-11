import tkinter as tk
import random
plocha=tk.Canvas(height=600,width=600)
plocha.pack()
for i in range(20):
    plocha.create_rectangl(x,y,190,y)
    x+=10
    y+=10
    plocha.update()
    plocha.after(100)

print()
input()
quit()
