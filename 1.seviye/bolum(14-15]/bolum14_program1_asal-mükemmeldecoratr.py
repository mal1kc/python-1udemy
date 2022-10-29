#
# Program
#
# 1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. Daha sonra bir tane decorator fonksiyon
# kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.

def mukemelsayidecoratr(func):
    def wrapper(aralik):
        mukemelsayilar = list()
        for sayi in aralik:
            i = 1
            toplam = 0
            for i in range(1, sayi):
                if sayi % i == 0:
                    toplam += i
            if toplam == sayi:
                mukemelsayilar.append(sayi)
            else:
                continue
        print("{0}-{1} arasındaki {2} sayıların içindeki mükemmel sayilar : ".format(min(aralik), max(aralik),
                                                                                     len(aralik)))
        for j in mukemelsayilar:
            print(j,",",end="\t")
        func(aralik)
    return wrapper


@mukemelsayidecoratr
def asalsayibul(aralik):
    asal_sayilar = list()
    for sayi in aralik:
        if sayi > 1:
            for j in range(2, sayi):
                if sayi % j == 0:
                    break
            else:
                asal_sayilar.append(sayi)
    print("\n{0}-{1} arasındaki {2} sayıların içindeki asal sayilar : ".format(min(aralik), max(aralik), len(aralik)))
    for i in asal_sayilar:
        print(i)


asalsayibul(range(1, 1001))