import tkinter as tk
plocha=tk.Canvas(width=600,height=600,bg="black")
plocha.pack()
x=10
y=10
x2=590
y2=10
for i in range(26):
    plocha.create_line(x,y,x2,y2,fill="white",width=2)
    x+=23
    y2+=20
    plocha.update()
    plocha.after(100)

print()
input()
quit()
