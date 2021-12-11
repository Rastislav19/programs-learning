import tkinter
plocha=tkinter.Canvas(height=600)
plocha.pack()

plocha.create_oval(200-100,400-100,200+100,400+100)
plocha.create_oval(200-50,250-50,200+50,250+50)
plocha.create_oval(200-25,175-25,200+25,175+25)
plocha.create_oval(140-10,250-10,140+10,250+10)
plocha.create_oval(260-10,250-10,260+10,250+10)
plocha.create_rectangle(175,115,225,150)


print()
input("Pre skončenie programu stlač ENTER.")
quit()
