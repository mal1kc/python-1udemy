# bolum 8 proje 3
#   aklıma hyapabileceiğim hayvan özelliği gelmedi----------- yarım bırakıldı------------------
# Bu projede ise 4 tane sınıfı oluşturun.
#
# Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
#
# Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek
# özellikler ve metodlar ekleyin.
##
## havlama
##
##
##
#
# Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek
# özellikler ve metodlar ekleyin.
#
# At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek
# özellikler ve metodlar ekleyin.
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
        int(a)
    except ValueError:
        try:
            float(a)
        except ValueError:
            return "str"
        else:
            return "float"
    else:
        return "int"


class Hayvan:

    def __init__(self, cinsiyet="erkek", ayak_sayisi=2, solunum_tipi="akciğer", yasam_alani="kara"):
        self.cinsiyet = cinsiyet
        self.ayak_sayisi = ayak_sayisi
        self.solunum_tipi = solunum_tipi
        self.yasam_alani = yasam_alani

    def ise(self,tur):
        print("{} her yeri ıslattı".format(tur))


class Kopek(Hayvan):

    def __init__(self, cinsiyet=1, ayak_sayisi=2, solunum_tipi="akciğer", yasam_alani="kara"):
        super().__init__(cinsiyet, ayak_sayisi, solunum_tipi, yasam_alani)
        self.cinsiyet = cinsiyet
        self.ayak_sayisi = ayak_sayisi
        self.solunum_tipi = solunum_tipi
        self.yasam_alani = yasam_alani


kopek_1 = Hayvan()

kopek_1.ise("kopek")

print(kopek_1.cinsiyet, kopek_1.yasam_alani)

