import tkinter
plocha=tkinter.Canvas()
plocha.pack()

plocha.create_oval(200-100,100-100,200+100,100+100,outline="yellow",width=3)
plocha.create_oval(200-90,100-90,200+90,100+90,width=3)
plocha.create_oval(175-50,75-50,175+50,75+50,outline="red",width=3)

print()
input("Pre skončenie programu stlač ENTER.")
quit()
