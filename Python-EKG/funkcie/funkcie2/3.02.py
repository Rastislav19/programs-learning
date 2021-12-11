import random
def PIN():
    kód=[]
    for i in range(3):
        číslo=random.randit(0,9)
        kód.append(číslo)
    return kód
tip=int(input("Zadaj PIN kód (štvorciferné číslo): "+"\n")))
if tip==PIN():
    print("PIN je správny.")
else:
    for i in range(2):
        if i==0:
            print("PIN je nesprávny. Skúste to znova. Ostávajú Vám ešte",i+1,"pokusi.")
            tip=int(input("Zadaj PIN kód (štvorciferné číslo): "+"\n")))

        elif i==1:
            print("PIN je nesprávny. Skúste to znova. Ostávajú Vám ešte",i+1,"pokus.")
        else:
            print("Karta bola zablokovaná!!")
