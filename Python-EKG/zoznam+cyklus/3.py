teploty=[10,13,15,18,17,12,12]
for i in teploty:
    priemer=sum(teploty)/len(teploty)
    if i>priemer:
        print(i,"je nadpriemerná teplota.")

print()
input("Pre skončenie stalč ENTER.")
quit()
