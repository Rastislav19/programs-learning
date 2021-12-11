import tkinter as tk
plocha=tk.Canvas(height=110,width=200)
plocha.pack()
y=10
y2=20
for i in range(5):
    plocha.create_line(10,y,190,y2)
    y+=10
    y2+=15
    plocha.update()
    plocha.after(100)

print()
input()
quit()
