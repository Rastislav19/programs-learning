import tkinter as tk
plocha=tk.Canvas(height=350,width=400)
plocha.pack()
x=10
y=10
x2=20
y2=15
for i in range(30):
    plocha.create_rectangle(x,y,x2,y2)
    x2+=5
    y2+=5

print()
input()
quit()
