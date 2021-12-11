import tkinter
plocha=tkinter.Canvas(width="600",height="600")
plocha.pack()
farby=["red","orange","yellow","green","blue","indigo","purple"]
y=10
for i in farby:
    plocha.create_line(10,y,100,y,width="10",fill=i)
    y+=10

print()
input("Pre skončenie stlač ENTER.")
quit()
