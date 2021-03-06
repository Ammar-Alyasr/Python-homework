import tkinter
from tkinter import *
from tkinter import messagebox
import time, locale
import sqlite3

from tkinter.ttk import Panedwindow


vt = sqlite3.connect("dukkan.db")
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS kiralayicilar(adSoyad,Tc,saat,ucret)")
im.execute("CREATE TABLE IF NOT EXISTS yoneticiler(yoneticiAd, yoneticiSifre)")
im.execute("CREATE TABLE IF NOT EXISTS ucretler(ucret)")
im.execute("INSERT INTO yoneticiler (yoneticiAd,yoneticiSifre) VALUES(?,?)",
           ("root","toor"))
vt.commit()


root = Tk()
root.configure(background="#264d73")
root.minsize(500, 400)
root.maxsize(500, 400)
root.title("Biseklet Kiralama ...")

def kiralayici():
    kiralayiciSayfasi = Tk()
    kiralayiciSayfasi.configure(background="#264d73")
    kiralayiciSayfasi.minsize(400, 300)
    kiralayiciSayfasi.maxsize(400, 300)
    kiralayiciSayfasi.title('Hos geldin... ')

    global txtisim, txttc
    lblisim = Label(kiralayiciSayfasi, text=" AD SOYAD ",bg="#d9d9f2")
    lblisim.grid(row=3, column=3)

    txtisim = Entry(kiralayiciSayfasi)
    txtisim.grid(row=3, column=5)

    lbltc = Label(kiralayiciSayfasi, text="TC",bg="#d9d9f2")
    lbltc.grid(row=5, column=3)

    txttc = Entry(kiralayiciSayfasi)
    txttc.grid(row=5, column=5)

    b2 = Button(kiralayiciSayfasi, text=" AL ", width=15, command=al,bg="#d9d9f2")
    b2.grid(row=6,column=4)
    b3 = Button(kiralayiciSayfasi, text=" Iade Et ", width=15, command=iade,bg="#d9d9f2")
    b3.grid(row=6,column=5)
im.execute("update kiralayicilar set saat=(?)",
                ("09:07:00",))
vt.commit()


def al():

    if(txttc.get()!= ""):
        im.execute("INSERT INTO kiralayicilar (adsoyad,Tc,saat) VALUES(?,?,?)",
                (txtisim.get(), txttc.get(), time.strftime("%H:%M:%S")))
        vt.commit()
        im.execute("SELECT * FROM kiralayicilar")
        veriler = im.fetchall()
        print(veriler)


        kiralayiciSayfasi4= Tk()
        kiralayiciSayfasi4.configure(background='#264d73')
        lblal1 = Label(kiralayiciSayfasi4, text="Başarılı bir şekilde kırallandı,bisiklet kulanabilirsiniz...",font="elephant",bg="#d9d9f2")
        lblal1.pack(padx=7, pady=3, side=TOP)
        lblal = Label(kiralayiciSayfasi4, text="isim",bg="#d9d9f2").pack(padx=10, pady=5, side=TOP)
        lblal= Label(kiralayiciSayfasi4, text=txtisim.get()).pack(padx=10, pady=5, side=TOP)
        lblal = Label(kiralayiciSayfasi4, text=" Saat ",bg="#d9d9f2").pack(padx=10, pady=5, side=TOP)
        lblal = Label(kiralayiciSayfasi4, text=time.strftime("%H:%M:%S")).pack(padx=10, pady=5, side=TOP)
        print(txtisim)
        b5 = Button(kiralayiciSayfasi4, text=" Tamam ", command=quit, width=10,bg="#d9d9f2")
        b5.pack(padx=20, pady=50, side=BOTTOM)
    else:
        messagebox.showerror("Hata", "Dikkat!! TC Kutusu Boş Bırakılamaz!!")

def quit():
    exit()
