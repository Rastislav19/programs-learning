import tkinter as tk
plocha=tk.Canvas()
plocha.pack()

plocha.create_rectangle(50,50,230,230,fill="red")
plocha.create_rectangle(90,90,190,190,fill="blue")

plocha.create_text(45,45,text="A")
plocha.create_text(235,45,text="B")
plocha.create_text(45,235,text="D")
plocha.create_text(235,235,text="C")

plocha.create_text(140,184,text="100")
plocha.create_text(240,140,text="180")

print()
input("Pre skončenie programu stalč ENTER.")
quit()
