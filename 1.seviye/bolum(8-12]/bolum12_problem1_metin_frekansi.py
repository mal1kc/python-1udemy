# Problem 1
#
# Elinizde uzunca bir string olsun.
#
#             "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
#
#
# Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
#
# İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık.

class Dosya:
    def __init__(self, dosya_yolu):
        with open(dosya_yolu, "r", encoding="utf-8")as file:
            dosya_icerigi = file.read()

            kelimeler = dosya_icerigi.split()
            self.sade_harfler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                tek_harf = list(i)

                for j in tek_harf:
                    self.sade_harfler.append(j)

    # def tum_harfler(self):
    #
    #     kelimeler_kumesi = set()
    #
    #     for i in self.sade_harfler:
    #         kelimeler_kumesi.add(i)
    #     print("Tüm kelimeler ................")
    #     for i in kelimeler_kumesi:
    #         print(i)
    #         print("***************")

    def harf_frekansi(self):
        harf_sozluk = dict()

        for i in self.sade_harfler:
            if i in harf_sozluk:
                harf_sozluk[i] += 1
            else:
                harf_sozluk[i] = 1
        for harf, sayi in harf_sozluk.items():
            print("dosyada {} harfinden {} tane var ".format(harf, sayi))


dosya = Dosya("bolum12_problem1_metin_frekansi_metin.txt")

print(dosya.sade_harfler)
print("\n*********************\n")

dosya.harf_frekansi()
