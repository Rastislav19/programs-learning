A=int(input("Zadaj prirodzené číslo:"+"\n"))
zoznam=[]
for i in range(1,A+1):
    zoznam.append(i)
print(zoznam)
print(zoznam[2:(A+1):3])
print(zoznam[::-1])

print()
input("Pre skončenie stlač ENTER.")
quit()
