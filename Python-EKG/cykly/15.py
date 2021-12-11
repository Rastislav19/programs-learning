n=int(input("Zadaj n: "))
print(" /││││││\ ")
for i in range(n):
    print("││  ││  ││") #budova s oknami
    print("││││││││││") #ak posuniem tak bude iba spodné poschodie

for i in range(6): #6 krát sa ma to opýta
    meno=input("Ako sa voláš? ") #vymením s prvím 6 krát ma pozdraví.
    print("Ahoj",meno)
print("Ďalších už nezdravím.")

n=random.randrange(10)
for i in range(n):
    x=int(input("Zadaj n: "))
    print(x)

print()
input("Pre skončenie stalč ENTER.")
quit()
