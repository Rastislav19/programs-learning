import tkinter
plocha=tkinter.Canvas()
plocha.pack()
a=50
plocha.create_rectangle(50,100,150,150,fill="", width="5",outline="blue") #fill=""-> bude priesvitný
plocha.create_rectangle(155,155,155+a,155+a)

print()
input("Pre skončenie stlač ENTER.")
quit()
