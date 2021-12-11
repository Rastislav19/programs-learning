import tkinter as tk
import random
plocha=tk.Canvas(bg="black",width=400,height=300)
plocha.pack()
n=random.randint(50,500)
for i in range(n):
    x=random.randint(1,400)
    y=random.randint(1,300)
    plocha.create_text(x,y,text="*",font="Arial 10",fill="yellow")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
