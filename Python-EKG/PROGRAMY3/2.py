def asci(slovo):
    tabuľka=[]
    for i in slovo:
        číslo=ord(i)
        tabuľka.append(číslo)
    return tabuľka
slovo=input("Zadaj slovo:"+"\n")
print(asci(slovo))

print()
input("Pre skončenie stlač ENTER.")
quit()
