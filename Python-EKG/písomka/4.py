def obvod_štvorec(a):
    o_š=4*a
    return o_š
def obvod_obdĺžnik(b,c):
    o_o=2*(a+b)
    return o_o

a=int(input("Zadaj dĺžku strany štvorca:"+"\n"))
b=int(input("Zadaj dĺžku strany obdĺžnika:"+"\n"))
c=int(input("Zadaj dĺžku druhej strany obdĺžnika:"+"\n"))
print()
if obvod_štvorec(a)==obvod_obdĺžnik(b,c):
    print("Obvody sa rovnajú:")
elif obvod_štvorec(a)>obvod_obdĺžnik(b,c):
    print("Obvod obdĺžnika je menší.")
else:
    print("Obvod štvorca je menší.")

print()
input("Pre skončenie stlač ENTER.")
quit()