def iade():
    if(txttc.get()!= ""):
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

        sonsonuc = toplam_saat * 10.0  # bir saatlik ucreti 4 TL dir
        # sonsonuc=float(sonsonuc)
        sonsonuc = round(sonsonuc, 2)
        print(sonsonuc)

        im.execute("INSERT INTO ucretler(ucret) VALUES(?)",
                   (sonsonuc,))
        im.fetchall()


        kiralayiciSayfasi3 = Tk()
        kiralayiciSayfasi3.configure(background="#264d73")
        lbliade = Label(kiralayiciSayfasi3, text=" isim ",bg="#d9d9f2").pack(padx=10, pady=5, side=TOP)
        lbliade = Label(kiralayiciSayfasi3, text=veriler[0][0]).pack(padx=10, pady=5, side=TOP)

        lbliade = Label(kiralayiciSayfasi3, text=" Başlangic Saat ",bg="#d9d9f2").pack(padx=10, pady=5, side=TOP)
        lbliade = Label(kiralayiciSayfasi3, text=veriler[0][2]).pack(padx=10, pady=5, side=TOP)

        lbliade = Label(kiralayiciSayfasi3, text=" Bitiş Saat ",bg="#d9d9f2").pack(padx=10, pady=5, side=TOP)
        lbliade = Label(kiralayiciSayfasi3, text=time.strftime("%H:%M:%S")).pack(padx=10, pady=5, side=TOP)

        lbliade = Label(kiralayiciSayfasi3, text=" Ücret ", bg="#d9d9f2").pack(padx=10, pady=5, side=TOP)
        lbliade = Label(kiralayiciSayfasi3, text=sonsonuc).pack(padx=10, pady=5, side=TOP)

        b5 = Button(kiralayiciSayfasi3, text=" Vazgeç ",command=quit ,width=15,bg="#d9d9f2")
        b5.pack(padx=20, pady=50, side=LEFT)
        b6 = Button(kiralayiciSayfasi3, text=" Iade Et ",command=quit, width=15,bg="#d9d9f2")
        b6.pack(padx=20, pady=50, side=RIGHT)

        im.execute("DELETE FROM kiralayicilar where Tc=(?)", [txttc.get()])
        vt.commit()

    else:
        messagebox.showerror("Hata","Boşluk Bırakılamaz !!")

def yonetici():

    yoneticiSayfasi = Tk()
    yoneticiSayfasi.configure(background="#264d73")
    yoneticiSayfasi.minsize(150, 150)
    yoneticiSayfasi.maxsize(150, 150)
    yoneticiSayfasi.title('Hos geldin (Yönetici)... ')

    global username_guess,password_guess
    username_text = Label(yoneticiSayfasi, text="Kullanci ismi: ", bg="#d9d9f2")
    username_text.grid(row=0, column=5)

    username_guess = Entry(yoneticiSayfasi)
    username_guess.grid(row=2, column=5)



    password_text = Label(yoneticiSayfasi, text="Şifre:", bg="#d9d9f2")
    password_text.grid(row=5, column=5)

    password_guess = Entry(yoneticiSayfasi)
    password_guess.grid(row=7, column=5)
    b=Button(yoneticiSayfasi, text=" GİR ", width=15, bg="#d9d9f2",command=gir)
    b.grid(row=10, column=5)

im.execute("SELECT * FROM yoneticiler")
yontici_Bilgileri = im.fetchall()
print(yontici_Bilgileri[0][0])


def gir():
    im.execute("SELECT * FROM yoneticiler")
    yontici_Bilgileri = im.fetchall()
    print(username_guess.get())
    if (username_guess.get()!= yontici_Bilgileri and password_guess.get()!=yontici_Bilgileri[0][1]):
        messagebox.showinfo("-- HATA --", "Girdiğiniz Bilgiler Hatalıdır...")

    else:
        girsayfasi = Tk()
        girsayfasi.configure(background="#264d73")


        txtToplam= Label(girsayfasi, text="Toplam Elde Edilen", bg="#d9d9f2")
        txtToplam.pack(padx=20, pady=30)

        txtToplam2 = Label(girsayfasi,bg="#d9d9f2")
        txtToplam2.pack(padx=20, pady=30)


        im.execute("SELECT SUM(ucret) FROM ucretler")
        ucretler = im.fetchall()
        print(ucretler)
        txtToplam2.config(text=(ucretler,"TL"))

        b2 = Button(girsayfasi, text="Günü Sonlandır!",command=sonlandir, bg="#d9d9f2")
        b2.pack(padx=30, pady=30)

def sonlandir():
    result = messagebox.askyesno(title="Sonlandir", message="Son Günün Tüm Bilgileri Silincek, Devam Etmek İstiyor Musunuz?")
    if result == True:
        im.execute("DELETE FROM kiralayicilar")
        im.execute("DELETE FROM ucretler")
        vt.commit()


b2 = Button(root, text="Kıralayıcı", width=30,height=5, command=kiralayici,bg="#d9d9f2")
b2.pack(padx=20, pady=50)

b1 = Button(root, text="Yöneticin", width=30,height=5, command=yonetici,bg="#d9d9f2")
b1.pack(padx=20, pady=50)

mainloop()
