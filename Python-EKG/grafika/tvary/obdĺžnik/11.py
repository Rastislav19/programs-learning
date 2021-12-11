import tkinter
import random
plocha=tkinter.Canvas()
plocha.pack()

for i in range(3):
    hrúbka=random.randint(1,5)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    farba=f'#{r:02x}{g:02x}{g:02x}'
    bg_farba=f'#{r:02x}{g:02x}{g:02x}'
    if i==0:
        plocha.create_rectangle(10,10,60,60,width=hrúbka,fill=bg_farba,outline=farba)
    elif i==1:
        plocha.create_rectangle(20,20,50,50,width=hrúbka,fill=bg_farba,outline=farba)
    else:
        plocha.create_rectangle(30,30,40,40,width=hrúbka,fill=bg_farba,outline=farba)

print()
input("Pre skončenie stlač ENTER.")
quit()
