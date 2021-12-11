import tkinter as tk
plocha=tk.Canvas(bg="black")
plocha.pack()
r=50
plocha.create_oval(100-50,100-50,100+50,100+50,outline="white")
plocha.create_text(100,100,text="kruh",font="Arial 12 bold",fill="white")

print()
input("Pre skončenie stalč ENTER.")
quit()
