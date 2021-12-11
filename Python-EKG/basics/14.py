písmená=["a","b","c","d","a","b","A"]
print("Zoznam písmená=",písmená)
písmená.append("e")
print("Zoznam po pridaní prvku e na koniec=",písmená)
písmená.remove("c")
print("Zoznam po odstaránení prvku c=",písmená)
početa=písmená.count("a") #môžeme spraviť premennú ktorú tam vložime, keďže tám nemôžeme vložiť celý kód
print("Počet prvkou a v zozname=",početa)
písmená.pop() #maže posledný znak, keď je prázny, alebo na určitej pozícii
print("Zoznam po odstránení posledného prvku=",písmená)
písmená.remove("a")
print("zoznam po odstránení prvku a=",písmená)

print()
input("Pre skončenie stalč ENTER.")
quit()
