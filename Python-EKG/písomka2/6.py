import tkinter as tk
plocha=tk.Canvas(width=200,height=150,bg="white")
plocha.pack()
plocha.create_oval(10,40,190,110,fill="green")
plocha.create_text(95,75,text="08:21",font="Arial 35")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
