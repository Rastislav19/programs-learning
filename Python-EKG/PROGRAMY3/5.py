dátum=input("Zadaj dátum svojho narodenia:"+"\n")
zoznam=[]
for i in dátum:
    if i==".":
        zoznam.append(0)
    else:
        i=int(i)
        zoznam.append(i)
osobné_číslo=sum(zoznam)
if 9>=osobné_číslo>=1:
    if osobné_číslo==1:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je: Kritika a férový prístup.")
    elif osobné_číslo==2:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je: Citovo založení spoločník.")
    elif osobné_číslo==3:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je: Tvoriví pohoďák.")
    elif osobné_číslo==4:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je: Práca na prvom mieste.")
    elif osobné_číslo==5:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je: Tvrdohlaví kreatívec.")
    elif osobné_číslo==6:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je: Žiadny stres a konflikty.")
    elif osobné_číslo==7:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je: Disciplinovaní pracant.")
    elif osobné_číslo==8:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je: Dynamickí víťaz.")
    elif osobné_číslo==9:
        print("Tvoje osobné číslo je:",osobné_číslo,"a tvoja charakteristika je:  Pozitívni spoločník.")
else:
    while osobné_číslo>9:
        for i in str(osobné_číslo):
            zoznam1=[]
            i=int(i)
            zoznam1.append(i)
        osobné_číslo=sum(zoznam1)

print()
input("Pre skončenie stalč ENTER.")
quit()
