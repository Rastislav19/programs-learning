import random
def farba(f):
    if f==0:
        return "red"
    elif f==1:
        return "white"
    elif f==2:
        return "green"
    elif f==3:
        return "black"
    else:
        return "braun"
for f in range(5):
    print(f+1,".",farba(f))
print()
f= random.randint(1,5) #náhodne si vyberie jednu.
print(f+1,".",farba(f))

print()
input("Pre skončenie stalč ENTER.")
quit()
