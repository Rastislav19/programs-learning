import socket as s
host=input("Zadaj doménu stránky:"+"\n")
print(f"IP of {host} is {s.gethostbyname(host)}")

print()
input("Pre skončenie programu stlač ENTER.")
quit()
