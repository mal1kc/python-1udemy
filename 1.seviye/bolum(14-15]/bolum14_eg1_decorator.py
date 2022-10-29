def ekstra(fonk):
    def wrapper(sayilar):
        ciftler_toplami = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0
        for sayi in sayilar:
            if sayi % 2 == 0:
                ciftler_toplami += sayi
                cift_sayilar += 1
            else:
                tekler_toplami += sayi
                tek_sayilar += 1

        print("Teklerin Ortalaması : ", tekler_toplami / tek_sayilar)
        print("Çiftlerin Ortalaması : ", ciftler_toplami / cift_sayilar)
        fonk(sayilar)

    return wrapper


@ekstra
def ortalambul(sayilar):
    toplam = 0

    for sayi in sayilar:
        toplam += sayi
    print("Genel Ortalama : ", toplam / len(sayilar))


ortalambul([1, 2, 3, 4, 5, 7, 8, 8, 9, 9, 9, 9])
