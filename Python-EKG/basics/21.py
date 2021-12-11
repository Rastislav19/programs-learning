domácezvieratá=["pes","mačka","škrečok","sliepka","zajac"]
print("Zoznam domácich zvierat je=",domácezvieratá)
domácezvieratá.insert(0,"Vlk")
domácezvieratá.insert(2,"medveď")
domácezvieratá.append("Jeleň")
print("Zoznam po pridaní 3 lesných zvierat je=",domácezvieratá)
zlep=",".join(domácezvieratá)
print("Zlepený zoznam do reťazca=",zlep)
print("Počet a v reťazci=",zlep.find("a"))
print("Reťazec s vymeneným a za *=",zlep.replace("a","*"))

print()
input("Pre skončenie stalč ENTER.")
quit()
