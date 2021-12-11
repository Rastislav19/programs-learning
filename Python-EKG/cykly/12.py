n=int(input("Zadaj prirodzené číslo n: "+"\n"))
faktoriál=1
for i in range(n,1,-1):
    faktoriál*=i
print("Faktoriál čísla je: ",faktoriál)

print()
input("Pre skončenie stalč ENTER.")
quit()
