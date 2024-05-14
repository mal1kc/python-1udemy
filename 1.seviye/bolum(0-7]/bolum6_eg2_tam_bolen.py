"""

Sayının tam bölenlerini bulma

"""

def tambolen(sayi):
    tambolenler = []
    for i in range(1,sayi+1):
        if (sayi % i == 0 ):
            tambolenler.append(i)
        else:
            continue
    return tambolenler

while True:
    sayi = input("Tam bölenlerini öğrenmek istediğiniz bir sayı giriniz (çıkmak için q ya basın): ")
    if (sayi == 'q'):
        print("iyi günler, program kapatıdı")
        break
    else:
        sayi = int(sayi)
        if len(tambolen(sayi)) > 1 :
            print("giridiğiniz {} sayısının tam bölenleri {} sayılarıdır ".format(sayi, tambolen(sayi)))
        else:
            print("giridiğiniz {} sayısının kendinden başka bir böleni yoktur".format(sayi))
