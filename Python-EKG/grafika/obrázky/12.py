import tkinter as tk
import random
plocha=tk.Canvas(width=1000,height=600)
plocha.pack()

x=10
sx1=35
sy1=35
sx2=85
sy2=35
sx3=60
sy3=60
sx4=60
sy4=85
for i in range(4):
    farba=f"#{random.randrange(256**3):06x}"
    plocha.create_rectangle(x,10,x+100,110,fill=farba)
    r=random.randint(5,20)
    farba=f"#{random.randrange(256**3):06x}"
    plocha.create_rectangle(sx1-r,sy1-r,sx1+r,sy1+r,fill=farba)
    plocha.create_rectangle(sx2-r,sy2-r,sx2+r,sy2+r,fill=farba)
    r=random.randint(5,10)
    farba=f"#{random.randrange(256**3):06x}"
    plocha.create_rectangle(sx3-r,sy3-r,sx3+r,sy3+r,fill=farba)
    r=random.randint(10,20)
    farba=f"#{random.randrange(256**3):06x}"
    plocha.create_rectangle(sx4-r,sy4-r/2,sx4+r,sy4+r/2,fill=farba)
    x+=120
    sx1+=120
    sx2+=120
    sx3+=120
    sx4+=120

print()
input()
quit()
