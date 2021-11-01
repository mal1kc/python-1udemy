import sqlite3

con = sqlite3.connect("deneme.db")

cursor = con.cursor()


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_sayisi INT)")
    con.commit()


def veri_ekle2(isim, yazar, yayinevi, sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)", (isim, yazar, yayinevi, sayfa_sayisi))
    con.commit()


def verileri_al():
    print('\n')
    cursor.execute("SELECT * From kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik tablosundaki veriler ..")
    for i in liste:
        print(i)


def verileri_al2():
    cursor.execute("SELECT Isim,Yazar From kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik tablosundaki kitaplar ve yazarları ..")
    for i in liste:
        print(i)


def verileri_al3(yayinevi):
    cursor.execute("SELECT * FROM kitaplik WHERE Yayinevi = ?", (yayinevi,))
    liste = cursor.fetchall()
    print("Kitaplik tablosundaki {} adli yayin evinin kitapları ..".format(yayinevi))
    for i in liste:
        print(i)


def veririleri_guncelle(eski_yayinevi, yeni_yayinevi):
    cursor.execute("UPDATE kitaplik SET Yayinevi = ? WHERE Yayinevi = ?", (yeni_yayinevi, eski_yayinevi,))
    con.commit()


def verileri_sil(yazar):
    cursor.execute("DELETE FROM kitaplik WHERE Yazar = ?", (yazar,))


# isim = input("İsim: ")
# yazar = input("Yazar: ")
# yayinevi = input("Yayinevi: ")
# sayfa_sayisi= int(input("Sayfa Sayisi : "))
# veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi)


verileri_al3("Metis Edebiyat")
veririleri_guncelle('Metis Edebiyat', 'Metis Yayınları')

verileri_sil("Ahmet Ümit")
verileri_al()

con.close()
