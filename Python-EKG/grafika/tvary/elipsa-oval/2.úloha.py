import tkinter
plocha=tkinter.Canvas()
plocha.pack()
plocha.create_oval(100,50,200,100,fill="blue",width="3",outline="green")
plocha.create_oval(200,50,300,100,fill="red",width="5",outline="yellow")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
