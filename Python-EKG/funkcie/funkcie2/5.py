def rovnica(a,b,c):
    if a==0:
        print("Nie je to lieneárna rovnica!")
    else:
        x=(c-b)/a
    return x
a=int(input("Zadaj hodnotu a:"+"\n"))
b=int(input("Zadaj hodnotu b:"+"\n"))
c=int(input("Zadaj hodnotu c:"+"\n"))
print("Hodnota x=",roud(rovnica(a,b,c),2))

print()
input("Pre skončenie programu stlač ENTER.")
quit()
