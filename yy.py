import tkinter
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
root.title("Biseklet Kiralama ...")

# logo = PhotoImage(file = 'resim.jpg')
# background_label = Label(root, image=logo)
# background_label.image = logo
# background_label.place(x=2, y=2, relwidth=1, relheight=1)



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
    b2.grid(row=5,column=1)
    b3 = Button(kiralayiciSayfasi, text="Iade Et", width=10, command=iade)
    b3.grid(row=5,column=3)


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
    print(veriler[0][2][1])

    a = veriler[0][2][0]
    b = veriler[0][2][1]
    c = a + b #Girissaat
    c=int(c)
    print(c)

    f = veriler[0][2][3]
    t = veriler[0][2][4]
    d = f + t  # giris dakika kısmı
    d = int(d)
    print(d)

    cikisZamani = time.strftime("%H %M") #cikis SAAT
    saat1 = cikisZamani[0]
    saat2 = cikisZamani[1]
    saat = saat1 + saat2
    saat = int(saat)#cikis SAAT
    print(saat)

    dakika1 = cikisZamani[3]
    dakika2 = cikisZamani[4]
    dakika = dakika1 + dakika2
    dakika = int(dakika)
    print(dakika)

    saat_farkı = 0
    dakika_farkı = 0
    toplam_saat = 0
    if saat > c:
        if dakika > d:
            dakika_farkı = dakika - d
            saat_farkı = saat - c
            toplam_dakika = (saat_farkı * 60) + dakika_farkı
            toplam_saat = toplam_dakika / 60
        elif dakika < d:
            dakika_farkı = (dakika + 60) - d
            saat = saat - 1
            saat_farkı = saat - c
            toplam_dakika = (saat_farkı * 60) + dakika_farkı
            toplam_saat = toplam_dakika / 60


    elif saat < c:
        if dakika > d:
            dakika_farkı = dakika - d
            saat_farkı = (24 - c) + saat
            toplam_dakika = (saat_farkı * 60) + dakika_farkı
            toplam_saat = toplam_dakika / 60
        elif dakika < d:
            dakika_farkı = (dakika + 60) - d
            saat = saat - 1
            saat_farkı = (24 - c) + saat
            toplam_dakika = (saat_farkı * 60) + dakika_farkı
            toplam_saat = toplam_dakika / 60

            print(toplam_dakika)
    print("saat farkı:{0}, dakika farkı: {1}, toplam geçen süre saat cinsinden:{2}".format(saat_farkı, dakika_farkı,
                                                                                           toplam_saat))

    toplam_saat = float(toplam_saat)

    sonsonuc = toplam_saat * 4.0  # bir saatlik ucreti 4 TL dir
    # sonsonuc=float(sonsonuc)
    sonsonuc = round(sonsonuc, 2)
    print(sonsonuc)



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

    im.execute("DELETE FROM kiralayicilar where Tc=(?)", [txttc.get()])
    vt.commit()


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
