import tkinter
plocha=tkinter.Canvas()
plocha.pack()
plocha.create_rectangle(10,10,60,40,fill="blue", width="4")
plocha.create_rectangle(60,10,110,40,fill="yellow", width="4")
plocha.create_rectangle(10,40,60,70,fill="red", width="4")
plocha.create_rectangle(35,25,85,55,fill="brown", width="4")

print()
input("Pre skončenie stlač ENTER.")
quit()
