teploty=[10,13,15,18,17,12,12]
print("Súčet teplôt je=",sum(teploty))
print("Minimum je=",min(teploty))
print("Maximum je=",max(teploty))
print("Priemerná teplota je=",round(sum(teploty)/len(teploty),2)) #pri round musíme na 2 pozícii uviesť na koľko desatinných miest

print()
input("Pre skončenie stalč ENTER.")
quit()
