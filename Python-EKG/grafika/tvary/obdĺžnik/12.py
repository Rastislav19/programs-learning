import tkinter
plocha=tkinter.Canvas()
plocha.pack()
plocha.create_line(10,100,10,50)
plocha.create_line(10,50,60,100)
plocha.create_line(60,100,60,50)
plocha.create_line(60,50,10,50)
plocha.create_line(10,50,35,10)
plocha.create_line(35,10,60,50)
plocha.create_line(60,50,10,100)
plocha.create_line(10,100,60,100)

print()
input("Pre skončenie stlač ENTER.")
quit()
