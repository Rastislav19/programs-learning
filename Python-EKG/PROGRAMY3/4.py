def cif_sucet(číslo):
    zoznam=[]
    for i in číslo:
        zoznam.append(int(i))
    return sum(zoznam)
číslo=input("Zadaj číslo:"+"\n")
print("Ciferný súčet zadaného čísla je:",cif_sucet(číslo))

print()
input("Pre skončenie stlač ENTER.")
quit()
