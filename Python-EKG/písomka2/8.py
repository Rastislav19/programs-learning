import tkinter as tk
import random
plocha=tk.Canvas(width=1000,height=500)
n=int(input("Zadaj počet napísov (min. 15):"+"\n"))
plocha.pack()
if n<15:
    print("Chyba!!! Zadané číslo musí byť min.15!")
else:
    for i in range(n):
        x=random.randint(50,950)
        y=random.randint(50,450)
        veľkosť=random.randint(10,30)
        veľkosť_písma=f'Arial {veľkosť} bold'
        plocha.create_text(x,y,text="STREDA",fill="green",angle="-30",font=veľkosť_písma)

print()
input()
quit()
