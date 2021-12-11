import tkinter
plocha=tkinter.Canvas(width="600",height="600",bg="yellow")
plocha.pack()

plocha.create_line(10,10,130,10,fill="brown")
plocha.create_line(10,10,10,50,fill="brown")
plocha.create_line(30,10,30,50,fill="brown")
plocha.create_line(50,10,50,50,fill="brown")
plocha.create_line(70,10,70,50,fill="brown")
plocha.create_line(90,10,90,50,fill="brown")
plocha.create_line(110,10,110,50,fill="brown")
plocha.create_line(130,10,130,50,fill="brown")

print()
input("Pre skončenie stlač ENTER.")
quit()
