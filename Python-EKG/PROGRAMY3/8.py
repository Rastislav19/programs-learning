text=input("Zadaj text:"+"\n")
zoznam=["y","ý","Ý","Y","i","í","Í","I"]
for i in text:
    if i in zoznam:
        text=text.replace(i,"_")
print(text)

print()
input("Pre skončenie stlač ENTER.")
quit()
