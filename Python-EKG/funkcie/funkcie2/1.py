veta=str(input("Zadaj vetu: "+"\n"))
písmená=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Q","Z"]
znak=[".","?","!"]
if veta[0] in písmená and veta[-1] in znak:
    print("Veta je napísaná správne!")
else:
    print("Vo vete sú chyby.")

print()
input("Pre skončenie stlačte ENTER")
quit()
