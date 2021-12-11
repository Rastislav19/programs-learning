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

for i in range(2,13):
    print("Súčet",i,"padol",hody.count(i),"-krát.")

print()
input("Pre skončenie stlačte ENTER.")
quit()
