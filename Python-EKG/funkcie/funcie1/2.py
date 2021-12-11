def prevod(euro):
    koruny=round(euro*27.02,2)
    return koruny
euro=float(input("Zadaj sumu v €:"+"\n"))
print("Máš",prevod(euro),"korún.")
print()
def prevod(euro):
    return round(euro*27.02,2)
euro=float(input("Zadaj sumu v €:"+"\n"))
print("Máš",prevod(euro),"korún.")

print()
input("Pre skončenie stlač ENTER.")
quit()
