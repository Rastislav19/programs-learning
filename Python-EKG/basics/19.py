domácezvieratá=["pes","mačka","škrečok","sliepka","zajac"]
print("Zoznam domácich zvierat je=",domácezvieratá)
print("Prvé a poslené zviera zo zonamu je=",domácezvieratá[0],"a",domácezvieratá[4])
domácezvieratá.insert(0,"Vlk")
domácezvieratá.insert(2,"medveď")
domácezvieratá.append("Jeleň")
print("Zoznam po pridaní 3 lesných zvierat je=",domácezvieratá)
print("Počet zvierat v zozname je=",len(domácezvieratá))
if "krava" in domácezvieratá:
    print("Krava je v zozname.")
else:
    print("Krava nie je v zozname.")
print("Zoznam v opačnom poradí je=",domácezvieratá[::-1])

print()
input("Pre skončenie stalč ENTER.")
quit()
