# Problem 1
#
# Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
#
#          [(3,4),(10,3),(5,6),(1,9)]
#
# Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına
# bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.
#
#          [12, 30, 30, 9]
#
# Not : map() fonksiyonunu kullanmaya çalışın.
print("----------------------\n")
liste_dk = [(3, 2), (9, 3), (5, 2), (40, 85), (20, 36), (15, 12)]


def alan_hesapla(demet):
    return demet[0] * demet[1]


print(list(map(alan_hesapla, liste_dk)))
print("\n----------------------")
# Problem 2
#
# Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.
#
#      [(3,4,5),(6,8,10),(3,10,7)]
#
# Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen
# belirten kenarları bulunduran listeyi ekrana yazdırın.
#
#      [(3, 4, 5), (6, 8, 10)]
#
# * Not: filter() fonksiyonunu kullanmaya çalışın. *
print("----------------------\n")

liste_2 = [(3, 4, 5), (6, 8, 10), (3, 10, 7), (6, 9, 8), (1, 6, 8), (7, 36, 10), (21, 54, 12)]


def ucgen_mi(cisim):
    # Ia + bI > c > Ib - cI
    if abs(cisim[0] + cisim[1]) > abs(cisim[2]) and (
            (abs(cisim[0] + cisim[2]) > cisim[1]) and abs(cisim[1] + cisim[2]) > cisim[0]):
        return True
    return False


print(list(filter(ucgen_mi, liste_2)))

print("\n----------------------")
# Problem 3
#
# Elinizde şöyle bir liste bulunsun.
#
#     [1,2,3,4,5,6,7,8,9,10]
#
# Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.
#
# Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.
from functools import reduce

print("----------------------\n")

liste_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ciftler = list(filter(lambda x: x % 2 == 0, liste_3))

print(reduce(lambda x, y: x + y, ciftler))

print("\n----------------------")
# Problem 4
#
# Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.
#
#         isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#
#         soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
#
# Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
#
# *Not: zip() fonksiyonunu kullanmaya çalışın. *
print("----------------------\n")

isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve", "Erdal"]
soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat", "İtoğlu"]

for i, j in zip(isimler, soyisimler):
    print(i, j)

print("\n----------------------")
