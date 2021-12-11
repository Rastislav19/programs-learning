import tkinter
plocha=tkinter.Canvas(bg="black",width="600",height="600")
plocha.pack()

plocha.create_line(10,10,210,10,width="5",fill="white")
plocha.create_line(10,30,210,30,width="5",fill="white")
plocha.create_line(10,50,210,50,width="5",fill="white")
plocha.create_line(10,70,210,70,width="5",fill="white")
plocha.create_line(10,90,210,90,width="5",fill="white")
plocha.create_line(10,110,10,210,width="10",fill="yellow")
plocha.create_line(30,110,30,210,width="10",fill="yellow")

print()
input("Preskončenie stlač ENTER.")
quit()
