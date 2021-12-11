import tkinter as tk
plocha=tk.Canvas(width=200,height=110,bg="white")
plocha.pack()
x=1
y=1
x2=200
y2=1
for i in range(11):
    plocha.create_line(x,y,x2,y2)
    y+=10
    y2+=10
    plocha.update()
    plocha.after(100)

print()
input()
quit()
