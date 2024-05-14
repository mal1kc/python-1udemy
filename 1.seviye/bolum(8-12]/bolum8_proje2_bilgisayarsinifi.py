#
# 8.bolum proje 2
#
#  Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.
#
# Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
#
#
# oyun aç {---}
#
# rastgele oyun seç {---}
#
# hesap makinesini çalıştır {---}
#
# python scriptlerini aç {---}
#
# saat{-}
#
# temel---
# aç kapa++++++++++++++++++
#
# print ile bilgisyar özellikleri+++++++
#
# random modulu ile tahmini fps test-iptaliptaliptaliptal
#
# sesi ayarları +- susturma++++++++++++++++
#
# açık programlar+++++++++
#
# program aç+++++++
#
# program yükle +++++++++++
#
# program sil+++++++++++++++++++
#
# rastgele şifre oluştur{-}
#
# fotoğrafları göster {---}
#
# ram kullanımı  {---}
#
# cpu kullanımı {---}
#
# gpu kullanımı {---}
#
# * = opsiyonal
# ---temel
# yapımı uzun sürdüğünden ve hayali kalması için silinenler {---}
#
# üşendiklerim {-}
#

def evet_hayir(girdi):
    if girdi == 'e' or 'E':
        return True
    elif girdi == 'h' or 'H':
        return False
    else:
        return True


def get_key(va, dic):
    for k, v in dic.items():
        if v == va:
            return k


def input_control(a):
    try:
        temp = int(a)
    except ValueError:
        try:
            temp = float(a)
        except ValueError:
            return "str"
        else:
            return "float"
    else:
        return "int"


class Program:
    def __init__(self, program_durum="kapalı", program_cpu_yuk=1, pid=None, program_ram_yuk="1mb"):
        self.program_durum = program_durum
        self.program_cpu_yuk = program_cpu_yuk
        self.pid = pid
        self.program_ram_yuk = program_ram_yuk


