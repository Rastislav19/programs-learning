import tkinter as tk
plocha=tk.Canvas(width=200,height=300,bg="white")
plocha.pack()
plocha.create_rectangle(95,10,105,290,fill="brown")
plocha.create_rectangle(10,10,190,60,fill="blue")
plocha.create_text(100,35,text="Bardejov",font="Calibri 25 bold",fill="white")

print()
input()
quit()
