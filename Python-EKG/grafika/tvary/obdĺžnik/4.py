import tkinter
plocha=tkinter.Canvas()
plocha.pack()
plocha.create_rectangle(10,10,60,40,fill="red", width="5")
plocha.create_rectangle(70,10,120,40,fill="green", width="5")
plocha.create_rectangle(130,10,180,40,fill="yellow", width="5")

print()
input("Pre skončenie stlač ENTER.")
quit()
