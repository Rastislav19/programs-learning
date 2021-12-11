import random
kto=["Martin","Ján","Peter","Petra","Klára"]
s_kým=["s Evou","s Antonom","s Milanom","s Janou","s Jozefom"]
kedy=["včera","dnes","ráno","poobede","večer","v noci"]
kde=["doma","vonku","v škole","v posteli","v kine"]
čo_robili=["písali","kreslili","sa učili","ležali","čítali"]
print(random.choice(kto),random.choice(s_kým),random.choice(kedy),random.choice(kde),random.choice(čo_robili))

print()
input("Pre skončenie stlačte ENTER.")
quit()
