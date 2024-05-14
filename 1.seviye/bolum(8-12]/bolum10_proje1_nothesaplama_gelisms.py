def not_hesapla(satir):
    satir = satir[:-1]

    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

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
        harf = "kaldı"

    if harf == "kaldı":
        return liste
    else:
        return isim + "----------------->" + harf + "\n"


with open("bolum10_eg1_nothesaplama.txt", "r", encoding="utf-8")as file1:
    eklenecekler_listesi = []
    kalanlar_listesi = []
    for i in file1:
        if type(not_hesapla(i)) == str:
            eklenecekler_listesi.append(not_hesapla(i))
        else:
            kalanlar_listesi.append(not_hesapla(i))

    with open("bolum10_eg1_nothesaplama-sonuc.txt", "w", encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)

    with open("bolum10_proje1_nothesaplama-kalanlar.txt", "w", encoding="utf-8") as file3:
        for i in range(len(kalanlar_listesi)):
            file3.write("{} bu notları aldığından kaldı --> {} {} {} \n".format(kalanlar_listesi[i][0],
                                                                                kalanlar_listesi[i][1],
                                                                                kalanlar_listesi[i][2],
                                                                                kalanlar_listesi[i][3]))
