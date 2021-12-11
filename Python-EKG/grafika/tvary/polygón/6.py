import tkinter as tk
import random
plocha=tk.Canvas(height=400,width=400)
n=random.randint(1,20)
plocha.pack()
for i in range(n):
    x=random.randint(21,400)
    y=random.randint(21,400)
    r=20
    farba=f'#{random.randrange(256**3):06x}'
    číslo=random.randint(1,9)
    plocha.create_oval(x-r,y-r,x+r,y+r,fill=farba)
    plocha.create_text(x,y,text=číslo,font="Arial 30")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
