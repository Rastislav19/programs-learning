def obsah_s(a):
    return a*a
def obsah_o(b,c):
    return b*c

a=float(input("Zadaj stranu štvorca a:"+"\n"))
b=float(input("Zadaj stranu obdlžníka b:"+"\n"))
c=float(input("Zadaj stranu obdlžníka c:"+"\n"))

if a<=0 or b<=0 or c<=0:
    print("Chyba! Strany musia byť kladné.")
else:
    Os=obsah_s(a)
    Oo=obsah_o(b,c)
    if Os == Oo:
        print("Obsahy sa rovnajú.")
    else:
        if Os > Oo:
            print("Obsah štvorca je väčší.")
        else:
            print("Obsah obdĺžníka je väčší.")

print()
input("Pre skončenie stlačte ENTER")
quit()
