# coding=utf-8
from tkinter import *

from tkinter import *
from tkinter.ttk import Panedwindow



root = Tk()
root.minsize(500, 400)
root.maxsize(500, 400)


def kiralayici():
    kiralayiciSayfasi = Tk()
    kiralayiciSayfasi.minsize(400,400)
    #kiralayiciSayfasi.titel('Hos geldin... ')

    lblisim = Label(kiralayiciSayfasi, text="AD SOYAD").pack(padx=10,pady=5,side=TOP)
    txtisim = Entry(kiralayiciSayfasi, width=30).pack(padx=10, pady=1,side=TOP )

    lbltc = Label(kiralayiciSayfasi, text="TC").pack(padx=10, pady=10, side=TOP)
    txttc = Entry(kiralayiciSayfasi, width=30).pack(padx=10, pady=1, side=TOP)

    b2 = Button(kiralayiciSayfasi, text="AL", width=10, command=kiralayici)
    b2.pack(padx=20, pady=50,side=LEFT )
    b3 = Button(kiralayiciSayfasi, text="Iade Et", width=10, command=kiralayici)
    b3.pack(padx=20, pady=50, side=LEFT )

b2 = Button(root, text="Kıralayıcı", width=10, command=kiralayici)
b2.pack(padx=20,pady=50)


def yonetici():
    yoneticiSayfasi = Toplevel()
    yoneticiSayfasi.minsize(400,400)


    # yoneticiSayfasi.titel('Hos geldin (Yönetici)... ')

b1 = Button(root, text="Yöneticin", width=10, command=yonetici)
b1.pack(padx=20,pady=50)






# pan = Panedwindow(root, orient=HORIZONTAL)
# pan.pack(fill=BOTH, expand=True)
# f1 = frame(pan, width=200, height=400, relief=SUNKEN)
# f2 = frame(pan, width=200, height=400, relief=SUNKEN)
# pan.add(f1, weight=2)
# pan.add(f1, weight=4)



mainloop()
