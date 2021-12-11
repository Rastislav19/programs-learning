import tkinter
plocha=tkinter.Canvas(width=600,height=600)
plocha.pack()

plocha.create_oval(300-200,300-200,300+200,300+200)
plocha.create_oval(200-25,250-25,200+25,250+25)
plocha.create_oval(400-25,250-25,400+25,250+25)
plocha.create_oval(75-25,300-25,75+25,300+25)
plocha.create_oval(525-25,300-25,525+25,300+25)
plocha.create_oval(200,400,400,450)
plocha.create_rectangle(275,275,325,350)

print()
input("Pre skončenie programu stlač ENTER.")
quit()