class Bilgisayar:
    i = 2

    def __init__(self, pc_adi, pc_gucdrurumu="açık", ses=0, programlistesi=None, acik_programlar=None,
                 yuklenebilir_proglar=None):

        self.pc_adi = pc_adi
        if programlistesi is None:
            programlistesi = ["firefox", "steam", "windows explorer"]
            self.programlistesi = programlistesi
        self.ses = ses
        if acik_programlar is None:
            acik_programlar = {2: "windows explorer", 3: "steam"}
            self.acik_programlar = acik_programlar
        self.pc_gucdurumu = pc_gucdrurumu
        if yuklenebilir_proglar is None:
            yuklenebilir_proglar = ["opera", "mails", "ubisofconnect", "battle.net", "jdownloader", "bittorrent",
                                    "origin"
                , "7zip", "pycharm", "discord", "gtaV", "satisfactory", "minecraft", "darkest-dungeon"]
            self.yuklenebilir_proglar = yuklenebilir_proglar

    def __str__(self):
        return """
            güç durumu {}
            ses düzeyi {}
            
            açık programlar {}
            
            yuklu programlar {}
            
        """.format(self.pc_gucdurumu, self.ses, self.acik_programlar, self.programlistesi)

    def pc_guc_kontrol(self):

        if self.pc_gucdurumu == "açık":
            gird1 = input("\n pc zaten açık açık kapatmak istermisiniz ? (e/h varsayılan : h ) : ")
            if evet_hayir(gird1):
                print("pc kapatılıyor ..")
                self.pc_gucdurumu == "kapalı"
        else:
            gird1 = input("\n pc kapalı açmak istermisiniz ? (e/h varsayılan : h ) : ")
            if evet_hayir(gird1):
                self.pc_gucdurumu == "açık"

    def pc_ses(self):

        def pc_ses_artir(d=1):
            if self.ses < 100:
                self.ses += d
                if 100 >= self.ses:
                    print("ses : ", self.ses)
                else:
                    self.ses = 100
                    print("maksimum değerden fazla bir değer girdiğinizden ses : {}".format(self.ses))
            else:
                print("televizyon sesi en yüksekte - ses :100 -")

        def pc_ses_azalt(d=1):
            if self.ses > 0:
                self.ses -= d
                if 0 <= self.ses:
                    print("ses : ", self.ses)
                else:
                    self.ses = 100
                    print("minumum değerden az bir değer girdiğinizden ses : {}".format(self.ses))
            else:
                print("televizyon sesi en düşükte - ses : 0 -")

        def pc_ses_sustur(eski_ses=None):
            self.eski_ses = self.ses
            if self.ses == 0:
                self.ses = eski_ses
                print("ses susturulması kapatıldı.")
            else:
                self.ses = 0
                print("ses susturuldu")

        while True:
            girdi = input("\n ses arttırmak için '+',azaltmak için '-',susturmak için 'm' (geri dönmek için '0') : ")
            if girdi == '0':
                break
            elif girdi == '+':
                while True:
                    girdii = input(" artış mıktarı : ")
                    if input_control(girdii) == "int":
                        girdii = int(girdii)
                        if girdii == 0:
                            break
                        else:
                            pc_ses_artir(girdii)
                    else:
                        print("hatalı bir veri girdiniz")
            elif girdi == '-':
                while True:
                    girdii = input(" azalma mıktarı : ")
                    if input_control(girdii) == "int":
                        girdii = int(girdii)
                        if girdii == 0:
                            break
                        else:
                            pc_ses_azalt(girdii)
                    else:
                        print("hatalı bir veri girdiniz")
            elif girdi == 'm':
                pc_ses_sustur()
            else:
                print("hatalı bir veri girdiniz")

    #####programlar------------------------------------------------------

    def program_ac(self):
        gird1 = input("\n açmak istediğiz programın adını veya yüklü uygulamaları görmek isterseniz '0' : ")

        if gird1 == '0':
            print(self.programlistesi)
            gird1 = input("\nlisteden açmak istediğiniz program adını, işlem iptali için '0' :")
            if gird1 == "0":
                return
            else:
                if gird1 in self.programlistesi:
                    gird1 = program()
                    self.acik_programlar[i + 1] = gird1

        elif gird1 in self.programlistesi:
            gird1 = input(
                " \t {} adlı program açlılacaktır devam etmek için enter işlemi iptal etmek için '0' : ".format(gird3))
            if gird1 == "0":
                return
            else:
                gird1 = program()
                self.acik_programlar[i + 1] = gird1
                acikprog_guncelle()
        else:
            print("\nhatalı bir giriş yaptınızdan herhanngi bir program açamadınız")

    def acikprog_goruntule(self):
        # acikprogram_goruntule = self.acik_programlar
        # acikprogram_goruntule = sorted(acikprogram_goruntule)
        for item in self.acik_programlar.keys():
            print("açık programlar \n İşlem numarası : {},Program Adı: {}".format(item, self.acik_programlar))
        # for item in acikprogram_goruntule:
        #   print("Key : {} , Value : {}".format(item, acikprogram_goruntule[item]))

    def program_kapat(self):
        acikprog_goruntule()

        gird1 = input("\nlisteden kapatmak istediğiniz program işlem numarasını, işlem iptali için '0' : ")
        if gird1 == '0':
            return
        elif gird1 in self.acik_programlar:
            gird2 = input(
                " \t {} adlı program kapatılacaktır devam etmek için enter işlemi iptal etmek için '0' : ".format(
                    gird1))
            if gird2 == "0":
                return
            else:
                del self.acik_programlar[gird1]
        else:
            print("\nhatalı bir giriş yaptınızdan herhanngi bir programı kapatamadınız .")

    def program_yukle(self):
        print("\n", self.yuklenebilir_proglar)
        gird1 = input("listeden yüklemek istediğiniz uygulamanın adı nedir : ")

        if gird1 == '0':
            return
        elif gird1 in self.yuklenebilir_proglar:
            gird1 = program()
            self.programlistesi.append(gird1)
            self.yuklenebilir_proglar.remove(gird1)
        else:
            print("\nhatalı bir giriş yaptınızdan herhanngi bir işlem yapamadınız .")

    def program_kaldir(self):
        print("\n yüklü programlar", self.programlistesi)
        gird1 = input("listedeki hangi programı kaldırmak istiyorsunuz : ")
        if gird1 == '0':
            return
        elif gird1 in self.programlistesi:
            if gird1 in self.program_isimleri:
                print("program açık önce programı kapatınız .")
            else:
                self.yuklenebilir_proglar.append(gird1)
                self.programlistesi.remove(gird1)
        else:
            print("\nhatalı bir giriş yaptınızdan herhanngi bir işlem yapamadınız .")


def anasayfa():
    print("""
    #sınıf denemesi#  bilgisaya v1
    selam yapmak istediğiniz nedir
    
    1.bilgisayar seçmek yada bilgisayar sinifina yeni üye oluştur
    
    2.pc aç/kapa
    
    3.ses ayarları
    
    4.programlar
    
    5.kullanımlan pc özellikleri
    
    geri dönmek için '0' 
    
    çıkış için 'q' 
    
    not : oluşturulmak istenen hiç bir şeyin adı sayıdan ibaret olamaz
    """)


def kullanilan_sec():
    girdi = input("seçmek istediğiniz pc numarasını giriniz  liste için 'l': ")
    if input_control(girdi) == "int":
        kullanilan_pc = pc_listesi[int(girdi)]
    elif girdi == 'l':
        for k, v in pc_listesi.items():
            print("pc numarası : {},pc adı : {}".format(k, pc_listesi[k]))
    else:
        print("hatalı girdi")


pc_1 = Bilgisayar(pc_adi="pc_1", pc_gucdrurumu="kapalı")
pc_2 = Bilgisayar(pc_adi="pc_2", pc_gucdrurumu="kapalı")
pc_listesi = {1: pc_1, 2: pc_2}

kullanilan_pc = pc_listesi[1]

help(Bilgisayar)

