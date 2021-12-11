import random
rok=0
sms=[]
mesiace=["Januári","Februári","Marci","Apríli","Máji","Júni","Júli","Auguste","Septembri","Októbri","Novembri","Decembri"]
for i in mesiace:
    počet_sms=random.randint(0,50)
    if i=="Februári":
        print("Vo",i,"bol počet sms",počet_sms)
    else:
        print("V",i,"bol počet sms",počet_sms)
    sms.append(počet_sms)
priemer=round(sum(sms)/12,2)

print()
print("Priemer sms za mesiac je",priemer)
print("Maximálny počet sms za mesiac je",max(sms),"v",sms.index(max(sms))+1,". mesiaci.")
print("Minimálny počet sms za mesiac je",min(sms),"v",sms.index(min(sms))+1,". mesiaci.")

print()
input("Pre skončenie stlačte ENTER.")
quit()
