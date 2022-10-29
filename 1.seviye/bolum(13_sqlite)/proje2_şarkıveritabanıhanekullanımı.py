from proje2_sarkıveritabani import *


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


def anamenu():
    print(""" neler ile işlem yapmak istersiniz

    1.Sanatçılar

    2.Şarkılar

    3.Albümler
    
    önceki menulere donmek icin '0'
    programı kapatmak için 'q'
    eklerken bos bırakmak istediğinize boş yazın
    """)


def sarkimenu():
    print("""Şarkılarla yapmak istediğiniz işlem nedir
    
    1.şarkı ekle 
    
    2.tüm şarkıları listele
    
    3.şarkı sözü yazdır
    
    4.şarkı sil
    
    5.şarkı sözü ekle
    
    """)


def albummenu():
    print("""Albümlerle yapmak istediğiniz işlem nedir

       1.Albüm ekle 

       2.tüm Albümleri listele

       3.Albüm özelliğini yazdır

       4.Albüm sil
       """)


def sanatcimenu():
    print("""sanatçılarla yapmak istediğiniz işlem nedir

       1.sanatçı ekle 

       2.tüm sanatçıları listele

       3.sanatçı özelliklerini yazdır

       4.sanatçı sil
       """)


main = Main()

while True:
    anamenu()
    girdi = input("yapmak istediğiniz işlem numarasını giriniz : ")
    if input_control(girdi) == "str":
        if girdi == 'q':
            print("iyi günler")
            main.baglanti_kes()
            break
        else:
            print("hatalı bir girdi girdiniz")
    else:
        if input_control(girdi) == "int":
            if girdi == '0':
                continue
            elif girdi == '1':
                sanatcimenu()
                girdi = input("yapmak istediğiniz işlem numarasını giriniz : ")
                if input_control(girdi) == "str":
                    if girdi == "q":
                        break
                    else:
                        print("hatalı bir girdi girdiniz")
                else:
                    if girdi == "0":
                        continue
                    elif girdi == "1":
                        print("eklemek istediğiniz sanatçı bilgileri nedir")
                        isim = input("Sanatçı isim : ")
                        sarkilar = input("Sanatçı sarkıları (',' ayırın) : ")
                        albumler = input("Sanatçı albümleri : ")
                        sanatci = Sanatci(main.sanatciid(), isim, sarkilar, albumler)
                        main.sanatci_ekle(sanatci)
                    elif girdi == "2":
                        print("veritabanındaki listeler")
                        main.sanatcilari_listele()
                    elif girdi == "3":
                        gird1 = input("özelliklerini istediğiniz sanatçının adı : ")
                        main.sanatci_sorgula(gird1)
                    elif girdi == "4":
                        gird1 = input("silmek istedigibiz sanatçı adı nedir : ")
                        gird2 = input(" {} isimli sanatçıyı/ları silmek istediğinize emin misiniz e/h : ".format(gird1))
                        if evet_hayir(gird2):
                            main.sanatci_sil(gird1)
                            print("{} isimli başarıyla silindi".format(gird1))
                        else:
                            continue
                    else:
                        print("hatalı bir girdi girdiniz")
            elif girdi == '2':
                sarkimenu()
                girdi = input("yapmak istediğiniz işlem numarasını giriniz : ")
                if input_control(girdi) == "str":
                    if girdi == "q":
                        break
                    else:
                        print("hatalı bir girdi girdiniz")
                else:
                    if girdi == "0":
                        continue
                    elif girdi == "1":
                        print("eklemek istediğiniz şarkı bilgileri nedir")
                        isim = input("şarkının ismi : ")
                        album = input("şarkının bulunduğu album : ")
                        tur = input("Şarkının türü nedir : ")
                        sanatci = input("Şarkının sanatçısı : ")
                        sozler = input("Şarkının sözleri : ")
                        uzunluk = input("Şarkının uzunluğu : ")
                        sarki = Sarki(main.sarkiid(), isim, album, tur, uzunluk, sanatci, sozler)
                        main.sarki_ekle(sarki)
                    elif girdi == "2":
                        print("veritabanındaki listeler")
                        main.sarkilari_listele()
                    elif girdi == "3":
                        gird1 = input("özelliklerini istediğiniz şarkının adı : ")
                        main.sarki_sorgula(gird1)
                    elif girdi == "4":
                        gird1 = input("silmek istedigibiz şarkı adı nedir : ")
                        gird2 = input(" {} isimli şarkıyı silmek istediğinize emin misiniz e/h : ".format(gird1))
                        if evet_hayir(gird2):
                            main.sarki_sil(gird1)
                            print("{} isimli başarıyla silindi".format(gird1))
                        else:
                            continue
                    else:
                        print("hatalı bir girdi girdiniz")
            elif girdi == "3":
                albummenu()
                girdi = input("yapmak istediğiniz işlem numarasını giriniz : ")
                if input_control(girdi) == "str":
                    if girdi == "q":
                        break
                    else:
                        print("hatalı bir girdi girdiniz")
                else:
                    if girdi == "0":
                        continue
                    elif girdi == "1":
                        print("eklemek istediğiniz albüm bilgileri nedir")
                        isim = input("albümün ismi : ")
                        tur = input("Albümün türü nedir : ")
                        sanatci = input("Albümün sanatçısı : ")
                        sarkilar = input("Albümün şarkıları : ")
                        album = Album(main.albumiid(), isim, sanatci, tur, 0, sarkilar)
                        main.album_ekle(album)
                    elif girdi == "2":
                        print("veritabanındaki albümler")
                        main.albumleri_listele()
                    elif girdi == "3":
                        gird1 = input("özelliklerini istediğiniz albümnün adı : ")
                        main.album_sorgula(gird1)
                    elif girdi == "4":
                        gird1 = input("silmek istedigibiz albüm adı nedir : ")
                        gird2 = input(" {} isimli albümü silmek istediğinize emin misiniz e/h : ".format(gird1))
                        if evet_hayir(gird2):
                            main.album_sil(gird1)
                            print("{} isimli başarıyla silindi".format(gird1))
                        else:
                            continue
                    else:
                        print("hatalı bir girdi girdiniz")
        else:
            print("hatalı bir girdi girdiniz")
