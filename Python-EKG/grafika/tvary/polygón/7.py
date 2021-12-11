import tkinter as tk
plocha=tk.Canvas(height=1000,width=1000)
plocha.pack()
#okres Poprad
plocha.create_rectangle(10,10,110,60,fill="white",outline="black")
plocha.create_rectangle(13,13,108,58,fill="blue",outline="")
plocha.create_text(60,25,text="OKRES",font="Arial 15 bold",fill="white")
plocha.create_text(60,45,text="POPRAD",font="Arial 15 bold",fill="white")
#maximálna rýchlosť 30
plocha.create_oval(60-50,115-50,60+50,115+50,fill="white",outline="black")
plocha.create_oval(60-45,115-45,60+45,115+45,fill="red",outline="")
plocha.create_oval(60-35,115-35,60+35,115+35,fill="white",outline="")
plocha.create_text(60,115,text="30",font="Arial 40 bold")
#maximálna rýchlosť 80 od-do
plocha.create_rectangle(55,170,65,360,fill="grey")
plocha.create_oval(60-50,220-50,60+50,220+50,fill="white",outline="black")
plocha.create_oval(60-45,220-45,60+45,220+45,fill="red",outline="")
plocha.create_oval(60-35,220-35,60+35,220+35,fill="white",outline="")
plocha.create_text(60,220,text="80",font="Arial 40 bold")
plocha.create_rectangle(10,270,110,340,fill="white",width="3")
plocha.create_text(60,305,text="20:00-06:00",font="Arial 13")
#Nemocnica
plocha.create_rectangle(10,370,110,470,fill="white")
plocha.create_rectangle(13,373,107,467,fill="blue")
plocha.create_text(60,450,text="NEMOCNICA",fill="white",font="Arial 10 bold")
plocha.create_text(60,410,text="H",fill="white",font="Arial 60 bold")
#prudké klesanie
plocha.create_polygon(10,580,60,480,110,580,fill="white",outline="black")
plocha.create_polygon(15,577,60,485,105,577,fill="red",outline="")
plocha.create_polygon(30,565,60,510,90,565,fill="white",outline="")
plocha.create_polygon(33,563,42,550,87,563,fill="black")
plocha.create_text(60,548,text="12%",angle="-18")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
