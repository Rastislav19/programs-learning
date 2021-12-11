def objem_kocka(a):
    o1=a*a*a
    return o1
def objem_kvader(b,c,d):
    o2=b*c*d
    return o2
a=int(input("Zadaj dĺžku strany:"+"\n"))
b=int(input("Zadaj dĺžku strany:"+"\n"))
c=int(input("Zadaj dĺžku strany:"+"\n"))
d=int(input("Zadaj dĺžku strany:"+"\n"))
print("Objem kocky je:",objem_kocka(a))
print("Objem kvádra je:",objem_kvader(b,c,d))
if objem_kocka(a)>objem_kvader(b,c,d):
    print("Objem kocky je väčší než objem kvádra.")
elif objem_kocka(a)<objem_kvader(b,c,d):
    print("Objem kocky je menší než objem kvádra.")
else:
    print("Objemy sa rovnajú.")

print()
input("Pre skončenie stlač ENTER.")
quit()
