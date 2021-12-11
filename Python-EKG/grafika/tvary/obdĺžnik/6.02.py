import tkinter
plocha=tkinter.Canvas()
plocha.pack()
#B
plocha.create_rectangle(120,100,170,150,fill="white")
plocha.create_rectangle(100,100,150,150,fill="")
plocha.create_rectangle(150,100,200,150,fill="green")
plocha.create_rectangle(100,150,150,200,fill="",outline="")

print()
input("Pre skončenie stlač ENTER.")
quit()