while True:
    anasayfa()

    # print("\n",help(Bilgisayar()),"\n")

    girdi = input(" yapmak istediğiniz işlem nedir (örn. '1' , 'q' , '2') : ")

    if girdi == 'q':
        break
    elif input_control(girdi) == "str" or input_control(girdi) == "float":
        print("hatalı bir değer girdiniz ..")
        continue
    elif girdi == '1':
        girdi = input("pc seçmek için '2'veya oluşturmak istediğin pc numarası"
                      "(olan pclerin listesi için '1',geri dönmek için '0' ): ")
        if input_control(girdi) == "int":
            if girdi == '0':
                continue
            elif girdi == '1':
                print("\n 'pc_numarası','pc_adı'", pc_listesi)
                for i in pc_listesi.keys():
                    print("pc numarsı: {},pc adı: {}".format(i, pc_listesi[i].pc_adi))

            elif girdi == '2':
                kullanilan_sec()
            else:
                if girdi in pc_listesi.keys():
                    print("zaten bu numarada bir pc bulunuyor")
                else:
                    gird2 = input("bilgisayara koymak istediğiniz ad nedir : ")
                    pc_listesi[int(girdi)] = gird2
                    yenipc_isim = "pc_" + str(gird2)
                    pc_listesi[int(girdi)] = Bilgisayar(pc_adi=str(yenipc_isim))
        else:
            if input_control(girdi) == 'float':
                print("seni çakal seni")
                break
            else:
                if girdi in pc_listesi.values():
                    print("zaten bu isimde bir pc bulunuyor")
                else:
                    gird2 = input("bilgisayara koymak istediğiniz numara nedir : ")
                    a = 0
                    while a in pc_listesi.keys():
                        a += 1
                        try:
                            pc_listesi[a] = sorted(pc_listesi.keys())[pc_listesi[pc_listesi[a]]]
                        except KeyError:
                            continue
                    pc_listesi[int(gird2)] = girdi
                    yenipc_isim = "pc_" + str(gird2)
                    pc_listesi[int(gird2)] = Bilgisayar(pc_adi=str(yenipc_isim))
                    print("pc başarıyla oluşturuldu")
    elif girdi == '2':
        girdi = input("kullanılan pcyi açmak/kapatmak '1' pcyi seçmek '2' geriye dönmek '0' : ")
        if girdi == '0':
            continue
        elif girdi == '1':
            kullanilan_pc.pc_gucdurumu = "açık" if kullanilan_pc.pc_gucdurumu == "kapalı" else "kapalı"
        elif girdi == '2':
            kullanilan_sec()
            girdi = input("kullanılan pcyi açmak/kapatmak '1' geriye dönmek '0' : ")
            if girdi == '0':
                continue
            elif girdi == '1':
                kullanilan_pc.pc_gucdurumu = "açık" if kullanilan_pc.pc_gucdurumu == "kapalı" else "kapalı"
            else:
                print("hatalı bir veri girdiniz")
        else:
            print("hatalı bir veri girdiniz")
            continue
    elif girdi == '3':
        girdi = input("kullanılan pc ses ayarları '1' pcyi seçmek '2' geriye dönmek '0' : ")
        if girdi == '0':
            continue
        elif girdi == '1':
            kullanilan_pc.pc_ses()
        elif girdi == '2':
            kullanilan_sec()
        else:
            print("hatalı bir veri girdiniz")
    elif girdi == '4':
        print("{} numaralı pc de işlem yapımlmaktadır \n".format(get_key(kullanilan_pc, pc_listesi)))
        girdi = input("başka pc seçmek istermisiniz e/h varsayılan(h) :")
        if evet_hayir(girdi):
            kullanilan_sec()
        else:
            girdi = input("""
                programlarla yapmak istediğiniz işlem nedir
                
                1.program aç/kapa
                2.program yukle/kaldir
            
            """)
            if girdi == '0':
                continue
            elif girdi == '1':
                girdi == print("program,açmak için a kapatmak için k : ")
                if girdi == '0':
                    continue
                elif girdi == 'a' or girdi == 'A':
                    kullanilan_pc.program_ac()
                elif girdi == 'k' or girdi == 'K':
                    kullanilan_pc.program_kapat()
                else:
                    print("hatalı bir veri girdiniz")
            elif girdi == '2':
                girdi == print("program,yuklemek için y kaldırmak için k : ")
                if girdi == '0':
                    continue
                elif girdi == 'y' or girdi == 'Y':
                    kullanilan_pc.program_yukle()
                elif girdi == 'K' or girdi == 'K':
                    kullanilan_pc.program_kaldir()
                else:
                    print("hatalı bir veri girdiniz")
            else:
                print("hatalı bir veri girdiniz")
    elif girdi == '5':
        girdi = input(" özelliklerini görüntülemek istediğiniz pc numarası ,liste için 'l' : ")
        if girdi == 'l':
            print(pc_listesi)
        elif input_control(girdi) == 'int':
            print(pc_listesi[int(girdi)])
        else:
            print("hatalı bir veri girdiniz")
