číslo=input("Zadaj číslo:"+"\n")
prvočísla=[]
for i in číslo:
    i=int(i)
    počet=0
    for deliteľ in range(1,i+1):
        if i%deliteľ==0:
            počet+=1
    if počet==2:
        prvočísla.append(i)
print("Ciferný súčet prvočísel zadaného čísla je:",sum(prvočísla))

print()
input("Pre skončenie stlač ENTER.")
quit()
