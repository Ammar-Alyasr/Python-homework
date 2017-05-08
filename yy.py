from tkinter import *
from tkinter import Message
import time, locale
import sqlite3
from tkinter.ttk import Panedwindow

vt = sqlite3.connect("dukkan.db")
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS kiralayicilar(adSoyad,Tc,saat)")
root = Tk()
root.minsize(500, 400)
root.maxsize(500, 400)
root.title("Bisekletler kıralam için ...")


def kiralayici():
    kiralayiciSayfasi = Tk()
    kiralayiciSayfasi.minsize(400, 400)
    kiralayiciSayfasi.maxsize(400, 400)
    kiralayiciSayfasi.title('Hos geldin... ')

    global txtisim, txttc
    lblisim = Label(kiralayiciSayfasi, text="AD SOYAD")
    lblisim.grid(row=0, column=0)

    txtisim = Entry(kiralayiciSayfasi)
    txtisim.grid(row=0, column=1)

    lbltc = Label(kiralayiciSayfasi, text="TC")
    lbltc.grid(row=1, column=0)

    txttc = Entry(kiralayiciSayfasi)
    txttc.grid(row=1, column=1)

    b2 = Button(kiralayiciSayfasi, text="AL", width=10, command=al)
    b2.grid(row=5, column=1)

    b3 = Button(kiralayiciSayfasi, text="Iade Et", width=10, command=iade)
    b3.grid(row=5, column=2)


def al():
    im.execute("INSERT INTO kiralayicilar (adsoyad,Tc,saat) VALUES(?,?,?)",
               (txtisim.get(), txttc.get(), time.strftime("%H:%M:%S")))
    vt.commit()
    im.execute("SELECT * FROM kiralayicilar")
    veriler = im.fetchall()
    print(veriler)


def iade():


    im.execute("SELECT * FROM kiralayicilar WHERE Tc=(?)", [txttc.get()])
    veriler = im.fetchall()
    print(veriler)
    print(veriler[0][2])

    kiralayiciSayfasi3 = Tk()
    lbliade = Label(kiralayiciSayfasi3, text="isim").pack(padx=10, pady=5, side=TOP)
    lbliade = Label(kiralayiciSayfasi3, text=veriler[0][0]).pack(padx=10, pady=5, side=TOP)

    lbliade = Label(kiralayiciSayfasi3, text="baslangic ").pack(padx=10, pady=5, side=TOP)
    lbliade = Label(kiralayiciSayfasi3, text=veriler[0][2]).pack(padx=10, pady=5, side=TOP)

    lbliade = Label(kiralayiciSayfasi3, text="bitis ").pack(padx=10, pady=5, side=TOP)
    lbliade = Label(kiralayiciSayfasi3, text=time.strftime("%H:%M:%S")).pack(padx=10, pady=5, side=TOP)

    b5 = Button(kiralayiciSayfasi3, text="Vazgeç", width=10)
    b5.pack(padx=20, pady=50, side=LEFT)
    b6 = Button(kiralayiciSayfasi3, text="Iade Et", width=10)
    b6.pack(padx=20, pady=50, side=RIGHT)


def yonetici():
    yoneticiSayfasi = Tk()
    yoneticiSayfasi.minsize(400, 400)
    yoneticiSayfasi.maxsize(400, 400)
    yoneticiSayfasi.title('Hos geldin (Yönetici)... ')

    pan = Panedwindow(yoneticiSayfasi, orient=HORIZONTAL)
    pan.pack(fill=BOTH, expand=1)
    f1 = Frame(yoneticiSayfasi, width=200, height=400, relief=SUNKEN)
    f2 = Frame(yoneticiSayfasi, width=200, height=400, relief=SUNKEN)
    pan.add(f1, weight=2)
    pan.add(f2, weight=4)


b2 = Button(root, text="Kıralayıcı", width=10, command=kiralayici)
b2.pack(padx=20, pady=50)

b1 = Button(root, text="Yöneticin", width=10, command=yonetici)
b1.pack(padx=20, pady=50)

mainloop()
