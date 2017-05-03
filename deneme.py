#-*- coding:utf-8 -*-
#Veritabanı Modülü import etme
import sqlite3
import tkinter
from tkinter import *


#Veritabanı Oluşturma ve Veritabanına Bağlanma
vt = sqlite3.connect('veritabani.accdb')
# Veritabanı işlemlerini hızlı yapmak için imleç oluşturuyoruz.
im =vt.cursor()

#Tablo oluşturma fonksiyonu
def olustur():
    im.execute("CREATE TABLE IF NOT EXISTS kullanicilar(ad,soyad,numara,vize,final,gecmenot)")
    im.execute("CREATE TABLE IF NOT EXISTS musteriler(ad,soyad,numara)")
# Tabloya Kayıt Ekleme
def ekle():
    ad= raw_input("adiniz")
    soyad= raw_input("Soyadınız :")
    numara= raw_input("Numara :")
    vize=float(raw_input("vize :"))
    final= float(raw_input("Final :"))
    gecmenot =(vize *0.3)+(final*0.7)
    im.execute("INSERT INTO kullanicilar (ad,soyad,numara,vize,final,gecmenot) VALUES(?,?,?,?,?,?)",
               (ad,soyad,numara,vize,final,gecmenot))
    vt.commit()

def musterilereEkleme():
    ad= raw_input("adiniz")
    soyad= raw_input("Soyadınız :")
    numara= raw_input("Numara :")

    im.execute("INSERT INTO musteriler (ad,soyad,numara) VALUES(?,?,?)",
               (ad,soyad,numara))
    vt.commit()


def listele():
    a=141
    im.execute("SELECT * FROM kullanicilar WHERE numara=?",a) #burada bı hata vardı...
    veriler= im.fetchall()
    print ("Veriler:")
    print (veriler)

def musterilerigoster():
    im.execute("SELECT * FROM musteriler")
    veriler= im.fetchall()
    print ("Veriler:")
    print (veriler)

def ara():
    aranannumara=input("Aramak istediğiniz numara:  ")
    im.execute("SELECT * FROM kullanicilar WHERE numara=?",aranannumara)
    veriler= im.fetchall()
    print ("Veriler:")
    print (veriler)

def ekstralistele():

    im.execute("SELECT * FROM kullanicilar ORDER BY ad DESC")
    veriler= im.fetchall()
    print (veriler)

def sil():
    silin = input("Silinecek Numarayı gir : ")
    im.execute("DELETE FROM kullanicilar where numara=(?)",[silin])
    vt.commit()


def guncelle():
    simdiki=input("Guncellenecek no :")
    sonraki=input("Ne olsun :")
    im.execute("UPDATE kullanicilar SET numara=? WHERE numara=?",(sonraki,simdiki))
    vt.commit()

olustur()


listele()
    # musterilereEkleme()

    # print("musteriler listesi : ")
    # musterilerigoster()

    # print ("--İslem Secin--")
    # print ("1-Ekle\n2-Sil\n3-Guncelle\n4-Listele\n5-Ara\n6-EkstraListele\n0-Çıkış")
    # islem = input("Seçiminiz : ")
    # if(islem==1):
    #     ekle()
    # elif(islem==2):
    #     sil()
    # elif(islem==3):
    #     guncelle()
    # elif(islem==4):
    #     listele()
    # elif(islem==5):
    #     ara()
    # elif(islem==5):
    #      ekstralistele()

