import tkinter as tk
plocha=tk.Canvas(width=1000,height=600)
plocha.pack()

def postavička():
    plocha.create_polygon(10,100,40,50,70,100,fill="white",outline="black")
    plocha.create_oval(20,20,60,50,fill="red")
    plocha.create_rectangle(25,100,35,150,fill="red")
    plocha.create_rectangle(45,100,55,150,fill="red")

postavička()

print()
input()
quit()
