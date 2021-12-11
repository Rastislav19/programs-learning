import tkinter as tk
plocha=tk.Canvas(height=110,width=200)
plocha.pack()
x=10
y=10
y2=40
for i in range(5):
    plocha.create_line(x,y,x,y2)
    x+=10
    y+=10
    y2+=10
    plocha.update()
    plocha.after(100)

print()
input()
quit()
