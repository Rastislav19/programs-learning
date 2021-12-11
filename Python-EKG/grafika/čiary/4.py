import tkinter
plocha=tkinter.Canvas(width="600",height="600")
plocha.pack()
y=10
for i in range(7):
    if i==0:
        plocha.create_line(10,y,100,y,width="10",fill="red")
    elif i==1:
        plocha.create_line(10,y,100,y,width="10",fill="orange")
    elif i==2:
        plocha.create_line(10,y,100,y,width="10",fill="yellow")
    elif i==3:
        plocha.create_line(10,y,100,y,width="10",fill="green")
    elif i==4:
        plocha.create_line(10,y,100,y,width="10",fill="blue")
    elif i==5:
        plocha.create_line(10,y,100,y,width="10",fill="indigo")
    else:
        plocha.create_line(10,y,100,y,width="10",fill="purple")
    y+=10

print()
input("Pre skončenie stlač ENTER.")
quit()
