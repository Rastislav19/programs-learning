import tkinter
plocha=tkinter.Canvas(width=400,height=200,bg="white")
plocha.pack()

plocha.create_oval(200-50,100-50,200+50,100+50,fill="red",outline="")
plocha.create_oval(225-45,100-45,225+45,100+45,fill="white",outline="")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
