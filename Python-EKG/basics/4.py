farby=["biela","modrá","červená","žltá","zelená","čierna"]
print("Dĺžka zozanmu je=",len(farby),"prvkov")
print("Piaty prvok je=",farby[4])
print("Po tretí prvok=",farby[:2])
print("Od druhúho prvku=",farby[1:])
print("Obrátený zoznam je=",farby[::-1])
farby.reverse()
print(farby)
del farby[2:4]
print("Zoznam po vymazaní je=",farby)
farby.append("oranžová")
print("Zoznam po pridaní farby je=", farby)
farby.insert(1,"fialová")
print("Zoznam po pridaní farby je=", farby)
farby.sort()
print("Zoznam podľa abecedy je=", farby)
if "Síva" in farby:
    print("Síva je v zozname.")
else:
    print("Sivá nie je v zozname.")

print()
input("Pre skončenie stalč ENTER.")
quit()
