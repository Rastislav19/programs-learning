slovo=input("Napíš slovo (bez diakritiky):"+"\n")
N=int(input("Zadaj o koľko znakov má nastať posun:"+"\n"))
abeceda=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
šifra=[]
for i in slovo:
    veľké_písmeno=i.upper()
    písmeno=abeceda.index(veľké_písmeno)
    písmeno+=N
    zašifrované_písmeno=abeceda[písmeno]
    šifra.append(zašifrované_písmeno)
zlep="".join(šifra)
print(zlep)

print()
input("Pre skončenie stlač ENTER.")
quit()
