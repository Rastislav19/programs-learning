reťazec=input("Zadaj príklad:"+"\n")
znamienka=["*","/","+","-"]
for i in reťazec:
    if i in znamienka:
        a=reťazec.replace(i,"_")
print(a)

print()
input("Pre skončenie stalč ENTER.")
quit()
