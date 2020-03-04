import pyqrcode
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox


def create_widget():
    label=Label(text='ENTER THE TEXT HERE:',bg='blue')
    label.grid(row=0,column=1,padx=5,pady=5)

    root.entry=Entry(width=30,textvariable=qrInput)
    root.entry.grid(row=0,column=2,padx=5,pady=5)

    button=Button(text='GENERATE',width=10,command=QRcodeGenerate)
    button.grid(row=0,column=3,padx=5,pady=5)

    root.imagelabel=Label(root,bg='red')
    root.imagelabel.grid(row=2,column=1,columnspan=3,padx=5,pady=5)

def QRcodeGenerate():
    qrString=qrInput.get()

    if qrString!='':
        qrGenerate=pyqrcode.create(qrString)
        path="PATH" #eg: /home/bhushan/Documents/python/qrcode/
        name=path+qrString+'.png'

        qrGenerate.png(name,scale=10)
        #qrGenerate.svg(qrString,scale=5)
        image=Image.open(name)
        #image.show()
        #image=image.resize(400,400,Image.BOX)

        image=ImageTk.PhotoImage(image)

        root.imagelabel.config(image=image)
        root.imagelabel.photo=image
    else:
        messagebox.showerror("error",'enter a text')

root=tk.Tk()

root.title("QR CODE GENERATOR")
root.geometry("600x500")
root.resizable(False,False)
root.config(background='darkolivegreen4')

qrInput=StringVar()
create_widget()
root.mainloop()
