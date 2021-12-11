import tkinter as tk
plocha=tk.Canvas()
plocha.pack()

plocha.create_text(80,30,text="Python",fill="blue",font="Arial 25 bold")
plocha.create_text(180,50,text="Ahoj",fill="red",font="Arial 25",angle="45")
plocha.create_text(280,80,text="Slnko",fill="yellow",font="Arial 25 italic",angle="-90")

print()
input("Pre skončenie stlač ENTER.")
quit()
