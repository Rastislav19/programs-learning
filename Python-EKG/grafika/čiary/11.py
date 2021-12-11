import tkinter
plocha=tkinter.Canvas(width="600",height="600")
plocha.pack()

plocha.create_line(10,10,50,10)
plocha.create_line(50,10,50,70)
plocha.create_line(50,70,10,70)
plocha.create_line(10,70,10,10)

print()
input("Pre skončenie stlač ENTER.")
quit()
