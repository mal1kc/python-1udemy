from proje1_kutuphane import *


def input_control(gir):
    try:
        int(gir)
    except ValueError:
        try:
            float(gir)
        except ValueError:
            return "str"
        else:
            return "float"
    else:
        return "int"


def evet_hayir(gir):
    if gir == 'e' or 'E':
        return True
    elif gir == 'h' or 'H':
        return False
    else:
        return True


print(""""***********************************
Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

Çıkmak için 'q' geri dönemek için '0' a basın.
***********************************""")



while True:
    girdi = input("yapmak istediğiniz işlem numarasını giriniz : ")
    if input_control(girdi) == "str":
        if girdi == 'q':
            print("iyi günler")
            kutuphane.baglanti_kes()
            time.sleep(1)
            break
        else:
            print("hatalı bir girdi girdiniz")
    else:
        if input_control(girdi) == "int":
            if girdi == '1':
                print("kütüphanede bulunan kitaplar")
                kutuphane.kitaplari_goster()
            elif girdi == '2':
                girdi = input("sorgulamak istedğiniz kitap adı (geri dönmek için '0') : ")
                if girdi == '0':
                    continue
                else:
                    print("Kitap Sorgulanıyor...")
                    time.sleep(2)
                    kutuphane.kitap_sorgula(girdi)
            elif girdi == '3':
                girdi = input("eklemek istedğiniz kitap adı,yazarı,yayınevi,tür,baskı sayısını arada virgülle giriniz "
                              "(geri dönmek için '0') : ")
                if girdi.find(',') == -1:
                    print("hatalı şekilde girdiniz sırayla giriniz \n")
                    isim = input("İsim:")
                    yazar = input("Yazar:")
                    yayinevi = input("Yayınevi:")
                    tur = input("Tür:")
                    baski = int(input("Baskı:"))
                    yeni_kitap = Kitap(kutuphane.sonid + 1, isim, yazar, yayinevi, tur, baski)
                    print("Kitap ekleniyor....")
                    time.sleep(2)
                    kutuphane.kitap_ekle(yeni_kitap)
                    print("Kitap Eklendi....")
                else:
                    kitap_ozellik = list(girdi.split(","))
                    isim = kitap_ozellik[0]
                    yazar = kitap_ozellik[1]
                    yayinevi = kitap_ozellik[2]
                    tur = kitap_ozellik[3]
                    baski = kitap_ozellik[4]
                    yeni_kitap = Kitap(kutuphane.sonid + 1, isim, yazar, yayinevi, tur, baski)
                    print("Kitap ekleniyor....")
                    time.sleep(2)
                    kutuphane.kitap_ekle(yeni_kitap)
                    print("Kitap Eklendi....")
            elif girdi == '4':
                girdi = input("silmek istediğiniz kitabin adı : ")

                gird2 = input("{} isimli kitabı silmek istediğinize emin misiniz (e/h) : ".format(girdi))

                if evet_hayir(gird2):
                    kutuphane.kitap_sil(girdi)
                else:
                    print("menuye donuluyor")
                    continue
            elif girdi == '5':
                girdi = input("baskı sayısını yükseltmek istediğiniz kitab ismi ? : ")
                if girdi == '0':
                    continue
                else:
                    kutuphane.baski_yukselt(girdi)
        else:
            print("hatalı bir girdi girdiniz")
