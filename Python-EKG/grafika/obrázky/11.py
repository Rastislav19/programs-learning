import tkinter as tk
plocha=tk.Canvas(width=1000,height=600)
plocha.pack()

plocha.create_rectangle(110,295,445,305,fill="grey")
def rušeň():
    plocha.create_rectangle(10,270,110,330,fill="green")
    plocha.create_rectangle(30,260,50,270,fill="blue")
    plocha.create_rectangle(70,250,110,270,fill="red")
    x=30
    for i in range(4):
        plocha.create_line(x,255,x+1,230,width=3)
        x+=7
    x=9
    for i in range(4):
        plocha.create_oval(x,320,x+30,350,fill="black")
        x+=25
print(rušeň())
x=115
x2=125
x3=170
for i in range(4):
    plocha.create_rectangle(x,270,x+100,330,fill="green")
    plocha.create_rectangle(x2,280,x2+35,300,fill="blue")
    plocha.create_rectangle(x3,280,x3+35,300,fill="blue")
    plocha.create_oval(x2,320,x2+35,350,fill="black")
    plocha.create_oval(x3,320,x3+35,350,fill="black")
    x+=110
    x2+=110
    x3+=110

print()
input()
quit()
