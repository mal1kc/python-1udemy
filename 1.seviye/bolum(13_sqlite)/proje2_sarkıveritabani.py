# Proje 2
# v1 = bagımsız tablolar şimdilik
# Siz de bir tane Şarkı projesi geliştirmeye çalışın.
#
#                      Örnek özellikler;
#
#                      1. Şarkı İsmi
#                      2. Sanatçı
#                      3. Albüm
#                      4. Prodüksiyon Şirketi----
#                      5. Şarkı Süresi
#
#                      Örnek Metodlar;
#
#                      1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
#                      2. Şarkı Ekle
#                      3. Şarkı Sil

import sqlite3


class Main:

    def __init__(self):
        self.baglanti = sqlite3.connect("müzikkütüphanesi.db")

        self.cursor = self.baglanti.cursor()

    def baglanti_kes(self):
        self.cursor.close()

    def veritabanindakiler(self, isim):
        sorgu = "SELECT * FROM {}".format(isim)

        self.cursor.execute(sorgu)

        return self.cursor.fetchall()

    def tablolari_yaz(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [
            v[0] for v in self.cursor.fetchall()
            if v[0] != "sqlite_sequence"
        ]
        self.baglanti.close()
        print(tables)

    def sanatciid(self):
        # girdi alırken fonksiyon kullanılmalı
        if len(self.veritabanindakiler("sanatçılar")) == 0:
            self.sanatcid = 1
            return self.sanatcid
        else:
            sorgu = "SELECT MAX(id) FROM sanatçılar"
            self.cursor.execute(sorgu)
            self.sanatcid = self.cursor.fetchall()[0][0]
            self.sanatcid += 1
            return self.sanatcid

    def sanatci_ekle(self, sanatci):
        sorgu = "INSERT INTO sanatçılar VALUES(?,?,?,?)"
        self.cursor.execute(sorgu, (sanatci.ids, sanatci.isim, sanatci.sarkilar, sanatci.albumler))
        self.baglanti.commit()

    def sanatcilari_listele(self):
        sanatcilar = self.veritabanindakiler("sanatçılar")
        if len(sanatcilar) == 0:
            print("Kütüphanede sanatcı")
        else:
            for i in sanatcilar:
                sanatci = Sanatci(i[0], i[1], i[2], i[3])
                print(sanatci)

    def sanatci_sorgula(self, isim):
        sorgu = "SELECT * FROM sanatçılar WHERE isim = ?"

        self.cursor.execute(sorgu, (isim,))

        sanatcilar = self.cursor.fetchall()
        if len(sanatcilar) == 0:
            print("böyle bir sanatçı kayıtlı değil")
        else:
            sanatci = Sanatci(sanatcilar[0][0], sanatcilar[0][1], sanatcilar[0][2], sanatcilar[0][3])
            print(sanatci)

    def sanatci_sil(self, isim):
        sorgu = "DELETE FROM sanatçılar WHERE isim = ?"

        self.cursor.execute(sorgu, (isim,))

        self.baglanti.commit()

    def sarkiid(self):
        # girdi alırken fonksiyon kullanılmalı
        if len(self.veritabanindakiler("şarkılar")) == 0:
            self.sarkid = 1
            return self.sarkid
        else:
            sorgu = "SELECT MAX(id) FROM şarkılar"
            self.cursor.execute(sorgu)
            self.sarkid = self.cursor.fetchall()[0][0]
            self.sarkid += 1
            return self.sarkid

    def sarki_ekle(self, sarki):
        sorgu = "INSERT INTO şarkılar VALUES(?,?,?,?,?,?,?)"
        self.cursor.execute(sorgu,
                            (sarki.ids, sarki.isim, sarki.album, sarki.tur, sarki.uzunluk, sarki.sanatci, sarki.sozler))
        self.baglanti.commit()

    def sarkilari_listele(self):
        sarkilar = self.veritabanindakiler("şarkılar")
        if len(sarkilar) == 0:
            print("Kütüphanede sarki")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                print(sarki)

    def sarki_sorgula(self, isim):
        sorgu = "SELECT * FROM şarkılar WHERE isim = ?"

        self.cursor.execute(sorgu, (isim,))

        sarkilar = self.cursor.fetchall()
        if len(sarkilar) == 0:
            print("böyle bir sanatçı kayıtlı değil")
        else:
            sarki = Sarki(sarkilar[0][0], sarkilar[0][1], sarkilar[0][2], sarkilar[0][3], sarkilar[0][4],
                          sarkilar[0][5], sarkilar[0][6])
            print(sarki)

    def sarki_sil(self, isim):
        sorgu = "DELETE FROM şarkılar WHERE isim = ?"

        self.cursor.execute(sorgu, (isim,))

        self.baglanti.commit()

    def albumiid(self):
        # girdi alırken fonksiyon kullanılmalı
        if len(self.veritabanindakiler("albümler")) == 0:
            self.albumid = 1
            return self.albumid
        else:
            sorgu = "SELECT MAX(id) FROM albümler"
            self.cursor.execute(sorgu)
            self.albumid = self.cursor.fetchall()[0][0]
            self.albumid += 1
            return self.albumid

    def album_ekle(self, album):

        sorgu = "INSERT INTO albümler VALUES(?,?,?,?,?,?)"
        self.cursor.execute(sorgu, (album.ids, album.isim, album.sanatci, album.tur, album.uzunluk, album.sarkilar))
        self.baglanti.commit()

    def albumleri_listele(self):
        albumler = self.veritabanindakiler("albümler")
        if len(albumler) == 0:
            print("Kütüphanede albümler")
        else:
            for i in albumler:
                album = Album(i[0], i[1], i[2], i[3], i[4], i[5])
                print(album)

    def album_sorgula(self, isim):
        sorgu = "SELECT * FROM albümler WHERE isim = ?"

        self.cursor.execute(sorgu, (isim,))

        albumler = self.cursor.fetchall()
        if len(albumler) == 0:
            print("böyle bir albüm kayıtlı değil")
        else:
            album = Album(albumler[0][0], albumler[0][1], albumler[0][2], albumler[0][3], albumler[0][4],
                          albumler[0][5])
            print(album)

    def album_sil(self, isim):
        sorgu = "DELETE FROM albümler WHERE isim = ?"

        self.cursor.execute(sorgu, (isim,))

        self.baglanti.commit()


class Sanatci:

    def __init__(self, ids, isim, sarkilar=None, albumler=None):
        if sarkilar is None:
            self.sarkilar = []
        else:
            self.sarkilar = sarkilar
        if albumler is None:
            self.albumler = []
        else:
            self.albumler = albumler
        self.ids = ids
        self.isim = isim
        self.main = Main()
        self.cursor = self.main.cursor
        self.baglanti = self.main.baglanti
        sorgu = "CREATE TABLE IF NOT EXISTS sanatçılar (id INT,isim TEXT,sarkilar TEXT,albumler TEXT)"

        self.cursor.execute(sorgu)
        self.baglanti.commit()

        sorgu = "SELECT MAX(id) FROM sanatçılar"
        self.cursor.execute(sorgu)
        self.sonid = self.cursor.fetchall()[0][0]

    def __str__(self):
        return "id : {},isim {},sarkilar : {}\n,albumler : {}".format(self.ids, self.isim, self.sarkilar, self.albumler)


class Sarki:

    def __init__(self, ids, isim, album, tur, uzunluk, sanatci, sozler=None):
        self.ids = ids
        self.isim = isim
        self.album = album
        self.uzunluk = uzunluk
        self.sanatci = sanatci
        self.tur = tur
        if sozler is None:
            self.sozler = ["None"]
        else:
            self.sozler = sozler
        self.main = Main()
        self.cursor = self.main.cursor
        self.baglanti = self.main.baglanti
        sorgu = "CREATE TABLE IF NOT EXISTS şarkılar (id INT,isim TEXT,album TEXT,tur TEXT,uzunluk TEXT,sanatci TEXT," \
                "sozler TEXT) "

        self.cursor.execute(sorgu)
        self.baglanti.commit()

        sorgu = "SELECT MAX(id) FROM şarkılar"
        self.cursor.execute(sorgu)
        self.sonid = self.cursor.fetchall()[0][0]

    def __str__(self):
        return "isim {},sanatçı = {},album : {},uzunluk : {},tur : {}\n,sozler {}".format(self.isim, self.sanatci,
                                                                                          self.album, self.uzunluk,
                                                                                          self.tur, self.sozler)


class Album:

    def __init__(self, ids, isim, sanatci, tur, uzunluk, sarkilar=None):
        self.ids = ids
        self.uzunluk = int(uzunluk)
        if sarkilar is None:
            self.sarkilar = []
        else:
            self.sarkilar = sarkilar
            for i in len(self.sarkilar):
                uzunluk += self.sarkilar[i].uzunluk
        self.uzunluk = uzunluk
        self.isim = isim
        self.sanatci = sanatci
        self.tur = tur
        self.main = Main()
        self.cursor = self.main.cursor
        self.baglanti = self.main.baglanti
        sorgu = "CREATE TABLE IF NOT EXISTS albümler (id INT,isim TEXT,sanatçı TEXT,tur TEXT,uzunluk INT,sarkilar TEXT)"

        self.cursor.execute(sorgu)
        self.baglanti.commit()

        sorgu = "SELECT MAX(id) FROM albümler"
        self.cursor.execute(sorgu)
        self.sonid = self.cursor.fetchall()[0][0]

    def __str__(self):
        return "id : {},isim {},sanatçı = {},sarkilar : {},uzunluk : {},tur : {}\n".format(self.ids, self.isim,
                                                                                           self.sanatci, self.sarkilar,
                                                                                           self.uzunluk, self.tur)
