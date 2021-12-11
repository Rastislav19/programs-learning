import tkinter as tk
plocha=tk.Canvas(height=300,width=100,bg="black")
plocha.pack()
plocha.create_rectangle(10,10,90,290,fill="grey",outline="")
plocha.create_oval(50-35,70-35,50+35,70+35,fill="red",outline="")
plocha.create_oval(50-35,150-35,50+35,150+35,fill="yellow",outline="")
plocha.create_oval(50-35,230-35,50+35,230+35,fill="green",outline="")

print()
input()
quit()
