import random
heslo=random.randint(1000,9999)
for i in range(1,4):
    tip=int(input("Zadajte PIN:"+"\n"))
    if tip==heslo:
        print("PIN je správny.")
    else:
        if i==3:
            print("Karta je zablokovaná.")
        else:
            print("PIN je nesprávny.")
        ##### iná možnosť
        pokusy=3
        while pokusy>0:
            print("PIN je nesprávny.")
        else:
            print("Karta je zablokovaná.")
print()
input("Pre skončenie stlačte ENTER")
quit()
