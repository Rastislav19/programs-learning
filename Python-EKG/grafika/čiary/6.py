import tkinter
plocha=tkinter.Canvas(width="600",height="600")
plocha.pack() 
a=110,10
b=210,200
c=10,200

d=110,200
e=310,200
f=210,10

plocha.create_line(a,b)
plocha.create_line(b,c)
plocha.create_line(c,a)

plocha.create_line(d,e)
plocha.create_line(e,f)
plocha.create_line(f,d)

print()
input("Pre skončenie stlač ENTER.")
quit()
