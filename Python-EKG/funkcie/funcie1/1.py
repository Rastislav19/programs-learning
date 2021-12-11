
def stromček(číslo):
    for i in range(číslo):
        for i in range(3):
            print("  *  ")
            print(" *** ")
            print("*****")
        print("  |  ")
        print("  |  ")
        print("__|__")
        print()

stromček(int(input("Zadaj počet stromčekov:"+"\n")))

print()
input("Pre skončnie stlač ENTER.")
quit()
