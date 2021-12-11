text=input("Zadaj text:"+"\n")
def počet_číslic(text):
    počet_čísel=0
    for i in list(text):
        if i<=str(9) and i>=str(0):
            počet_čísel+=1
    return počet_čísel
def počet_malých(text):
    počet_m_písmen=0
    for i in list(text):
        if ord(i)>=97 and ord(i)<=122:
            počet_m_písmen+=1
    return počet_m_písmen
def počet_veľkých(text):
    počet_v_písmen=0
    for i in list(text):
        if ord(i)>=65 and ord(i)<=90:
            počet_v_písmen+=1
    return  počet_v_písmen

print("Počet číslic je:",počet_číslic(text))
print("Počet malých písmen je:",počet_malých(text))
print("Počet veľkých písmen je:",počet_veľkých(text))

print()
input("Pre skončenie stlač ENTER.")
quit()
