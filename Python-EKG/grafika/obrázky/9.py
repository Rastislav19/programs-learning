import tkinter as tk
import random
plocha=tk.Canvas(height=600,width=600)
plocha.pack()
x=10
y=15
for i in range(7):
    farba_štvorca=f"#{random.randrange(256**3):06x}"
    farba_trojúholníka=f"#{random.randrange(256**3):06x}"
    plocha.create_rectangle(x,y,x+20,y+20,fill=farba_štvorca,outline="")
    plocha.create_polygon(x,y,x+10,y-10,x+20,y,fill=farba_trojúholníka)
    x+=30
    plocha.update()
    plocha.after(100)

print()
input()
quit()
