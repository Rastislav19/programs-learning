a=int(input("Zadaj dĺžku v metroch: "+"\n"))
b=int(input("Zadaj dĺžku v metroch: "+"\n"))
c=int(input("Zadaj dĺžku v metroch: "+"\n"))

if a+b>c and a+c>a and a+c>b:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a:
        print("Je v tvare pravoúhleho trojuholníka.")
    else:
        print("Nie je v tvare pravoúhleho trojuholínka.")
    o=a+b+c
    e=o*3.5
    s=(a+b+c)/2
    S=(s*(s-a)*(s-b)*(s-c))**(1/2)
    hnojivo=S/3.5
    E=hnojivo*1.8
    print("Na oplotenie je potreba",round(o,2),"metrov pletiva. Stáť to bude:",round(e,2),"€.")
    print("Rozloha záhradky je",round(S,2),"metrov štvorcových. Bude treba na to",round(hnojivo,2),"10 litrových hnojív. Stáť to bude:",round(E,2),"€.")
else:
    print("Nie je v tvare trojuholníka. Zadaj iné údaje.")

print()
input("Pre skončenie stlačte ENTER.")
quit()
