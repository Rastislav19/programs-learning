import tkinter
plocha=tkinter.Canvas()
plocha.pack()
plocha.create_rectangle(10,50,80,175,fill="red",outline="")
plocha.create_rectangle(80,50,150,175,fill="white",outline="")
plocha.create_rectangle(150,50,220,175,fill="blue",outline="")

print()
input("Pre skončenie stlač ENTER.")
quit()
