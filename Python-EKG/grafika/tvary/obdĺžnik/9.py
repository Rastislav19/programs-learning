import tkinter
import random

plocha=tkinter.Canvas()
plocha.pack()

for i in range(10):
    a=random.randint(10,240)
    b=random.randint(10,180)
    plocha.create_rectangle(a,b,a+140,b+80)

print()
input("Pre skončenie stlač ENTER.")
quit()
