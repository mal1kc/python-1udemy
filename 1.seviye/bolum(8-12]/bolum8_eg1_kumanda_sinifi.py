import random
import time

'''
derstekine göre değiştirilmiş geliştirilmiş kumanda sınıfı
'''

class Kumanda:

    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanallistesi=None, tv_kanal="trt"):

        if kanallistesi is None:
            kanallistesi = ["trt"]
            self.kanallistesi = kanallistesi
        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanallistesi = kanallistesi

        self.tv_kanal = tv_kanal

    def tv_ac(self):
        if self.tv_durum == "açık":
            print("televizyon zaten açık ")
        else:
            print("televizyon açılıyor")
            self.tv_durum = "açık"

    def tv_kapat(self):
        if self.tv_durum == "kapalı":
            print("televizyon zaten kapalı ")
        else:
            print("televizyon kapatılıyor")
            self.tv_durum = "kapalı"

    def tv_guc_kontrol(self):
        if self.tv_durum == "açık":
            return 1
        else:
            print("tv açık olmadığundan herangi bir işlem yapılmıyor")
            return 2

    def tv_ses_duzeyi(self):

        def tv_ses_artir():
            if self.tv_ses <= 100:
                self.tv_ses += 1
                print("ses : ", self.tv_ses)
            else:
                print("televizyon sesi en yüksekte - ses :100 -")

        def tv_ses_azalt():
            if self.tv_ses > 0:
                self.tv_ses -= 1
                print("ses : ", self.tv_ses)
            else:
                print("televizyon sesi en düşükte - ses : 0 -")

        def tv_ses_sustur():
            eski_ses = self.tv_ses
            if self.tv_ses == 0:
                self.tv_ses = eski_ses
                print("ses susturulması kapatıldı.")
            else:
                self.tv_ses = 0
                print("ses susturuldu")

        while True:
            cevap = input(
                "\nSesi Azalt : '<' \nSesi Artır : '>' \nSesi sustur aç/kapa : 's'\n "
                "Çıkış : herhangi bir tuş ('<','>','s' hariç)  : ")
            print("\n")
            if (cevap == '>'):
                tv_ses_artir()

            elif (cevap == '<'):
                tv_ses_azalt()

            elif (cevap == 's'):
                tv_ses_sustur()

            else:
                print("\nses güncellendi . Ses : ", self.tv_ses)
                print("\n")
                break

    def tv_kanal_ekle(self, kanal_ismi):

        print("{} isimli kanal ekleniyor".format(kanal_ismi))
        self.kanallistesi.append(kanal_ismi)
        time.sleep(1)

    def tv_kanal_degistir(self, a):

        def kanal_degistir(self, x):
            if (len(self.kanallistesi) >= x + 1):
                eski_kanal = self.tv_kanal
                self.tv_kanal = self.kanallistesi[x - 1]
                print("kanal değitirildi.\n {} --> {} ".format(eski_kanal, self.tv_kanal))
            else:
                print("bu kanal numarasında kanal bulunmuyor .( kanal listesinde o kadar kanal bulunmuyor .)")

        if a == 'r':
            rastgele = random.randint(0, (len(self.kanallistesi) - 1))
            kanal_degistir(self, rastgele)
            pass
        else:
            a = int(a)
            a = abs(a)
            kanal_degistir(self, a)

        a = str(a)

    def __len__(self):
        return len(self.kanallistesi)

    def __str__(self):
        return " Tv durumu :{} \n Tv ses : {}\n Tv de açık olan kanal : {} \n Tv de bulunan kanallar listesi : {}".format(
            self.tv_durum, self.tv_ses, self.tv_kanal, self.kanallistesi)

#def yenikumanda(a):
#   exec(a = Kumanda())


def menu():
    print("""
    Televizyon uygulaması

    0. Kumanda Değiştir(şimdilik çalışma altında otomatik 1. kullanılır )

    1. Tv Aç

    2. Tv Kapat

    3. Ses Ayarları

    4. Kanal Ekle

    5. Tv de  Bulunan Kanal Sayısını Öğrenme

    6. Kanal Değiştirme

    7. Tv Bilgileri öğrenme

    uygulamayı kapatmak için 'q' ya basınız
    """)


menu()

kumanda1 = Kumanda()

while True:

    girdi1 = input("yapmak istediğiniz işlem tuşuna basınız (menu : '8') : ")

    if (girdi1 == 'q'):

        print(" 1 saniye sonra çıkılcak ")
        time.sleep(1)
        break

    elif (girdi1 == '0'):
        print(" şimdilik çalışma altında - otomatik 1. kullanılıyor. ")

        '''
        girdi2 = input("kullanmak istediğiniz kumanda numarası yada  oluşturmak isterseniz : '0' ")

        if girdi2 == '0':
            girdi3 = input("istediğiniz ismi girin:")

            exec (girdi3 = Kumanda())

        else:

             print("kumanda 1  seçidi")

        '''

    elif (girdi1 == '1'):
        kumanda1.tv_ac()

    elif (girdi1 == '2'):
        kumanda1.tv_kapat()

    elif (girdi1 == '3'):
        if kumanda1.tv_guc_kontrol() == 1:
            kumanda1.tv_ses_duzeyi()

    elif (girdi1 == '4'):
        if kumanda1.tv_guc_kontrol() == 1:
            kanal_isimleri = input("eklenicek kanal isimlerini ',' ile ayırarak girin : ")
            kanal_listesi = kanal_isimleri.split(",")

            for eklenecek_kanlalar in kanal_listesi:
                kumanda1.tv_kanal_ekle(eklenecek_kanlalar)

    elif (girdi1 == '5'):
        if kumanda1.tv_guc_kontrol() == 1:
            print("Tv deki kanal listesinde {} adet kanal var".format(len(kumanda1)))

    elif (girdi1 == '6'):
        if kumanda1.tv_guc_kontrol() == 1:
            kumanda1.tv_kanal_degistir(input("değiştirmek istediğini kanalnumarası (rastgele : r)) : "))

    elif (girdi1 == '7'):
        print(print(kumanda1))

    elif (girdi1 == '8'):
        menu()

    else:
        print("hatalı değer ")
