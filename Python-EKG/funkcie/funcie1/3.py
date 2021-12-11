def súčet(a,b):
    výsledok=a+b
    return výsledok

def rozdiel(a,b):
    return a-b

def súčin(a,b):
    return a*b

def podiel(a,b):
    return a/b

def priemer(a,b):
    return (a+b)/2

a=float(input("Zadaj prvé číslo:"+"\n"))
b=float(input("Zadaj druhé číslo:"+"\n"))
print()
print("Súčet čísel je=",súčet(a,b))
print("Rozdiel čísel je=",rozdiel(a,b))
print("Súčin čísel je=",súčin(a,b))
print("Podiel čísel je=",podiel(a,b))
print("Priemer čísel je=",priemer(a,b))

print()
input("Pre skončenie stlač ENTER.")
quit()
