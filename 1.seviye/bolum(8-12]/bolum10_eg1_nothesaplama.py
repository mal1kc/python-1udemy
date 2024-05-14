def not_hesapla(satir):
    satir = satir[:-1]

    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return isim + "----------------->" + harf + "\n"


with open("bolum10_eg1_nothesaplama.txt", "r", encoding="utf-8")as dosya:

    eklenecekler_listesi = []
    for i in dosya:
        eklenecekler_listesi.append(not_hesapla(i))
    with open("bolum10_eg1_nothesaplama-sonuc.txt", "w", encoding="utf-8") as cikti:
        for i in eklenecekler_listesi:
            cikti.write(i)
