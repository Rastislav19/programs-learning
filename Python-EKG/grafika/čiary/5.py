import tkinter
plocha=tkinter.Canvas(width="600",height="600")
plocha.pack()
a=110,10
b=210,200
c=10,200
plocha.create_line(a,b)
plocha.create_line(b,c)
plocha.create_line(c,a)

print()
input("Pre stlačenie stlač ENTER.")
quit()
