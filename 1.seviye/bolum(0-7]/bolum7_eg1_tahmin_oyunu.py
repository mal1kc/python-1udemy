'''
tahmin oyunu
'''
import random
import time

print("""-------------------------------------------------
 Rastgele oluşturulan sayıları tahmin etme oyunu 
-------------------------------------------------""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7
while True:
    tahmin = int(input("bir sayı giriniz : "))

    if tahmin > rastgele_sayi:
        print("kontrol ediliyor")

        time.sleep(1)

        print("tahmin edemediniz {} tahmin hakkınız kaldı".format(tahmin_hakki))
        print("daha küçük bir sayı söyleyiniz")
        print("")

        tahmin_hakki -= 1
    elif tahmin < rastgele_sayi:
        print("kontrol ediliyor")

        time.sleep(1)

        print("tahmin edemediniz {} tahmin hakkınız kaldı".format(tahmin_hakki))
        print("daha büyük bir sayı söyleyiniz")
        print("")

        tahmin_hakki -= 1
    else:
        print("tebrikler {} denemede buldunuz".format(abs(tahmin_hakki - 7) + 1))
        print("program sonlandırılıyor ..")
        break
