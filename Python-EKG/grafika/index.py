import tkinter
plocha= tkinter.Canvas(bg="red",width="750",height="500") #vytvoriť plátno (môžeme meniť rozmery a farby)
plocha.pack() #zobraziť plátno

plocha.create_line(10,10,100,100,50,150,10,10,width="15",fill="green")
plocha.create_rectangle(50,100,150,150,fill="", width="5",outline="blue") #fill=""-> bude priesvitný

f"#{random.randrange(256**3):06x}"#randomná farba

plocha.create_oval(50,100,150,150,width="3",outline="blue",fill="red")
plocha.create_rectangle(50,100,150,150)

plocha.create_oval(x-r,y-r,x+r,y+r)#kružnica

plocha.create_polygon()#uholník

x=150#súradnice stredu
y=100#súradnice stredu
plocha.create_text(x,y,text="Ahoj",fill="blue",font="Arial 15 italic",angle="14")#písnie textu do grafickej plochy



print()
input("Preskončenie stlač ENTER.")
quit()
