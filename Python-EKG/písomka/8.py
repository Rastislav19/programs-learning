známky=[]
dvojky=0
trojky=0
for i in range(8):
    známka=int(input("Zadaj známku (od 1 do 5):"+"\n"))
    známky.append(známka)
    if známka>2:
        dvojky+=1
    elif známka>3:
        trojky+=1
priemer=round(sum(známky)/8,2)
print()
if 1.5>=priemer>=1 and dvojky==0:
    print("Prospel s vyznamenaním! Priemer je:",priemer)
elif 2.0>=priemer>1.5 and trojky==0 or dvojky>0:
    print("Prospel veľmi dobre! Priemer je:",priemer)
elif 5>priemer>2.0 or trojky>0:
    print("Prospel! Priemer je:",priemer)
else:
    print("Neprospel! Priemer je",priemer)

print()
input("Pre skončenie stlač ENTER.")
quit()
