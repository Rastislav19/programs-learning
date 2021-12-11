import tkinter
plocha=tkinter.Canvas(width="600",height="600")
plocha.pack()

plocha.create_line(10,10,10,50,fill="red")
plocha.create_line(10,50,50,50,fill="red")

plocha.create_line(60,10,60,50,fill="blue")
plocha.create_line(60,10,100,10,fill="blue")
plocha.create_line(60,30,100,30,fill="blue")
plocha.create_line(60,50,100,50,fill="blue")

plocha.create_line(110,10,150,10)
plocha.create_line(130,10,130,50)

plocha.create_line(160,10,160,50,fill="green")
plocha.create_line(160,30,200,30,fill="green")
plocha.create_line(200,10,200,50,fill="green")

plocha.create_line(210,10,250,10,fill="orange")
plocha.create_line(250,10,210,50,fill="orange")
plocha.create_line(210,50,250,50,fill="orange")

print()
input("Pre skončenie stlač ENTER.")
quit()
