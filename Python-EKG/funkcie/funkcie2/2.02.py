def obsah_s(a):
    S=a*a
    return S
def obvod_o(b,c):
    o=b+c
    return o
def porovnanie(S,o):
    if obsah_s(a)>obvod_o(b,c):
        print("Obsah štvorca je väčší ako obvod obĺžnika.")
    elif obsah_s(a)<obvod_o(b,c):
        print("Obsah štvorca je menší ako obvod obĺžnika.")
    else:
        print("Obsah štvorca a obvod obdĺžnika sa rovnajú.")
a=float(input("Zadaj dĺžku strany v metroch: "+"\n"))
b=float(input("Zadaj dĺžku strany v metroch: "+"\n"))
c=float(input("Zadaj dĺžku strany v metroch: "+"\n"))
print()
if a and b and c>0:
    print("Obsah štvorca je:",obsah_s(a),"metrov štvorcových.")
    print("Obvod obdĺžnika je:",obvod_o(b,c),"metrov.")
    porovnanie(a*a,b+c)
else:
    print("Chyba!! Čísla musia byť kladné.")

print()
input("Pre skončenie stlač ENTER.")
quit()
