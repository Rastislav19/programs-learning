abc=["raz","dva","tri"]
print("Zoznam abc=",abc)
abc.append("koniec")
print("Zoznam po pridaní prvku koniec na koniec=",abc)
abc.insert(2,"stred")
print("Zoznam po pridaní prvku stred na pozíciu 2=",abc)
abc.insert(0,"začiatok")
print("Zoznam po pridaní prvku začiatok na začiatok=",abc)
abc.insert(5,"preposledný")
print("Zoznam po pridaní prvku predposledný pred posledný prvok=", abc)

print()
input("Pre skončenie stalč ENTER.")
quit()
