zoznam=[3,4,5,6,-3]
slova=["mama","tec","syn"]
mix=[3, "dom", ["a","b"]]
zoznam[0]
zoznam[-1]
a=["Jana","Peter", "Ivana", "Lucia", "Michal"]
print(a[2:4])
print(a[1:5:2]) #každú druhú
print(a[1:]) #po koniec
print(a[:4])
print(a[::-1]) #odzadu
a=[1, 2, 3, 5, 4]
len(a) #koľko prvkov je v zozname
min(a) #najmenšia hodnota
max(a) #najväčšia hodnota
sum(a) #súčet všetkých hodnôt
a.sort() #zoradí zoznam od najmenšieho

del a[2]
print(a)

zlep=",".join(domácezvieratá)#zlepí všetky prvky zo zoznamu do jedného textu a rozdelí ho čiarkou
zlep.replace("a","*") #vymení každé a v texte za *

import math
math.sqrt(a)#vypočíta odmocninu

def kresli(): #zadefinuje funkciu
     print("***")
kresli() #spustí funkciu

def kresli(číslo): #zadefinuje funkciu
    print("*"*číslo) #zopakuje to niekoľko krát v riadku
kresli(3) #za hodnotu číslo zadá 3
