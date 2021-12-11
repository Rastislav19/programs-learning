veta=input("Zadaj vetu: "+"\n")
print()
if "." in veta:
    print("Veta je oznamovacia.")
elif "?" in veta:
    print("Veta je opytovacia.")
elif "!" in veta:
    print("Veta je rozkazovacia.")
else:
    print("Error!!! Veta neobsahuje interpunkčné znamienko (./?/!).")
print()
samohlásky=0
zoznam_samohlások=["a","á","ä","e","é","i","í","o","ó","ô","u","ú","ia","ie","iu"]
for i in veta:
    if i in zoznam_samohlások:
        samohlásky+=1
        veta=veta.replace(i,"*")

print("Počet samohlások je:",samohlásky)
print()
print(veta)

print()
input("Pre skončenie stlačte ENTER.")
quit()
