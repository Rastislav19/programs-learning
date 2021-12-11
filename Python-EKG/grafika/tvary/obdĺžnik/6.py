import tkinter
plocha=tkinter.Canvas()
plocha.pack()
#A)
plocha.create_rectangle(120,100,170,150)
plocha.create_rectangle(100,100,150,150)
plocha.create_rectangle(150,100,200,150)
plocha.create_rectangle(100,150,150,200)

print()
input("Pre skončenie stlač ENTER.")
quit()
