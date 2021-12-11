reťazec=input("Zadaj príklad:"+"\n")
for i in raťazec:
    if i=="/" or i=="*" or i=="+" or i=="-":
        reťazec=reťazec.replace(i,"_")
print(reťazec)

print()
input("Pre skončenie stalč ENTER.")
quit()
