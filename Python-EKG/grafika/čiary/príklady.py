import tkinter
import random
plocha= tkinter.Canvas(bg="black") #vytvoriť plátno (môžeme meniť rozmery a farby)
plocha.pack() #zobraziť plátno
for i in range(100):
    x=random.randint(20,300)
    y=random.randint(20,300)
    plocha.create_line(0,0,x,y,fill="yellow")

print()
input("Pre skončenie stlač ENTER.")
quit()
