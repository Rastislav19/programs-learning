diktát=input("Zadajte text: "+"\n")
for i in diktát:
    if i=="y" or i=="ý" or i=="i" or i=="í":
        diktát=diktát.replace(i,"_")
print(diktát)

print()
input("Pre skončenie stalč ENTER.")
quit()
