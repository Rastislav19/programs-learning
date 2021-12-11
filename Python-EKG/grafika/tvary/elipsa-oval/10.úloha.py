import tkinter
plocha=tkinter.Canvas()
plocha.pack()

plocha.create_oval(50-20,50-20,50+20,50+20,fill="",outline="blue",width=3)
plocha.create_oval(90-20,50-20,90+20,50+20,fill="",outline="black",width=3)
plocha.create_oval(130-20,50-20,130+20,50+20,fill="",outline="red",width=3)
plocha.create_oval(70-20,80-20,70+20,80+20,fill="",outline="yellow",width=3)
plocha.create_oval(110-20,80-20,110+20,80+20,fill="",outline="green",width=3)

print()
input("Pre skončenie programu stlač ENTER.")
quit()
