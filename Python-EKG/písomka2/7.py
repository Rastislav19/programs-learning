import tkinter as tk
import random
plocha=tk.Canvas(width=1000,height=500)
n=int(input("Zadaj počet kartičiek:"+"\n"))
plocha.pack()
for i in range(n):
    x=random.randint(10,990)
    y=random.randint(10,490)
    farba=f"#{random.randrange(256**3):06x}"
    plocha.create_rectangle(x,y,x+20,y+20,fill=farba)

print()
input()
quit()
