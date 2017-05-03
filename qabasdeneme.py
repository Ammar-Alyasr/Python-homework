from Tkinter import*

import os

m = Tk()

m.minsize(300,100)

m. geometry("320x100")

def anasayfa1():
    print ("hello")

photo = PhotoImage(file="ammarik.jpg")
b1 = Button(m,image=photo,text="Button", command=anasayfa1,height=50,width=100)
b1.pack()


photo = PhotoImage(file="ammarik.jpg")
b2 = Button(m,image=photo,text="Button", command=anasayfa1,height=50,width=100)
b2.pack()

m.mainloop()