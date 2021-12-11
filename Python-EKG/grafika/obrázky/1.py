import tkinter as tk
import random
plocha=tk.Canvas(width=1000,height=600)
plocha.pack()

r=20
for i in range(30):
    x=random.randint(30,970)
    y=random.randint(30,570)
    číslo=random.randint(1,30)
    plocha.create_oval(x-r,y-r,x+r,y+r,fill="yellow")
    plocha.create_text(x,y,text=číslo)
    plocha.update()#zobrazí nové zmeny v grafickej ploche
    plocha.after(100)#pozdrží beh programu o zadaný počet milisekúnd

print()
input()
quit()
