import tkinter
plocha=tkinter.Canvas(width="600",height="600")
plocha.pack() 
a=110,10
b=210,200
c=10,200
plocha.create_line(a,b,width="5",fill="yellow")
plocha.create_line(b,c,width="7",fill="blue")
plocha.create_line(c,a,width="9",fill="green")

print()
input("Pre stlačenie stlač ENTER.")
quit()
