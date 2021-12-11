for i in range(5):
    print("Učím sa programovať v Pythone.")
    print("Ide mi to veľmi dobre.")
#
i=1
while i<6: #i<=5je to to isté
    print("Učím sa programovať v Pythone.")
    i=i+1 #i+=1 je tiež to isté
#
meno=(input("Zadaj meno: "))
for i in meno:
    print(i,end=" ") #vypíš i a na konci sprav
#
print("\n") #choď na nový riadok
meno=(input("Zadaj meno: "))
dĺžka=len(meno)
for i in range(dĺžka):
    print(i,end=" ")
#
for i in range(10):
    print("Poďme na to!")
#
n=int(input("Zadaj prirodzené číslo n= "))
for i in range(1,n+1):  #alebo range(n)
    print(i,end=" ")
#
n=int(input("Zadaj prirodzené číslo n= "))
súčet=0
for i in range(1,n+1):  #alebo range(n)
    print(i,end=" ")
    súčet=súčet+i
print("Súčet čísel je= ",súčet)
#
