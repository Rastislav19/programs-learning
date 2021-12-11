n=int(input("Zadaj prirodzené číslo n: "+"\n"))
print("Párne dvojciferné čísla od 1 do n: ")
if n<100:
    for i in range(10,n+1,2):
        print(i,end=" ")
    print("\n")
    print("Interval od 1 do n neobsahuje žiadne trojciferné čísla.")
else:
    for i in range(10,100,2):
        print(i,end=" ")
    print("\n")
    print("Nepárne trojciferné čísla od 1 do n: ")
    if n<1000:
        for i in range(101,n+1,2):
            print(i,end=" ")
    else:
        for i in range(101,1000,2):
            print(i,end=" ")

print()
input("Pre skončenie stalč ENTER.")
quit()
