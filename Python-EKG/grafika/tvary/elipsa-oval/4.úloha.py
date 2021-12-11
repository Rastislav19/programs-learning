import tkinter
plocha=tkinter.Canvas()
plocha.pack()
plocha.create_oval(10,10,60,60,outline="blue")
plocha.create_oval(30,10,80,60,outline="blue")
plocha.create_oval(50,20,100,70,outline="blue")
plocha.create_oval(90,30,140,80,outline="blue")
plocha.create_oval(130,50,180,100,outline="blue")
plocha.create_oval(160,80,210,130,outline="blue")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
