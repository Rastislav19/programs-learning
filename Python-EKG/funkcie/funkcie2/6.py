xa=float(input("Zadaj x-ovú súradnicu bodu A:"+"\n"))
ya=float(input("Zadaj y-ovú súradnicu bodu A:"+"\n"))
xb=float(input("Zadaj x-ovú súradnicu bodu B:"+"\n"))
yb=float(input("Zadaj y-ovú súradnicu bodu B:"+"\n"))
print()
xu=xa-xb
yu=ya-yb
print("Súradnice vektora AB=["+str(xu)+","+str(yu)+"]")
print("Veľkosť vektora AB:",(xu**2+yu**2)**(1/2))
print("Parametrické vyjadrenie priamky AB:")
print("x =",xa,"+",xu,"* t")
print("y =",ya,"+",yu,"* t")
c=-(-yu*xa+xu*ya)
print("Všeobecná rovnica priamky AB:")
print(str(-yu)+"x +",str(xu)+"y +",c,"= 0")
if -yu==0:
    px="Nemá priesečník osi x."
else:
    px=-c/-yu
if xu==0:
    py="Nemá prisečník osi y."
else:
    py=-c/xu
print("Px=["+str(px)+",0]")
print("Py=[0,"+str(py)+"]")

print()
input("Pre skončenie stlačte ENTER")
quit()
