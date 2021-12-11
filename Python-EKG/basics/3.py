teploty=[10,13,15,18,17,12,12]
print("Súčet teplôt je=",sum(teploty))
print("Minimuj je=",min(teploty))
print("Maximum je=",max(teploty))
print("Priemer teplôt je=",round(sum(teploty)/len(teploty),2))
teploty.sort()
print("Zoradený zoznam je=", teploty)
teploty.reverse()
print("Prevrátený zoznam je=", teploty)

print()
input("Pre skončenie stalč ENTER.")
quit()
