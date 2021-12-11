import tkinter
plocha=tkinter.Canvas(width=400,height=400,bg="blue")
plocha.pack()

plocha.create_oval(200-100,200-100,200+100,200+100,fill="yellow",outline="")
plocha.create_oval(275-50,220-90,275+50,220+90,fill="blue",outline="")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
