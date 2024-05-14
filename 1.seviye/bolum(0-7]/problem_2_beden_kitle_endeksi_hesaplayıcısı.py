v = int(input("versiyon seçiniz "))

kilo = float(input("kilonuzu giriniz (kg) = "))

boy = float(input("boyunuzu giriniz(m) = "))

if v == 1:
    print("0 - 18,4: Zayıf \n18,5 - 24,9: Normal \n25,0 - 29,9: Fazla Kilolu \n30,0 ve üstü :Obez(şişman)")
    print("İşlem sonucu: {}".format(kilo / boy * boy))
elif v == 2:
    sonuc = kilo / (boy * boy)
    if sonuc > 0.0 and 18.4 >= sonuc:
        print("İşlem sonucu : Boyunuza göre ZAYIFsınız ,Hesaplanan beden kitle indeksi {} ".format(sonuc))
    elif sonuc > 18.4 and 25.0 > sonuc:
        print("İşlem sonucu : Boyunuza göre NORMAL kilodasınız  ,Hesaplanan beden kitle indeksi {} ".format(sonuc))
    elif sonuc >= 25.0 and 30 > sonuc:
        print("İşlem sonucu : Boyunuza göre FAZLA kilolusunuz  ,Hesaplanan beden kitle indeksi {} ".format(sonuc))
    else:
        print("İşlem sonucu : Boyunuza göre OBEZ(ŞİŞMAN)sınız ,Hesaplanan beden kitle indeksi {} ".format(sonuc))
else:
    print("böyle bir versiyon bulunmamaktadır")
