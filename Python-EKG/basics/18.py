krajskémestáSK=["Bratislava","Trnava","Nitra","Trenčín","Žilina","Banská Bystrica","Košice","Prešov"]
print("Dĺžka zoznamu je=",len(krajskémestáSK),"prvkou")
print("Prvý a štvrtý prvok je=",krajskémestáSK[0],"a",krajskémestáSK[3])
del krajskémestáSK[2:5]
print("Zoznam bez prvkov na tretej až piatej pozícii je=",krajskémestáSK)
krajskémestáSK.insert(4,"Paríž")
print("Zoznam po pridaní prvku Paríž na 4. pozíciu je=",krajskémestáSK)
krajskémestáSK.sort()
print("Zoznam podľa abecedy je=",krajskémestáSK)

print()
input("Pre skončenie stalč ENTER.")
quit()
