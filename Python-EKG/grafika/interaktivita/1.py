import tkinter as tk
plocha=tk.Canvas()
plocha.pack()
def meno(klik):#musí sa to robiť cez funkciu
    x=klik.x
    y=klik.y
    plocha.create_text(x,y,text="Rastííík")

plocha.bind("<Button-1>",meno)#po stlačení ľavého tlačítka načíta funkciu meno
                              #Button-2=koliesko, Button-3=pravé tlačítko

print()
input()
quit()
