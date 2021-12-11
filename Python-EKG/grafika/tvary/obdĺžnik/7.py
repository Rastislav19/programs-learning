import tkinter
plocha=tkinter.Canvas()
plocha.pack()

#rakúsko
plocha.create_rectangle(10,10,60,20,fill="red",outline="")
plocha.create_rectangle(10,20,60,30,fill="white",outline="")
plocha.create_rectangle(10,30,60,40,fill="red",outline="")

#Nemecko
plocha.create_rectangle(70,10,120,20,fill="black",outline="")
plocha.create_rectangle(70,20,120,30,fill="red",outline="")
plocha.create_rectangle(70,30,120,40,fill="yellow",outline="")

#Taliansko
plocha.create_rectangle(130,10,145,40,fill="green",outline="")
plocha.create_rectangle(145,10,165,40,fill="white",outline="")
plocha.create_rectangle(165,10,180,40,fill="red",outline="")

#Švajčiarsko
plocha.create_rectangle(200,10,250,40,fill="red",outline="")
plocha.create_rectangle(215,20,235,30,fill="white",outline="")
plocha.create_rectangle(220,15,230,35,fill="white",outline="")

#Izrael
plocha.create_rectangle(260,10,310,15,fill="blue",outline="")
plocha.create_rectangle(260,15,310,35,fill="white",outline="")
plocha.create_rectangle(260,35,310,40,fill="blue",outline="")
plocha.create_line(285,20,)
plocha.create_line()
plocha.create_line()
plocha.create_line()
plocha.create_line()
plocha.create_line()

print()
input("Pre skončenie stlač ENTER.")
quit()
