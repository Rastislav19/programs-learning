import tkinter
plocha=tkinter.Canvas()
plocha.pack()
x,y=100,100
r=80
plocha.create_oval(x-r,y-r,x+r,y+r)

print()
input("Pre skončenie stlačte ENTER.")
quit()
