import tkinter as tk
import random
plocha=tk.Canvas(height=500,width=1000)
plocha.pack()
farby=["red","blue","yellow"]
for i in range(50):
    x=random.randint(10,990)
    y=random.randint(10,490)
    x2=random.randint(10,990)
    y2=random.randint(10,490)
    farba=random.choice(farby)
    plocha.create_line(x,y,x2,y2,fill=farba)

print()
input()
quit()
