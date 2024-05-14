# bölüm 5 versiyonu#
print("""
-------------------------------
Atm Makinesi v1
-------------------------------

İşlem numaraları;

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için 'q' tuşuna basınız.

-------------------------------
""")

bakiye = 10000
tur = 0
miktar = 0

while True:
    if tur == 0:
        islem = input("Yapmak istediğiniz işlemin numarasını giriniz : ")
    else:
        islem = input("Yapmak istediğiniz işlemin numarasını giriniz (çıkmak için 'q' tuşuna basınız) : ")
    if islem == "q":
        print("iyi günler dileriz ...")
        break
    elif islem == "1":
        print("Hesabınızda {} miktarında para bulunuyor ...".format(bakiye))
        tur += 1
    elif islem == "2":
        tur += 1
        miktar = int(input("Hesabınıza yatırmak istediğiniz miktarı giriniz : "))
        bakiye += miktar
        print("Hesabınıza {} para yatırdınız,Hesabınızdaki toplam bakiye {} oldu. ".format(miktar, bakiye))
    elif islem == "3":
        tur += 1
        miktar = int(input("Hesabınızdan çekmek istediğiniz miktarı giriniz : "))
        if (bakiye - miktar) < 0:
            print("Hesabınızda bulunandan fazlasını çekemezsiniz ... ")
            continue
        bakiye -= miktar
        print("Hesabınıza {} para çektiniz,Hesabınızdaki toplam bakiye {} oldu. ".format(miktar, bakiye))
    else:
        tur += 1
        print("Hatalı işlem kodu lütfen tekrar deneyiniz ...")
