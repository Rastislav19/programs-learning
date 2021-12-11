import tkinter
import random

plocha=tkinter.Canvas()
plocha.pack()
r=20
for i in range(100):
    x=random.randint(20,350)
    y=random.randint(20,300)
    farba= f'#{random.randrange(256**3):06x}'
    plocha.create_oval(x-r,y-r,x+r,y+r,fill=farba)

print()
input("Pre skončenie stlač ENTER.")
quit()
