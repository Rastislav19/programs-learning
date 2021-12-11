import tkinter
plocha=tkinter.Canvas()
plocha.pack()
plocha.create_oval(50,100,150,150,width="3",outline="blue",fill="red")
plocha.create_rectangle(50,100,150,150)

print()
input("Pre skončenie stlačte ENTER.")
quit()
