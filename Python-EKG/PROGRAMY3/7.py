číslo=int(input("Zadaj číslo:"+"\n"))
počet=0
for i in range(1,číslo+1):
    if číslo%i==0:
        počet+=1
if číslo==1:
    print("Zadané číslo je jednotka")
elif počet==2:
    print("Zadané číslo je prvočíslo.")
elif len(str(číslo))>1:
    print("Zadané číslo je zložené číslo.")
else:
    "Zadané číslo nie je 1,ani prvočíslo a ani zložené číslo."

print()
input("Pre skončenie stlač ENTER.")
quit()
