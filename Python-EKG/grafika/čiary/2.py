import tkinter
plocha=tkinter.Canvas(bg="yellow",width="400",height="600")
plocha.pack()
plocha.create_line(10,10,210,10,width="5",fill="white")
plocha.create_line(20,110,20,20,width="10",fill="brown")
plocha.create_line(20,30,250,100,width="3",fill="purple")

print()
input("Preskončenie stlač ENTER.")
quit()
