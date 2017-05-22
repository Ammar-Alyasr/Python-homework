import tkinter
from tkinter import *
from tkinter import messagebox
import time, locale
import sqlite3

from tkinter.ttk import Panedwindow


vt = sqlite3.connect("dukkan.db")
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS kiralayicilar(adSoyad,Tc,saat)")
im.execute("CREATE TABLE IF NOT EXISTS yoneticiler(yoneticiAd, yoneticiSifre)")
im.execute("INSERT INTO yoneticiler (yoneticiAd,yoneticiSifre) VALUES(?,?)",
           ("root","toor"))
vt.commit()


root = Tk()
root.configure(background="grey")
root.minsize(500, 400)
root.maxsize(500, 400)
root.title("Biseklet Kiralama ...")

def kiralayici():
    kiralayiciSayfasi = Tk()
    kiralayiciSayfasi.configure(background="grey")
    kiralayiciSayfasi.minsize(400, 300)
    kiralayiciSayfasi.maxsize(400, 300)
    kiralayiciSayfasi.title('Hos geldin... ')

    global txtisim, txttc
    lblisim = Label(kiralayiciSayfasi, text=" AD SOYAD ",bg="tan")
    lblisim.grid(row=3, column=3)

    txtisim = Entry(kiralayiciSayfasi)
    txtisim.grid(row=3, column=5)

    lbltc = Label(kiralayiciSayfasi, text="TC",bg="tan")
    lbltc.grid(row=5, column=3)

    txttc = Entry(kiralayiciSayfasi)
    txttc.grid(row=5, column=5)

    b2 = Button(kiralayiciSayfasi, text=" AL ", width=15, command=al,bg="tan")
    b2.grid(row=7,column=2)
    b3 = Button(kiralayiciSayfasi, text=" Iade Et ", width=15, command=iade,bg="tan")
    b3.grid(row=7,column=3)



def al():

    if(txttc.get()!= ""):
        im.execute("INSERT INTO kiralayicilar (adsoyad,Tc,saat) VALUES(?,?,?)",
                (txtisim.get(), txttc.get(), time.strftime("%H:%M:%S")))
        vt.commit()
        im.execute("SELECT * FROM kiralayicilar")
        veriler = im.fetchall()
        print(veriler)


        kiralayiciSayfasi4= Tk()
        kiralayiciSayfasi4.configure(background='grey')
        lblal1 = Label(kiralayiciSayfasi4, text="Başarılı bir şekilde kırallandı,bisiklet kulanabilirsiniz...",font="elephant",bg="tan")
        lblal1.pack(padx=7, pady=3, side=TOP)
        lblal = Label(kiralayiciSayfasi4, text="isim",bg="tan").pack(padx=10, pady=5, side=TOP)
        lblal= Label(kiralayiciSayfasi4, text=txtisim.get()).pack(padx=10, pady=5, side=TOP)
        lblal = Label(kiralayiciSayfasi4, text=" Saat ",bg="tan").pack(padx=10, pady=5, side=TOP)
        lblal = Label(kiralayiciSayfasi4, text=time.strftime("%H:%M:%S")).pack(padx=10, pady=5, side=TOP)
        print(txtisim)
        b5 = Button(kiralayiciSayfasi4, text=" Tamam ", command=quit, width=10,bg="tan")
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

        sonsonuc = toplam_saat * 4.0  # bir saatlik ucreti 4 TL dir
        # sonsonuc=float(sonsonuc)
        sonsonuc = round(sonsonuc, 2)
        print(sonsonuc)



        kiralayiciSayfasi3 = Tk()
        kiralayiciSayfasi3.configure(background="grey")
        lbliade = Label(kiralayiciSayfasi3, text=" isim ",bg="tan").pack(padx=10, pady=5, side=TOP)
        lbliade = Label(kiralayiciSayfasi3, text=veriler[0][0]).pack(padx=10, pady=5, side=TOP)

        lbliade = Label(kiralayiciSayfasi3, text=" Başlangic Saat ",bg="tan").pack(padx=10, pady=5, side=TOP)
        lbliade = Label(kiralayiciSayfasi3, text=veriler[0][2]).pack(padx=10, pady=5, side=TOP)

        lbliade = Label(kiralayiciSayfasi3, text=" Bitiş Saat ",bg="tan").pack(padx=10, pady=5, side=TOP)
        lbliade = Label(kiralayiciSayfasi3, text=time.strftime("%H:%M:%S")).pack(padx=10, pady=5, side=TOP)

        lbliade = Label(kiralayiciSayfasi3, text=" Ücret ", bg="tan").pack(padx=10, pady=5, side=TOP)
        lbliade = Label(kiralayiciSayfasi3, text=sonsonuc).pack(padx=10, pady=5, side=TOP)

        b5 = Button(kiralayiciSayfasi3, text=" Vazgeç ",command=message1 ,width=15,bg="tan")
        b5.pack(padx=20, pady=50, side=LEFT)
        b6 = Button(kiralayiciSayfasi3, text=" Iade Et ",command=message2, width=15,bg="tan")
        b6.pack(padx=20, pady=50, side=RIGHT)

        im.execute("DELETE FROM kiralayicilar where Tc=(?)", [txttc.get()])
        vt.commit()

    else:
        messagebox.showerror("Hata","Boşluk Bırakılamaz !!")

