počet=int(input("Zadaj počet teplôt:"+"\n"))
teploty=[]
for I in range(počet):
    teploty.append(input("Zadaj teplotu:"+"\n"))
deň=0
for i in teploty:
    print(str(deň)+". deň",i)
    deň+=1

print()
input("Pre skončenie stalč ENTER.")
quit()
