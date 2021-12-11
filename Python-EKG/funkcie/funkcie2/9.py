import math
def prepona(a,b):
    c=a*a+b*b
    return math.sqrt(c)
a=int(input("Zadaj veľkosť srany: "+"\n"))
b=int(input("Zadaj veľkosť srany: "+"\n"))
print(round(prepona(a,b),2))

print()
input("Pre skončenie stlač ENTER.")
quit()
