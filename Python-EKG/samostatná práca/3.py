import random
veľké_písmená=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","Y","X","Y","Z"]
malé_písmená=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","y","x","y","z"]
znak=["*","$","@","#","/","+"]
číslice=["0","1","2","3","4","5","6","7","8","9"]
for i in range(24):
    heslo=[]
    for i in range(2):
        heslo1=random.choice(veľké_písmená)
        heslo.append(heslo1)
    for i in range(3):
        heslo2=random.choice(malé_písmená)
        heslo.append(heslo2)
    for i in range(2):
        heslo3=random.choice(číslice)
        heslo.append(heslo3)
    for i in range(1):
        heslo4=random.choice(znak)
        heslo.append(heslo4)
    zlep="".join(heslo)
    print(zlep)

print()
input("Pre skončenie stlačte ENTER.")
quit()
