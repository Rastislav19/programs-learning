n=int(input("Zadaj prirodzené číslo n: "+"\n"))
print("Druhé mocniny čísla od 1 do n sú:")
for i in list(range(1,n+1)):
    print(i*i,end=" ")

print()
input("Pre skončenie stalč ENTER.")
quit()
