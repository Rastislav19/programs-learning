from tkinter import *
from tkinter import messagebox
import pyqrcode
import os
window=Tk()
window.title("QR code generator")

def generate():
    if len(subject.get())!=0:
        global myQR
        myQR=pyqrcode.create(subject.get())
        qrimage=myQR.xbm(scale=6)
        global photo
        photo=BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Error!","Please enter the subject!")
    try:
        showCode()
    except:
        pass

def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="Showing QR code for: "+subject.get())

def save():
    direction=path1=os.getcwd()+"\\QR Codes"
    if not os.path.exists(direction):
        os.makedirs(direction)
    try:
        if len(name.get()!=0):
            qrImage=myQr.png(os.path.join(direction, name.get()+".png"),scale=6)
        else:
            messagebox.showinfo("Error!","File name can not be empty!")
    except:
        messagebox.showinfo("Error!","Please generate the code first!")

lab1=Label(window, text="Enter subject",font=("Helvetica",12))
lab1.grid(row=0,column=0,sticky=N+S+E+W)

lab2=Label(window, text="Enter file name",font=("Helvetica",12))
lab2.grid(row=1,column=0,sticky=N+S+E+W)

subject=StringVar()
subjectEntry=Entry(window,textvariable=subject, font=("Helvetica",12))
subjectEntry.grid(row=0,column=1,sticky=N+S+E+W)

name=StringVar()
nameEntry=Entry(window,textvariable=name, font=("Helvetica",12))
nameEntry.grid(row=1,column=1,sticky=N+S+E+W)

createButton=Button(window,text="Create QR code",
                font("Helvetica",12), width=15,command=generate)
createButton.grid(row=0,column=3,sticky=N+S+E+W)
notificationLabel=Label(window)
notificationLabel.grid(row=2,column=1,sticky=N+S+E+W)

subLabel=Label(window,text="")
subLabel.grid(row=3,column=1,sticky=N+S+E+W)

showButton=Button(window,text="Save as PNG",
                font("Helvetica",12),width=15,command=save)
showButton.grid(row=1,column=3,sticky=N+S+E+W)
totalRows=3
totalCols=3
for row in range(totalRows+1):
    window.grid_rowconfigure(row,weight=1)
for col in range(totalCols+1):
    window.grid_colconfigure(col,weight=1)
window.mainloop()
