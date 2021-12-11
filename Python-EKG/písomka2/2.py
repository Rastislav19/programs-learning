import tkinter as tk
plocha=tk.Canvas(height=500,width=500)
plocha.pack()
plocha.create_rectangle(10,10,150,40,fill="red")
plocha.create_rectangle(10,40,150,70,fill="white")
plocha.create_rectangle(10,70,150,100,fill="blue")

print()
input()
quit()
