N=int(input("Zadaj počet príkladov (od 1 do 20): "+"\n"))
if 20>N>0:
    import random
    správne=0
    print("Vypočítaj!")
    for i in range(N):
        a=random.randint(1,9)
        b=random.randint(1,9)
        sucin=int(input(str(a)+"*"+str(b)+"="))
        if sucin==a*b:
            print("Správne!")
            správne+=1
        else:
            print("Nesprávne! Výsledok je: ",a*b)
else:
    print("Error zadaj väčšie číslo ako 0 a menšie ako 20.")
print()
percentá=(správne/N)*100
if správne==1:
    print("Sprváne si vypočítal",správne,"príklad. To je",round(percentá,2),"%.")
elif správne==2 or správne==3 or správne==4:
    print("Sprváne si vypočítal",správne,"príklady. To je",round(percentá,2),"%")
else:
    print("Sprváne si vypočítal",správne,"príkladov. To je",round(percentá,2),"%.")

print()
input("Pre skončenie stlačte ENTER.")
quit()
