import tkinter
import random

plocha=tkinter.Canvas()
plocha.pack()

for i in range(10):
    a=random.randint(10,240)
    b=random.randint(10,180)
    šírka=random.randint(10,100)
    výška=random.randint(10,100)
    plocha.create_rectangle(a,b,a+šírka,b+výška)

print()
input("Pre skončenie stlač ENTER.")
quit()
