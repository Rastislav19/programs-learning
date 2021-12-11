import tkinter
plocha=tkinter.Canvas(width=400,height=200)
plocha.pack()
x,y=200,100
r=50
plocha.create_oval(x-r,y-r,x+r,y+r,fill="red",outline="")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