def message1():
    messagebox.askyesno(title="Vazgeç", message="Sayfadan çikmak istiyor musunuz?...")
def message2():
    messagebox.askyesno(title="Iade Et", message="Sayfadan çikmak istiyor musunuz?...")

def yonetici():

    #
    # print("Trying to login...")

    # if user == username:
    #     messagebox.showinfo("-- COMPLETE --", "Girdiğiniz Kullancı ismi doğrudur...", icon="info")
    # elif user!=username:
    #     messagebox.showinfo("-- ERROR --", "Lütfen, Giridiğiniz kullancı isim yanliştir!...", icon="warning")
    # elif pas== password:
    #     messagebox.showinfo("-- COMPLETE --", "Girdiğiniz Şefre doğrudur...", icon="info")
    # else:
    #     messagebox.showinfo("-- ERROR --", "Lütfen, Giridiğiniz Şefre yanliştir!...", icon="warning")

    yoneticiSayfasi = Tk()
    yoneticiSayfasi.configure(background="grey")
    yoneticiSayfasi.minsize(300, 300)
    yoneticiSayfasi.maxsize(300, 300)
    yoneticiSayfasi.title('Hos geldin (Yönetici)... ')

    global username_guess,password_guess
    username_text = Label(yoneticiSayfasi, text="Kullanci ismi: ", bg="tan")
    username_text.grid(row=0, column=5)

    username_guess = Entry(yoneticiSayfasi)
    username_guess.grid(row=2, column=5)



    password_text = Label(yoneticiSayfasi, text="Şifre:", bg="tan")
    password_text.grid(row=5, column=5)

    password_guess = Entry(yoneticiSayfasi)
    password_guess.grid(row=7, column=5)
    b=Button(yoneticiSayfasi, text=" GİR ", width=15, bg="tan",command=gir)
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
        girsayfasi.configure(background="grey")
        byon = Button(girsayfasi, text=" kiralayaci ", width=30, height=3, bg="tan")
        byon.pack(padx=20, pady=30)
        byon1 = Button(girsayfasi, text=" Bisikletler ", width=30, height=3, bg="tan")
        byon1.pack(padx=20, pady=30)
        byon2 = Button(girsayfasi, text=" Hisaplar ", width=30, height=3, bg="tan")
        byon2.pack(padx=20, pady=30)



b2 = Button(root, text="Kıralayıcı", width=30,height=5, command=kiralayici,bg="tan")
b2.pack(padx=20, pady=50)

b1 = Button(root, text="Yöneticin", width=30,height=5, command=yonetici,bg="tan")
b1.pack(padx=20, pady=50)

mainloop()
