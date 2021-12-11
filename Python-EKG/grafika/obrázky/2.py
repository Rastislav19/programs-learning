import tkinter as tk
import random
plocha=tk.Canvas(width=1000,height=600)
plocha.pack()

r=20
for i in range(30):
    x=random.randint(30,970)
    y=random.randint(30,570)
    číslo=random.randint(1,30)
    farba=f"#{random.randrange(256**3):06x}"
    plocha.create_oval(x-r,y-r,x+r,y+r,fill=farba)
    plocha.create_text(x,y,text=číslo)
    plocha.update()
    plocha.after(100)

print()
input()
quit()
