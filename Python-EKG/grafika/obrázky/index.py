import tkinter as tk
plocha=tk.Canvas(width=1000,height=1000)
plocha.pack()
obrázok=tk.PhotoImage(file="")#vytvorí obrázkový objekt, prečítat názov súboru
plocha.create_image(100,100,image=obrázok)

print()
input("Pre skončenie programu stlač ENTER.")
quit()
