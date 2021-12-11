print("KENO 10")
tvoj_tip=[]
keno=[]
for i in range(10):
    tvoj_tip.append(int(input("Zadaj číslo od 1 do 50: "+"\n")))
import random
for i in range(10):
    náhoda=random.randint(1,50)
    keno.append(náhoda)
print("Výsledok KENO 10 je: ",keno)
print("Tvoj typ je: ",tvoj_tip)
if keno==tvoj_tip:
    print("Uhádol si! Vyhrávaš!!! Nič...")
else:
    print("Prehral si! Si loser... Skús to ale nabudúce!!!")

print()
input("Pre ukončenie stlačte ENTER:")
quit()
