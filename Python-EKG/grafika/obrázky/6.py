import tkinter as tk
plocha=tk.Canvas(width=200,height=110,bg="white")
plocha.pack()
y=2
for i in range(11):
    plocha.create_line(2,y,200,y)
    y+=10
    plocha.update()
    plocha.after(100)

x=2
for i in range(20):
    plocha.create_line(x,2,x,110)
    x+=10
    plocha.update()
    plocha.after(100)

print()
input()
quit()
