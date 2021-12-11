import random
print("Vypočítaj!")
správne=0
for i in range(10):
    a=random.randint(1,20)
    b=random.randint(1,20)
    tvoj_vypocet=int(input(str(a)+"+"+str(b)+"="))
    if tvoj_vypocet==(a+b):
        print("Správne!")
        správne+=1
    else:
        print("Nesprávne! Spravny výsledok je:",a+b)
percentá=(správne/10)*100
print()
print("Počet tvojich správnych odpovedí je:",správne,"Je to",percentá,"percent." )

print()
input("Pre skončenie stalč ENTER!")
quit()
