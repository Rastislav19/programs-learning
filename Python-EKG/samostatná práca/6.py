import random
počet_hodov=int(input("Zadaj počet hodov kockami: "+"\n"))
print()
hody=[]
for i in range(počet_hodov):
    kocka1=random.randint(1,6)
    kocka2=random.randint(1,6)
    print(i+1,".hod. Súčet bodov na kockách: ",kocka1+kocka2)
    hody.append(kocka1+kocka2)
print()
súčet2=0
súčet3=0
súčet4=0
súčet5=0
súčet6=0
súčet7=0
súčet8=0
súčet9=0
súčet10=0
súčet11=0
súčet12=0
for i in hody:
    if i==2:
        súčet2+=1
    elif i==3:
        súčet3+=1
    elif i==4:
        súčet4+=1
    elif i==5:
        súčet5+=1
    elif i==6:
        súčet6+=1
    elif i==7:
        súčet7+=1
    elif i==8:
        súčet8+=1
    elif i==9:
        súčet9+=1
    elif i==10:
        súčet10+=1
    elif i==11:
        súčet11+=1
    elif i==12:
        súčet12+=1
print("Súčet 2 padol",súčet2,"-krát.")
print("Súčet 3 padol",súčet3,"-krát.")
print("Súčet 4 padol",súčet4,"-krát.")
print("Súčet 5 padol",súčet5,"-krát.")
print("Súčet 6 padol",súčet6,"-krát.")
print("Súčet 7 padol",súčet7,"-krát.")
print("Súčet 8 padol",súčet8,"-krát.")
print("Súčet 9 padol",súčet9,"-krát.")
print("Súčet 10 padol",súčet10,"-krát.")
print("Súčet 11 padol",súčet11,"-krát.")
print("Súčet 12 padol",súčet12,"-krát.")

print()
input("Pre skončenie stlačte ENTER.")
quit()
