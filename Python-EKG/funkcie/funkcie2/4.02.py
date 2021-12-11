rodné_číslo=input("Zadajte rodné číslo:"+"\n")
if int(rodné_číslo)%11==0:
    print("Rodné číslo je neplatné lebo nie je deliteľné 11.")
else:
    if int(rodné_číslo[2])>2:
        print("Používateľ je žena.")
    else:
        print("Používateľ je muž.")
    if int(rodné_číslo[2:4])> 20:
        mesiac=int(rodné_číslo[2:4])-50
    else:
        mesiac=int(rodné_číslo[2:4])
    deň=int(rodné_číslo[4:6])
    print("Dátum narodenia:",str(deň)+"."+str(mesiac)+"."+rodné_číslo[0:2])

print()
input("Pre skončenie stlačte ENTER")
quit()
