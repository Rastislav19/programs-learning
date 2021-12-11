import tkinter
plocha=tkinter.Canvas(bg="red",width="600",height="400") #vytvoriť plátno (môžeme meniť rozmery a farby)
plocha.pack() #zobraziť plátno
a=10,10
b=210,10
d=10,110
f=250,100
plocha.create_line(a,b,width="5",fill="white")
plocha.create_line(a,d,width="10",fill="brown")
plocha.create_line(a,f,width="3",fill="purple")

print()
input("Preskončenie stlač ENTER.")
quit()
