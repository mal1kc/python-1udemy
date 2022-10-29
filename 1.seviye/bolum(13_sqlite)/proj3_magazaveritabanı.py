# Proje 3
#
# Süpermarket içindeki ürünler üzerinden bir tane Süpermarket Projesi geliştirmeye çalışın.
import sqlite3


class Market:
    def __init__(self):
        self.baglanti = sqlite3.connect("supermatket.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS müşteriler (id INT,isim TEXT,para TEXT)")
        self.baglanti.commit()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ürünler (id INT,isim TEXT,birim-fiyat TEXT,tür TEXT,"
                            "miktar TEXT,satıcı TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS satıcılar (id INT,isim TEXT,sattığı_ürünler TEXT")

    def tablo_getir(self, isim):
        sorgu = "SELECT * FROM {}".format(isim)

        self.cursor.execute(sorgu)

        return self.cursor.fetchall()

    def musteriid(self):
        if len(self.tablo_getir("müşteriler")) == 0:
            self.musterid = 1
            return self.musterid
        else:
            sorgu = "SELECT MAX(id) FROM müşteriler"
            self.cursor.execute(sorgu)
            self.musterid = self.cursor.fetchall()[0][0]
            self.musterid += 1
            return self.musterid

    def musteri_ekle(self, musteri):
        sorgu = "INSERT INTO müşteriler VALUES(?,?,?)"
        self.cursor.execute(sorgu, (self.musteriid(), musteri.isim, musteri.para))
        self.baglanti.commit()

    def uruniid(self):
        if len(self.tablo_getir("ürünler")) == 0:
            self.urunid = 1
            return self.urunid
        else:
            sorgu = "SELECT MAX(id) FROM ürünler"
            self.cursor.execute(sorgu)
            self.urunid = self.cursor.fetchall()[0][0]
            self.urunid += 1
            return self.urunid

    def urun_ekle(self, urun):
        sorgu = "INSERT INTO ürünler VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu, (self.uruniid(), urun.isim, urun.fiyat, urun.tür, urun.miktar, urun.satıcı))
        # satıcı urun bagıntısı kurulcak
        self.baglanti.commit()

    def saticiid(self):
        if len(self.tablo_getir("satıcılar")) == 0:
            self.saticid = 1
            return self.saticid
        else:
            sorgu = "SELECT MAX(id) FROM satıcılar"
            self.cursor.execute(sorgu)
            self.saticid = self.cursor.fetchall()[0][0]
            self.saticid += 1
            return self.saticid

    def satici_ekle(self, satici):
        sorgu = "INSERT INTO satıcılar"
        self.cursor.execute(sorgu, (self.saticiid(), satici.isim,satici.urunler))
        # satıcı urun bagıntısı kurulcak
        self.baglanti.commit()

    # def satıcı_bagıntısı(self, tablo1, sutun, oge, tablo2, ):
    #
    #     # 'tablo1' tablosunun 'sutun' isimli sütününda ogeyi arar varsa 'tablo2' 'sutun2' isimli sutunundaki ile eşler
    #     #
    #     sorgu = "SELECT {} FROM {}".format(sutun, tablo1)
    #     self.cursor.execute(sorgu)
    #     sutundakiler = self.cursor.fetchall()
    #     for i in range(len(sutundakiler)):
    #         if sutundakiler[i] == oge:
    #             sorgu1 = "SELECT * FROM {} WHERE id = ?".format(tablo1)
    #             self.cursor.execute(sorgu1,i)
    #             duzenlenecek = self.cursor.fetchall()
    #             duzenlendi = duzenlenecek[0][] +
    #
    #         else:
    #             # yeni satıcı ekle
