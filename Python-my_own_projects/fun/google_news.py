from GoogleNews import GoogleNews
googlenews=GoogleNews(period="7d")
googlenews.search("Slovakia")
result=googlenews.result()
for i in result:
    print("-"*50)
    print("Názov:",i["title"])
    print("Dátum:",i["date"])
    print("Popis:",i["desc"])
    print("Link:",i["link"])

print()
input("Pre skončenie reportu stlač ENTER.")
quit()
